import re

from PyQt5 import QtCore, QtGui, QtWidgets

from N2N import N2N
from configtool import ConfigTool


class UI(object):
    _tabWidget: QtWidgets.QTabWidget
    _configTool: ConfigTool
    _serverList: list
    _serverSelected: int
    _groupName: str
    _localIP: str
    _autoIP: str
    _n2n: N2N

    def __init__(self, TabWidget):
        # self.trayIcon = None
        self._tabWidget = TabWidget

    def setup(self):
        self._setupUi()
        self._setEventsHandle()
        self._setupConfig()
        self._setupN2N()

    def _setupUi(self):
        self._mainFont = QtGui.QFont()
        self._mainFont.setPointSize(9)
        self._mainFont.setFamily("SimSun")

        self._tabWidget.setObjectName("TabWidget")
        self._tabWidget.setWindowIcon(QtGui.QIcon("icon/icon.png"))
        self._tabWidget.resize(415, 450)
        self._tabWidget.setFixedSize(415, 450)
        self._tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self._tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self._tabWidget.setIconSize(QtCore.QSize(16, 16))
        self._tabWidget.setTabsClosable(False)
        self._tabWidget.setTabBarAutoHide(False)
        print(self._tabWidget.font().family())
        self._tabWidget.setFont(self._mainFont)

        self._setupMainTab()
        self._setupServerTableTab()

        self._retranslateUi(self._tabWidget)
        self._tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self._tabWidget)

    def _setupMainTab(self):
        self._mainTab = QtWidgets.QWidget()
        self._mainTab.setObjectName("mainTab")
        self._serverFrame = QtWidgets.QFrame(self._mainTab)
        self._serverFrame.setGeometry(QtCore.QRect(10, 10, 390, 80))
        self._serverFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._serverFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._serverFrame.setLineWidth(1)
        self._serverFrame.setMidLineWidth(0)
        self._serverFrame.setObjectName("serverFrame")
        self._serverAddressLabel = QtWidgets.QLabel(self._serverFrame)
        self._serverAddressLabel.setGeometry(QtCore.QRect(90, 40, 290, 30))
        _font = QtGui.QFont()
        _font.setPointSize(10)
        self._serverAddressLabel.setFont(_font)
        self._serverAddressLabel.setTextFormat(QtCore.Qt.AutoText)
        self._serverAddressLabel.setObjectName("serverAddressLabel")
        self._serverSelectComboBox = QtWidgets.QComboBox(self._serverFrame)
        self._serverSelectComboBox.setGeometry(QtCore.QRect(90, 10, 200, 20))
        self._serverSelectComboBox.setObjectName("serverSelectComboBox")
        self._serverTitleLabel = QtWidgets.QLabel(self._serverFrame)
        self._serverTitleLabel.setGeometry(QtCore.QRect(10, 10, 70, 30))
        self._serverTitleLabel.setObjectName("serverTitleLabel")
        self._serverTestPushButton = QtWidgets.QPushButton(self._serverFrame)
        self._serverTestPushButton.setGeometry(QtCore.QRect(300, 10, 80, 20))
        self._serverTestPushButton.setObjectName("serverTestPushButton")
        self._groupNameFrame = QtWidgets.QFrame(self._mainTab)
        self._groupNameFrame.setGeometry(QtCore.QRect(10, 100, 390, 50))
        self._groupNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._groupNameFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._groupNameFrame.setObjectName("groupNameFrame")
        self._groupNameTitleLabel = QtWidgets.QLabel(self._groupNameFrame)
        self._groupNameTitleLabel.setGeometry(QtCore.QRect(10, 10, 60, 30))
        self._groupNameTitleLabel.setObjectName("groupNameTitleLabel")
        self._groupNameLineEdit = QtWidgets.QLineEdit(self._groupNameFrame)
        self._groupNameLineEdit.setGeometry(QtCore.QRect(90, 10, 280, 30))
        self._groupNameLineEdit.setObjectName("groupNameLineEdit")
        self._localipFrame = QtWidgets.QFrame(self._mainTab)
        self._localipFrame.setGeometry(QtCore.QRect(10, 160, 390, 50))
        self._localipFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._localipFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._localipFrame.setObjectName("localipFrame")
        self._localipTitleLabel = QtWidgets.QLabel(self._localipFrame)
        self._localipTitleLabel.setGeometry(QtCore.QRect(10, 10, 60, 30))
        self._localipTitleLabel.setObjectName("localipTitleLabel")
        self._localipLineEdit = QtWidgets.QLineEdit(self._localipFrame)
        self._localipLineEdit.setGeometry(QtCore.QRect(90, 10, 150, 30))
        self._localipLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        _font = QtGui.QFont()
        _font.setPointSize(10)
        self._localipLineEdit.setFont(_font)
        self._localipLineEdit.setObjectName("localipLineEdit")
        self._localipAutoCheckBox = QtWidgets.QCheckBox(self._localipFrame)
        self._localipAutoCheckBox.setGeometry(QtCore.QRect(280, 10, 80, 30))
        _font = QtGui.QFont()
        _font.setPointSize(10)
        self._localipAutoCheckBox.setFont(_font)
        self._localipAutoCheckBox.setObjectName("localipAutoCheckBox")
        self._connectionFrame = QtWidgets.QFrame(self._mainTab)
        self._connectionFrame.setGeometry(QtCore.QRect(10, 220, 390, 200))
        self._connectionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._connectionFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._connectionFrame.setObjectName("connectionFrame")
        self._doConnectPushButton = QtWidgets.QPushButton(self._connectionFrame)
        self._doConnectPushButton.setGeometry(QtCore.QRect(310, 160, 75, 30))
        self._doConnectPushButton.setObjectName("doConnectPushButton")
        self._disConnectPushButton = QtWidgets.QPushButton(self._connectionFrame)
        self._disConnectPushButton.setGeometry(QtCore.QRect(225, 160, 75, 30))
        self._disConnectPushButton.setEnabled(False)
        self._disConnectPushButton.setObjectName("disConnectPushButton")
        self._connectionMsgTextBrowser = QtWidgets.QTextBrowser(self._connectionFrame)
        self._connectionMsgTextBrowser.setGeometry(QtCore.QRect(10, 10, 370, 140))
        _font = QtGui.QFont()
        _font.setFamily("Microsoft YaHei")
        _font.setPointSize(9)
        _font.setBold(False)
        _font.setWeight(50)
        self._connectionMsgTextBrowser.setFont(_font)
        self._connectionMsgTextBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self._connectionMsgTextBrowser.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._connectionMsgTextBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self._connectionMsgTextBrowser.setLineWidth(1)
        self._connectionMsgTextBrowser.setObjectName("connectionMsgTextBrowser")
        self._tabWidget.addTab(self._mainTab, "")

    def _setupServerTableTab(self):
        self._serverTableTab = QtWidgets.QWidget()
        self._serverTableTab.setObjectName("serverTableTab")
        self._serverTableFrame = QtWidgets.QFrame(self._serverTableTab)
        self._serverTableFrame.setGeometry(QtCore.QRect(10, 10, 390, 350))
        self._serverTableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._serverTableFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._serverTableFrame.setLineWidth(1)
        self._serverTableFrame.setMidLineWidth(0)
        self._serverTableFrame.setObjectName("serverTableFrame")
        self._serverTableView = QtWidgets.QTableView(self._serverTableFrame)
        self._serverTableView.setObjectName("serverTableView")
        self._serverTableView.horizontalHeader().setStretchLastSection(True)
        self._verticalLayout = QtWidgets.QVBoxLayout(self._serverTableFrame)
        self._verticalLayout.setObjectName("verticalLayout")
        self._verticalLayout.addWidget(self._serverTableView)
        self._serverTableModel = QtGui.QStandardItemModel(0, 2)
        self._serverTableView.setModel(self._serverTableModel)
        self._manageButtonFrame = QtWidgets.QFrame(self._serverTableTab)
        self._manageButtonFrame.setGeometry(QtCore.QRect(10, 370, 390, 50))
        self._manageButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self._manageButtonFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self._manageButtonFrame.setLineWidth(1)
        self._manageButtonFrame.setMidLineWidth(0)
        self._manageButtonFrame.setObjectName("manageButtonFrame")
        self._addServerButton = QtWidgets.QPushButton(self._manageButtonFrame)
        self._addServerButton.setGeometry(QtCore.QRect(10, 10, 75, 30))
        self._addServerButton.setObjectName("addServerButton")
        self._delServerButton = QtWidgets.QPushButton(self._manageButtonFrame)
        self._delServerButton.setGeometry(QtCore.QRect(95, 10, 75, 30))
        self._delServerButton.setObjectName("delServerButton")
        self._delServerButton.setStyleSheet("color:red")
        self._useServerButton = QtWidgets.QPushButton(self._manageButtonFrame)
        self._useServerButton.setGeometry(QtCore.QRect(305, 10, 75, 30))
        self._useServerButton.setObjectName("useServerButton")
        self._tabWidget.addTab(self._serverTableTab, "")

    def _retranslateUi(self, _TabWidget):
        _translate = QtCore.QCoreApplication.translate
        _TabWidget.setWindowTitle(_translate("TabWidget", "N2N"))
        self._serverAddressLabel.setText(_translate("TabWidget", ""))
        self._serverTitleLabel.setText(_translate("TabWidget", "服务器节点"))
        self._serverTestPushButton.setText(_translate("TabWidget", "测试"))
        self._groupNameTitleLabel.setText(_translate("TabWidget", "群组名"))
        self._groupNameLineEdit.setText(_translate("TabWidget", ""))
        self._localipTitleLabel.setText(_translate("TabWidget", "本机地址"))
        self._localipLineEdit.setInputMask(_translate("TabWidget", "000. 000. 000. 000; "))
        self._localipLineEdit.setText(_translate("TabWidget", ". . . "))
        self._localipAutoCheckBox.setText(_translate("TabWidget", "自动分配"))
        self._doConnectPushButton_textSet = ["连接", "连接中", "已连接"]
        self._doConnectPushButton.setText(_translate("TabWidget", self._doConnectPushButton_textSet[0]))
        self._disConnectPushButton.setText(_translate("TabWidget", "断开"))
        _TabWidget.setTabText(_TabWidget.indexOf(self._mainTab), _translate("TabWidget", "主页"))

        self._serverTableModel.setHorizontalHeaderLabels(["节点名", "地址"])
        self._addServerButton.setText(_translate("TabWidget", "添加"))
        self._delServerButton.setText(_translate("TabWidget", "删除"))
        self._delServerMsgBoxInfo = {"title": "删除节点", "text": "确定要删除这个节点吗？"}
        self._useServerButton.setText(_translate("TabWidget", "使用节点"))
        _TabWidget.setTabText(_TabWidget.indexOf(self._serverTableTab), _translate("TabWidget", "节点管理"))

    def _setEventsHandle(self):
        # set main tab elements events handle
        self._serverSelectComboBox.currentIndexChanged.connect(self._handle_serverSelectComboBox_selected)
        self._serverTestPushButton.clicked.connect(self._handle_serverTestPushButton_clicked)
        self._groupNameLineEdit.textChanged.connect(self._handle_groupNameLineEdit_changed)
        self._localipLineEdit.textChanged.connect(self._handle_localipLineEdit_changed)
        self._localipAutoCheckBox.stateChanged.connect(self._handle_localipAutoCheckBox_changed)
        self._doConnectPushButton.clicked.connect(self._handle_doConnectPushButton_clicked)
        self._disConnectPushButton.clicked.connect(self._handle_disConnectPushButton_clicked)

        # set server manage tab elements events handle
        self._serverTableModel.dataChanged.connect(self._handle_serverTableView_changed)
        self._addServerButton.clicked.connect(self._handle_addServerButton_clicked)
        self._delServerButton.clicked.connect(self._handle_delServerButton_clicked)
        self._useServerButton.clicked.connect(self._handle_useServerButton_clicked)

    def _setupConfig(self):
        self._configTool = ConfigTool("settings.json")
        self._serverList = []
        self._serverSelected = -1
        self._groupName = ""
        self._localIP = ""
        self._autoIP = "No"

        rst, jsonobj = self._configTool.readSettings()
        if rst == 0:
            try:
                if jsonobj["servers"] is not None:
                    self._serverList = jsonobj["servers"]
                _profile = jsonobj["profile"]
                _id = _profile["server_id"]
                self._groupName = _profile["group_name"]
                self._localIP = _profile["local_ip"]
                _auto_ip = _profile["auto_ip"]
                if re.match('^[a-zA-Z]+$', _auto_ip):
                    if _auto_ip.lower() == "yes":
                        self._autoIP = "Yes"
                for server_pos in range(len(self._serverList)):
                    server = self._serverList[server_pos]
                    if server["id"] == _id:
                        self._serverSelected = server_pos
                        break
                if self._serverSelected == -1:
                    self._serverSelected = 0
                # self.log_append("[Info] : 读取配置文件成功。")
            except Exception as e:
                self.log_append("[Error] : Failed to read configuration file.", color="red")
                self.log_append(e.__str__(), color="red")
                self._serverList = {}
                self._serverSelected = None
                self._groupName = ""
                self._localIP = ""

        elif rst == 1:
            self.log_append("[Error] : Failed to read configuration file.", color="red")
        elif rst == 2:
            self.log_append("[Error] : Failed to read configuration file.", color="red")

        self._uiFresh()

    def _setupN2N(self):
        self._n2n = N2N(self)
        self._setupN2N_config()
        self._n2n.start()

    def _setupN2N_config(self):
        _server_addr = self._serverList[self._serverSelected]["address"]
        _group_name = self._groupName
        _local_ip = self._localIP.replace(" ","")
        _auto_ip = False
        if self._autoIP == "Yes":
            _auto_ip = True
        self._n2n.setConfig(_server_addr, _group_name, _local_ip, _auto_ip)

    def log_append(self, text: str, color: str = "black", margin_top: str = "0px",
                   margin_bottom: str = "0px"):
        _translate = QtCore.QCoreApplication.translate
        self._connectionMsgTextBrowser.append(_translate("TabWidget",
                                                         f"<p style=\""
                                                         f"margin-top:\'{margin_top}\';"
                                                         f"margin-bottom:\'{margin_bottom}\';"
                                                         f"color:{color};"
                                                         f"\">{text}</p>"))

    def log_clear(self):
        self._connectionMsgTextBrowser.setText("")

    def _save_config(self):
        jsonobj = {}
        server_id = ""
        if len(self._serverList) > 0:
            server_id = self._serverList[self._serverSelected]["id"]
        jsonobj["profile"] = {
            "server_id": server_id,
            "group_name": self._groupName,
            "local_ip": self._localIP,
            "auto_ip": self._autoIP
        }
        jsonobj["servers"] = self._serverList
        self._configTool.saveSettings(jsonobj)

    def _uiFresh(self):

        for i in range(len(self._serverList)):
            _id = self._serverList[i]["id"]
            if _id == str(self._serverSelected):
                self._serverSelected = i
            self._serverList[i]["id"] = str(i)

        server_name_list = []
        server_addr_list = []
        for server in self._serverList:
            server_name_list.append(server["name"])
            server_addr_list.append(server["address"])

        # Clear the server select combobox
        self._serverSelectComboBox.blockSignals(True)
        while self._serverSelectComboBox.count() > 0:
            self._serverSelectComboBox.removeItem(0)

        self._serverSelectComboBox.addItems(server_name_list)
        self._serverSelectComboBox.setCurrentIndex(self._serverSelected)
        self._serverSelectComboBox.blockSignals(False)

        self._serverTableModel.blockSignals(True)
        row_cnt = len(self._serverList)
        self._serverTableModel.setRowCount(row_cnt)
        for i in range(row_cnt):
            index = self._serverTableModel.index(i, 0)
            self._serverTableModel.setData(index, server_name_list[i])
            index = self._serverTableModel.index(i, 1)
            self._serverTableModel.setData(index, server_addr_list[i])

        # self._serverListModel.setStringList(server_name_addr_list)
        self._serverTableModel.blockSignals(False)

        if len(self._serverList) > 0:
            server_address = self._serverList[self._serverSelected]["address"]
        else:
            server_address = ""
        self._serverAddressLabel.setText(server_address)

        self._groupNameLineEdit.setText(self._groupName)

        self._localipLineEdit.setText(self._localIP)
        self._localipAutoCheckBox.blockSignals(True)
        if self._autoIP == "Yes":
            self._localipLineEdit.setEnabled(False)
            self._localipAutoCheckBox.setChecked(True)
        elif self._autoIP == "No":
            self._localipLineEdit.setEnabled(True)
            self._localipAutoCheckBox.setChecked(False)
        self._localipAutoCheckBox.blockSignals(False)

        self._save_config()

    def _handle_serverSelectComboBox_selected(self):
        self._serverSelected = self._serverSelectComboBox.currentIndex()
        self._uiFresh()

    def _handle_serverTestPushButton_clicked(self):
        # self.log_append("")
        pass

    def _handle_groupNameLineEdit_changed(self):
        self._groupName = self._groupNameLineEdit.text()

    def _handle_localipLineEdit_changed(self):
        self._localIP = self._localipLineEdit.text()

    def _handle_localipAutoCheckBox_changed(self):
        if self._autoIP == "Yes":
            self._autoIP = "No"
        elif self._autoIP == "No":
            self._autoIP = "Yes"
        self._localipLineEdit.setReadOnly(not self._localipLineEdit.isReadOnly())
        self._uiFresh()

    def _handle_doConnectPushButton_clicked(self):
        self._uiFresh()
        self._setupN2N_config()
        self._doConnectPushButton.setText(self._doConnectPushButton_textSet[1])
        self._doConnectPushButton.setEnabled(False)
        if self._n2n.tryConnect():
            self._doConnectPushButton.setText(self._doConnectPushButton_textSet[2])
            self._disConnectPushButton.setEnabled(True)
        else:
            self._doConnectPushButton.setText(self._doConnectPushButton_textSet[0])
            self._doConnectPushButton.setEnabled(True)

    def _handle_disConnectPushButton_clicked(self):
        self._n2n.disConnect()
        self._doConnectPushButton.setText(self._doConnectPushButton_textSet[0])
        self._doConnectPushButton.setEnabled(True)
        self._disConnectPushButton.setEnabled(False)



    def _handle_serverTableView_changed(self, index):
        _row = index.row()
        _column = index.column()
        if _column == 0:
            self._serverList[_row]["name"] = self._serverTableModel.data(index)
        elif _column == 1:
            self._serverList[_row]["address"] = self._serverTableModel.data(index)
        self._save_config()

    def _handle_addServerButton_clicked(self):
        _server = {
            "id": str(len(self._serverList)),
            "name": "",
            "address": ""
        }
        self._serverList.append(_server)
        _row = self._serverTableModel.rowCount()
        self._serverTableModel.setRowCount(_row + 1)
        self._save_config()

    def _handle_delServerButton_clicked(self):
        _row = self._serverTableView.currentIndex().row()
        if _row == -1:
            return
        _name = self._serverList[_row]["name"]
        _addr = self._serverList[_row]["address"]
        _title = self._delServerMsgBoxInfo["title"]
        _text = f"{_name}\n{_addr}\n{self._delServerMsgBoxInfo['text']}"
        msg_box = QtWidgets.QMessageBox()
        rst = msg_box.warning(self._tabWidget, _title, _text,
                              QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.Cancel)
        if rst == QtWidgets.QMessageBox.Yes:
            self._serverList.pop(_row)
            self._serverTableModel.removeRow(_row)
            self._uiFresh()

    def _handle_useServerButton_clicked(self):
        _row = self._serverTableView.currentIndex().row()
        if _row == -1:
            return
        self._serverSelected = _row
        self._uiFresh()
        self._tabWidget.setCurrentIndex(0)

    def stop(self):
        self._save_config()
        self._n2n.stop()
