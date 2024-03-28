import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMenu, QWidget, QSystemTrayIcon, QAction

import UI


class TrayIcon:
    iconPath: str
    iconImage: QIcon
    mainWindow: QWidget
    trayActions: dict
    trayMenu: QMenu
    trayIcon: QSystemTrayIcon

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.iconPath = "icon/tray_icon.png"
        self.iconImage = QIcon()
        self.trayActions = {}
        self.trayMenu = None
        self._initTray()

    def _initTray(self):
        try:
            self.iconImage = QIcon(self.iconPath)
        except FileNotFoundError:
            self.iconImage = QIcon.fromTheme("edit-undo")

        self._initMenu()

        self.trayIcon = QSystemTrayIcon(self.mainWindow)
        self.trayIcon.setContextMenu(self.trayMenu)
        self.trayIcon.setIcon(self.iconImage)
        self.trayIcon.setToolTip("N2N")
        self.trayIcon.show()

        self.trayIcon.showMessage("test", "123", QSystemTrayIcon.MessageIcon.NoIcon)

    def _initMenu(self):

        self.trayActions = {
            "open": QAction("打开", self.mainWindow),
            "exit": QAction("退出", self.mainWindow),
            "doConnect": QAction("连接", self.mainWindow),
            "disConnect": QAction("断开连接", self.mainWindow),
            "openSource": QAction("开源", self.mainWindow)
        }

        self.trayMenu = QMenu(self.mainWindow)
        self.trayMenu.addAction(self.trayActions["open"])
        self.trayMenu.addAction(self.trayActions["doConnect"])
        self.trayMenu.addAction(self.trayActions["disConnect"])
        self.trayMenu.addAction(self.trayActions["openSource"])
        self.trayMenu.addAction(self.trayActions["exit"])

        font = QFont()
        font.setBold(True)
        self.trayActions["open"].setFont(font)
        self.trayActions["disConnect"].setEnabled(False)


    def setupHandle(self):
        self._setEventsHandle()

    def _setEventsHandle(self):
        # set tray icon event handle
        self._setActionHandle("open", self._handle_trayIcon_open)
        self._setActionHandle("exit", self._handle_trayIcon_exit)
        self._setActionHandle("doConnect", self._handle_trayIcon_doConnect)
        self._setActionHandle("disConnect", self._handle_trayIcon_disConnect)
        self._setActionHandle("openSource", self._handle_trayIcon_openSource)
        self.trayIcon.messageClicked.connect(self._handle_trayIcon_open)
        self.trayIcon.activated.connect(self._handle_trayIcon_activated)

    def _setActionHandle(self, actionName: str, func):
        self.trayActions[actionName].triggered.connect(func)

    def _handle_trayIcon_open(self):
        self.mainWindow.setVisible(True)
        self.mainWindow.activateWindow()

    def _handle_trayIcon_exit(self):
        QCoreApplication.quit()

    def _handle_trayIcon_doConnect(self):
        self.trayActions["doConnect"].setEnabled(False)
        self.trayActions["disConnect"].setEnabled(True)

    def _handle_trayIcon_disConnect(self):
        self.trayActions["doConnect"].setEnabled(True)
        self.trayActions["disConnect"].setEnabled(False)

    def _handle_trayIcon_openSource(self):
        os.system("start https://github.com/Icezero0/N2N-Client-GUI")

    def _handle_trayIcon_activated(self, reason):
        if reason == QSystemTrayIcon.Critical or reason == QSystemTrayIcon.MiddleClick or reason == QSystemTrayIcon.DoubleClick:
            self._handle_trayIcon_open()
        elif reason == QSystemTrayIcon.Context:
            self.trayIcon.contextMenu().show()
