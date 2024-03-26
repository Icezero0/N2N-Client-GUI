import ctypes
import os
import sys
import time

import N2N

N2NEXE = "N2N\\edge.exe"
groupName = "GDJAY1"
serverAddress = "52.192.105.70:3000"
localAddress = "192.168.5.2"


def _isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if __name__ == '__main__':

    # 获取管理员权限
    if not _isAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit(0)

    print("hello world")
    N2N_obj = N2N.N2N()
    N2N_obj.setConfig(serverAddress, groupName, localAddress)
    N2N_obj.start()
    N2N_obj.tryConnect()

    time.sleep(3)
    input("tap to disconnect")
    N2N_obj.disConnect()
    input("tap to connect")
    N2N_obj.tryConnect_autoIP()
    input("tap to disconnect")
    N2N_obj.disConnect()

    input("tap to stop")
    N2N_obj.stop()
    os.system("pause")