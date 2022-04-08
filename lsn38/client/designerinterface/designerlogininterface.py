from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(345, 393)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(345, 393))
        MainWindow.setMaximumSize(QtCore.QSize(345, 393))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAccessibleDescription("")
        MainWindow.setStyleSheet("background-color: #5F9EA0;\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLineEdit {\n"
"    color: black;\n"
"    background-color: #C0C0C0;\n"
"    border: 2px solid #3CB371;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: black;\n"
"    background-color: #3CB371;\n"
"    border-radius: 20;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7FFFD4;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5F9EA0;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(120, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 30, 401, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.input_ip_address = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip_address.setGeometry(QtCore.QRect(60, 190, 221, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_ip_address.setFont(font)
        self.input_ip_address.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.input_ip_address.setWhatsThis("")
        self.input_ip_address.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_ip_address.setStyleSheet("\n"
"")
        self.input_ip_address.setText("")
        self.input_ip_address.setAlignment(QtCore.Qt.AlignCenter)
        self.input_ip_address.setObjectName("input_ip_address")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 80, 91, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/log_in_icon.png"))
        self.label_2.setObjectName("label_2")
        self.input_nickname = QtWidgets.QLineEdit(self.centralwidget)
        self.input_nickname.setGeometry(QtCore.QRect(60, 250, 221, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_nickname.setFont(font)
        self.input_nickname.setStyleSheet("")
        self.input_nickname.setText("")
        self.input_nickname.setAlignment(QtCore.Qt.AlignCenter)
        self.input_nickname.setObjectName("input_nickname")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Login to chat"))
        self.input_ip_address.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.input_ip_address.setAccessibleDescription(_translate("MainWindow", "Type"))
        self.input_ip_address.setPlaceholderText(_translate("MainWindow", "Type IP address"))
        self.input_nickname.setPlaceholderText(_translate("MainWindow", "Type your name"))
