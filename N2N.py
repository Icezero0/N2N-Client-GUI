import io
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
    # n2n edge.exe相关参数
    _N2NPID: int
    _N2NEXE: str = "N2N/edge.exe"
    _groupName: str
    _serverAddr: str
    _localIP: str

    # 同步线程控制
    _listeningCon: threading.Condition
    _historyLock: threading.Lock

    # 状态
    _isConnecting: bool
    isAlive: bool

    def __init__(self):
        threading.Thread.__init__(self)
        self._N2NPID = 0
        self._pipe = None

        self._listeningCon = threading.Condition()
        self._historyLock = threading.Lock()

        self._isConnecting = False
        self.isAlive = False

    def setConfig(self, serverAddr: str, groupName: str, localIP: str):
        self._groupName = groupName
        self._serverAddr = serverAddr
        self._localIP = localIP

    def start(self):
        self.isAlive = True
        threading.Thread.start(self)

    def stop(self):
        if self._isConnecting:
            self.disConnect()
        self.isAlive = False
        self._knock()

    def tryConnect(self):
        if self._isConnecting:
            return True
        else:
            try:
                self._pipe = subprocess.Popen(
                    f"{self._N2NEXE} -c {self._groupName} -a {self._localIP} -l {self._serverAddr}",
                    stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
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

    def tryConnect_autoIP(self):
        if self._isConnecting:
            return True
        else:
            try:
                self._pipe = subprocess.Popen(
                    f"{self._N2NEXE} -c {self._groupName} -l {self._serverAddr}",
                    stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE
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

    def run(self):
        self._listeningCon.acquire()

        while self.isAlive:
            while self._isConnecting:
                info = b''
                msg = ""
                try:
                    success, msg = _decode(info)
                    while not success:
                        info = info + self._pipe.stdout.read(1)
                        success, msg = _decode(info)
                except Exception as e:
                    # traceback.print_exc(e)
                    break
                print(msg, end="")

            if self.isAlive:
                self._listeningCon.wait(2)
            print("child check")

        self._listeningCon.release()

    def _knock(self):
        with self._listeningCon:
            self._listeningCon.notify()

    def _killN2N(self):
        if self._N2NPID != 0:
            os.kill(self._N2NPID, signal.SIGTERM)
