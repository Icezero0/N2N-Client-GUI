import ctypes
import os
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget

import configtool
import main_window
import trayicon



if __name__ == '__main__':
    # 获取管理员权限
    # if not _isAdmin():
    #     ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
    #     exit(0)

    app = QApplication(sys.argv)

    mainWindow = QTabWidget()
    uiMainWindow = main_window.Ui_TabWidget()
    uiMainWindow.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

    # configObj = configtool.configTool()
    # errCode, jsonObj = configObj.readSettings()
    # print(jsonObj)
    # configObj.saveSettings(jsonObj)
    #
    # trayiconObj = trayicon.trayicon()
    # trayiconObj.create_tray_icon()
    #
    # os.system("pause")

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
