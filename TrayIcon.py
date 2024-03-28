import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMenu, QWidget, QSystemTrayIcon, QAction

import UI


class TrayIcon:
    _iconPath: list
    _iconImage: QIcon
    _mainWindow: QWidget
    _trayActions: dict
    _trayMenu: QMenu
    trayIcon: QSystemTrayIcon

    def __init__(self, mainWindow):
        self._mainWindow = mainWindow
        self._iconPath = ["icon/tray_icon.png", r"D:\project\python\N2N-Client-GUI\icon/tray_icon.png"]
        self._iconImage = QIcon()
        self._trayActions = {}
        self._trayMenu = None

    def setup(self):
        self._initTray()
        self._setupHandle()

    def _initTray(self):
        try:
            self._iconImage = QIcon(self._iconPath[0])
        except Exception:
            self._iconImage = QIcon(self._iconPath[1])

        self._initMenu()

        self.trayIcon = QSystemTrayIcon(self._mainWindow)
        self.trayIcon.setContextMenu(self._trayMenu)
        self.trayIcon.setIcon(self._iconImage)
        self.trayIcon.setToolTip("N2N")
        self.trayIcon.show()

    def _initMenu(self):

        self._trayActions = {
            "open": QAction("打开", self._mainWindow),
            "exit": QAction("退出", self._mainWindow),
            "doConnect": QAction("连接", self._mainWindow),
            "disConnect": QAction("断开连接", self._mainWindow),
            "openSource": QAction("开源仓库", self._mainWindow)
        }

        self._trayMenu = QMenu(self._mainWindow)
        self._trayMenu.addAction(self._trayActions["open"])
        self._trayMenu.addSeparator()
        self._trayMenu.addAction(self._trayActions["doConnect"])
        self._trayMenu.addAction(self._trayActions["disConnect"])
        self._trayMenu.addSeparator()
        self._trayMenu.addAction(self._trayActions["openSource"])
        self._trayMenu.addSeparator()
        self._trayMenu.addAction(self._trayActions["exit"])

        font = QFont()
        font.setBold(True)
        self._trayActions["open"].setFont(font)
        self._trayActions["disConnect"].setEnabled(False)

    def _setupHandle(self):
        self._setEventsHandle()

    def showMessage(self, msg: str, title: str = "通知", icon: int = QSystemTrayIcon.MessageIcon.NoIcon):
        self.trayIcon.showMessage(title, msg, icon)

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
        self._trayActions[actionName].triggered.connect(func)

    def _handle_trayIcon_open(self):
        self._mainWindow.setVisible(True)
        self._mainWindow.activateWindow()

    def _handle_trayIcon_exit(self):
        QCoreApplication.quit()

    def _handle_trayIcon_doConnect(self):
        self._trayActions["doConnect"].setEnabled(False)
        self._trayActions["disConnect"].setEnabled(True)

    def _handle_trayIcon_disConnect(self):
        self._trayActions["doConnect"].setEnabled(True)
        self._trayActions["disConnect"].setEnabled(False)

    def _handle_trayIcon_openSource(self):
        os.system("start https://github.com/Icezero0/N2N-Client-GUI")

    def _handle_trayIcon_activated(self, reason):
        if reason == QSystemTrayIcon.Critical or reason == QSystemTrayIcon.MiddleClick or reason == QSystemTrayIcon.DoubleClick:
            self._handle_trayIcon_open()
        elif reason == QSystemTrayIcon.Context:
            self.trayIcon.contextMenu().show()
