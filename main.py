import ctypes
import os
import sys

import configtool
import trayicon


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

    configObj = configtool.configTool()
    errCode, jsonObj = configObj.readSettings()
    print(jsonObj)
    configObj.saveSettings(jsonObj)

    trayiconObj = trayicon.trayicon()
    trayiconObj.create_tray_icon()

    os.system("pause")

    # print("hello world")
    # N2N_obj = N2N.N2N()
    # N2N_obj.setConfig(serverAddress, groupName, localAddress)
    # N2N_obj.start()
    # N2N_obj.tryConnect()
    #
    # time.sleep(3)
    # input("tap to disconnect")
    # N2N_obj.disConnect()
    # input("tap to connect")
    # N2N_obj.tryConnect_autoIP()
    # input("tap to disconnect")
    # N2N_obj.disConnect()
    #
    # input("tap to stop")
    # N2N_obj.stop()
    # os.system("pause")
