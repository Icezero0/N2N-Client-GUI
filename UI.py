from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabWidget


class UI(object):
    TabWidget: QTabWidget

    def __init__(self, TabWidget):
        # self.trayIcon = None
        self.TabWidget = TabWidget

    def setup(self):
        self.setupUi()
        # self.setupTrayIcon()
        self.setEventsHandle()

    def setupUi(self):
        self.TabWidget.setObjectName("TabWidget")
        self.TabWidget.setWindowIcon(QtGui.QIcon("icon/icon.png"))
        self.TabWidget.resize(415, 440)
        self.TabWidget.setFixedSize(415, 440)
        self.TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.TabWidget.setIconSize(QtCore.QSize(16, 16))
        self.TabWidget.setTabsClosable(False)
        self.TabWidget.setTabBarAutoHide(False)
        self.mainTab = QtWidgets.QWidget()
        self.mainTab.setObjectName("mainTab")
        self.serverFrame = QtWidgets.QFrame(self.mainTab)
        self.serverFrame.setGeometry(QtCore.QRect(10, 0, 390, 80))
        self.serverFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.serverFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.serverFrame.setLineWidth(1)
        self.serverFrame.setMidLineWidth(0)
        self.serverFrame.setObjectName("serverFrame")
        self.serverAddressLabel = QtWidgets.QLabel(self.serverFrame)
        self.serverAddressLabel.setGeometry(QtCore.QRect(90, 40, 290, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.serverAddressLabel.setFont(font)
        self.serverAddressLabel.setTextFormat(QtCore.Qt.AutoText)
        self.serverAddressLabel.setObjectName("serverAddressLabel")
        self.serverSelectComboBox = QtWidgets.QComboBox(self.serverFrame)
        self.serverSelectComboBox.setGeometry(QtCore.QRect(90, 10, 200, 20))
        self.serverSelectComboBox.setObjectName("serverSelectComboBox")
        self.serverSelectComboBox.addItem("")
        self.serverTitleLabel = QtWidgets.QLabel(self.serverFrame)
        self.serverTitleLabel.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self.serverTitleLabel.setObjectName("serverTitleLabel")
        self.serverManagePushButton = QtWidgets.QPushButton(self.serverFrame)
        self.serverManagePushButton.setGeometry(QtCore.QRect(300, 10, 80, 20))
        self.serverManagePushButton.setObjectName("serverManagePushButton")
        self.groupNameFrame = QtWidgets.QFrame(self.mainTab)
        self.groupNameFrame.setGeometry(QtCore.QRect(10, 90, 390, 50))
        self.groupNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.groupNameFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.groupNameFrame.setObjectName("groupNameFrame")
        self.groupnameTitleLabel = QtWidgets.QLabel(self.groupNameFrame)
        self.groupnameTitleLabel.setGeometry(QtCore.QRect(10, 10, 60, 30))
        self.groupnameTitleLabel.setObjectName("groupnameTitleLabel")
        self.groupnameLineEdit = QtWidgets.QLineEdit(self.groupNameFrame)
        self.groupnameLineEdit.setGeometry(QtCore.QRect(90, 10, 280, 30))
        self.groupnameLineEdit.setObjectName("groupnameLineEdit")
        self.localipFrame = QtWidgets.QFrame(self.mainTab)
        self.localipFrame.setGeometry(QtCore.QRect(10, 150, 390, 50))
        self.localipFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.localipFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.localipFrame.setObjectName("localipFrame")
        self.localipTitleLabel = QtWidgets.QLabel(self.localipFrame)
        self.localipTitleLabel.setGeometry(QtCore.QRect(10, 10, 60, 30))
        self.localipTitleLabel.setObjectName("localipTitleLabel")
        self.localipLineEdit = QtWidgets.QLineEdit(self.localipFrame)
        self.localipLineEdit.setGeometry(QtCore.QRect(90, 10, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.localipLineEdit.setFont(font)
        self.localipLineEdit.setObjectName("localipLineEdit")
        self.localipAutoCheckBox = QtWidgets.QCheckBox(self.localipFrame)
        self.localipAutoCheckBox.setGeometry(QtCore.QRect(280, 10, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.localipAutoCheckBox.setFont(font)
        self.localipAutoCheckBox.setObjectName("localipAutoCheckBox")
        self.connectionFrame = QtWidgets.QFrame(self.mainTab)
        self.connectionFrame.setGeometry(QtCore.QRect(10, 210, 390, 200))
        self.connectionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connectionFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.connectionFrame.setObjectName("connectionFrame")
        self.connectionPushButton = QtWidgets.QPushButton(self.connectionFrame)
        self.connectionPushButton.setGeometry(QtCore.QRect(310, 160, 75, 30))
        self.connectionPushButton.setObjectName("connectionPushButton")
        self.connectionMsgTextBrowser = QtWidgets.QTextBrowser(self.connectionFrame)
        self.connectionMsgTextBrowser.setGeometry(QtCore.QRect(10, 10, 370, 140))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.connectionMsgTextBrowser.setFont(font)
        self.connectionMsgTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.connectionMsgTextBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.connectionMsgTextBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.connectionMsgTextBrowser.setLineWidth(1)
        self.connectionMsgTextBrowser.setObjectName("connectionMsgTextBrowser")
        self.TabWidget.addTab(self.mainTab, "")

        self.retranslateUi(self.TabWidget)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.TabWidget)

    # def setupTrayIcon(self):
        # self.trayIcon = TrayIcon.TrayIcon(self.TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "N2N"))
        self.serverAddressLabel.setText(_translate("TabWidget", "52.192.105.70:3000"))
        self.serverSelectComboBox.setItemText(0, _translate("TabWidget", "节点 1 : 日本 - 东京"))
        self.serverTitleLabel.setText(_translate("TabWidget", "服务器节点"))
        self.serverManagePushButton.setText(_translate("TabWidget", "管理节点"))
        self.groupnameTitleLabel.setText(_translate("TabWidget", "群组名"))
        self.groupnameLineEdit.setText(_translate("TabWidget", "GDJAY1"))
        self.localipTitleLabel.setText(_translate("TabWidget", "本机地址"))
        self.localipLineEdit.setInputMask(_translate("TabWidget", "000. 000. 000. 000;_"))
        self.localipLineEdit.setText(_translate("TabWidget", ". . . "))
        self.localipAutoCheckBox.setText(_translate("TabWidget", "自动分配"))
        self.connectionPushButton.setText(_translate("TabWidget", "连接"))
        TabWidget.setTabText(TabWidget.indexOf(self.mainTab), _translate("TabWidget", "主页"))

    def setEventsHandle(self):
        # set tab widget elements event handle
        self.connectionPushButton.clicked.connect(self.handle_connectionPushButton_clicked)


    def Log_connectionTextBrowser(self, text: str, color: str = "black", margin_top: str = "2px", margin_bottom: str = "2px"):
        _translate = QtCore.QCoreApplication.translate
        self.connectionMsgTextBrowser.append(_translate("TabWidget",
                                                        f"<p style=\""
                                                        f"margin-top:\'{margin_top}\';"
                                                        f"margin-bottom:\'{margin_bottom}\';"
                                                        f"color:{color};"
                                                        f"\">{text}</p>"))

    def handle_connectionPushButton_clicked(self):
        local_ip = self.localipLineEdit.text()
        self.localipLineEdit.setReadOnly(not self.localipLineEdit.isReadOnly())
        self.Log_connectionTextBrowser(local_ip)

    # def handle_trayIcon_open(self):
    #     self.TabWidget.setVisible(True)
    #     self.TabWidget.activateWindow()

    # def handle_trayIcon_exit(self):
    #     QCoreApplication.quit()
    #
    # def handle_trayIcon_doConnect(self):
    #     self.trayIcon.trayActions["doConnect"].setEnabled(False)
    #     self.trayIcon.trayActions["disConnect"].setEnabled(True)
    #
    # def handle_trayIcon_disConnect(self):
    #     self.trayIcon.trayActions["doConnect"].setEnabled(True)
    #     self.trayIcon.trayActions["disConnect"].setEnabled(False)
    #
    # def handle_trayIcon_openSource(self):
    #     os.system("start https://github.com/Icezero0/N2N-Client-GUI")
    #
    # def handle_trayIcon_activated(self, reason):
    #     if reason == QSystemTrayIcon.Critical or reason == QSystemTrayIcon.MiddleClick or reason == QSystemTrayIcon.DoubleClick:
    #         self.handle_trayIcon_open()
    #     elif reason == QSystemTrayIcon.Context:
    #         self.trayIcon.trayIcon.contextMenu().show()
