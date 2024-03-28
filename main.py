import os
import sys
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QWidget

import configtool
import UI
import TrayIcon


class MainWindow(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self)

    def closeEvent(self, event):
        self.setVisible(False)
        event.ignore()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)

    mainWindow = MainWindow()

    ui = UI.UI(mainWindow)
    ui.setup()

    trayIcon = TrayIcon.TrayIcon(mainWindow)
    trayIcon.setup()

    ui.setupConfig()


    mainWindow.show()

    sys.exit(app.exec_())

    # configObj = configtool.configTool()
    # errCode, jsonObj = configObj.readSettings()
    # print(jsonObj)
    # configObj.saveSettings(jsonObj)
    #
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
