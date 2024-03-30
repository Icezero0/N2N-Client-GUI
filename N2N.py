import os
import signal
import subprocess
import threading
import time


def _decode(info: bytes):
    if not info:
        return False, ""
    ret = ""
    try:
        ret = info.decode("utf8")
    except Exception as e:
        return False, ret
    return True, ret


class N2N(threading.Thread):
    _checkout_: float = 2

    # n2n edge.exe相关对象
    _N2NPID: int
    _N2NEXE: str = "N2N/edge.exe"
    _groupName: str
    _serverAddr: str
    _localIP: str

    # 同步线程控制
    _listeningCon: threading.Condition

    # 状态
    _isConnecting: bool
    isAlive: bool

    def __init__(self, ui):
        threading.Thread.__init__(self)
        self._ui = ui
        self._groupName = ""
        self._serverAddr = ""
        self._localIP = ""
        self._autoIP = False
        self._N2NPID = 0
        self._pipe = None
        self._history = ""

        self._listeningCon = threading.Condition()
        # self._historyLock = threading.Lock()

        self._isConnecting = False
        self.isAlive = False

    def setConfig(self, serverAddr: str, groupName: str, localIP: str, autoIP: bool):
        self._groupName = groupName
        self._serverAddr = serverAddr
        self._localIP = localIP
        self._autoIP = autoIP

    def start(self):
        self.isAlive = True
        threading.Thread.start(self)

    def stop(self):
        if self._isConnecting:
            self.disConnect()
        self.isAlive = False
        self._knock()

    def tryConnect(self) -> bool:
        if self._isConnecting:
            return True
        else:
            self._killN2N()
            try:
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
                if self._autoIP:
                    self._pipe = subprocess.Popen(
                        f"{self._N2NEXE} -c {self._groupName} -l {self._serverAddr}",
                        stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo
                    )
                    self._N2NPID = self._pipe.pid
                else:
                    print(f"{self._N2NEXE} -c {self._groupName} -a {self._localIP} -l {self._serverAddr}")
                    self._pipe = subprocess.Popen(
                        f"{self._N2NEXE} -c {self._groupName} -a {self._localIP} -l {self._serverAddr}",
                        stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo
                    )
                    self._N2NPID = self._pipe.pid
            except Exception as e:
                # traceback.print_exc(e)
                self._pipe = None
                self._N2NPID = 0
                return False

            self._isConnecting = True
            self._knock()
            return True

    def disConnect(self):
        if self._isConnecting:
            self._isConnecting = False
            self._killN2N()
            self._pipe = None

    def _analyzeLine(self, msg: str):
        if msg == "":
            return
        self._ui.log_append(msg)
        time.sleep(0.1)
        print("analyze : " + msg)

    def run(self):
        self._listeningCon.acquire()

        while self.isAlive:
            msg = ""
            while self._isConnecting:
                info = b''
                try:
                    success, ch = _decode(info)
                    while not success:
                        info = info + self._pipe.stdout.read(1)
                        success, ch = _decode(info)
                except Exception as e:
                    # traceback.print_exc(e)
                    break
                msg += ch
                if msg.endswith("\n"):
                    self._analyzeLine(msg.replace("\n", ""))
                    msg = ""

            if self.isAlive:
                self._listeningCon.wait(self._checkout_)
            print("n2n check")

        self._listeningCon.release()

    def _knock(self):
        # 激活正在等待的线程
        with self._listeningCon:
            self._listeningCon.notify()

    def _killN2N(self):
        # 关闭n2n.exe
        if self._N2NPID != 0:
            os.kill(self._N2NPID, signal.SIGTERM)
        else:
            os.system("taskkill /f /im edge.exe")
