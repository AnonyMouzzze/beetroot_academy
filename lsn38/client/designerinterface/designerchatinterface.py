from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(399, 580)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(399, 580))
        MainWindow.setMaximumSize(QtCore.QSize(399, 580))
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #2F4F4F;\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    background-color: #696969;\n"
"    border: 2px solid #7FFFD4;\n"
"    border-radius: 13;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #696969;\n"
"    border: 2px solid #7FFFD4;\n"
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
"QPlainTextEdit { \n"
"    color: white;\n"
"    background-color: #5F9EA0;\n"
"    border: 2px solid #7FFFD4;\n"
"    border-radius: 15;\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.input_message = QtWidgets.QLineEdit(self.centralwidget)
        self.input_message.setEnabled(True)
        self.input_message.setGeometry(QtCore.QRect(10, 530, 331, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_message.sizePolicy().hasHeightForWidth())
        self.input_message.setSizePolicy(sizePolicy)
        self.input_message.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_message.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.input_message.setFont(font)
        self.input_message.setTabletTracking(False)
        self.input_message.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.input_message.setWhatsThis("")
        self.input_message.setStyleSheet("\n"
"\n"
"")
        self.input_message.setText("")
        self.input_message.setMaxLength(32766)
        self.input_message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_message.setObjectName("input_message")
        self.send_message_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_message_button.setGeometry(QtCore.QRect(350, 530, 41, 41))
        self.send_message_button.setStyleSheet("")
        self.send_message_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/send_message_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_message_button.setIcon(icon1)
        self.send_message_button.setIconSize(QtCore.QSize(25, 25))
        self.send_message_button.setObjectName("send_message_button")
        self.show_messages_area = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.show_messages_area.setGeometry(QtCore.QRect(10, 10, 381, 511))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.show_messages_area.setFont(font)
        self.show_messages_area.setStyleSheet("")
        self.show_messages_area.setFrameShape(QtWidgets.QFrame.Panel)
        self.show_messages_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_messages_area.setReadOnly(True)
        self.show_messages_area.setOverwriteMode(False)
        self.show_messages_area.setObjectName("show_messages_area")
        self.send_message_button.raise_()
        self.input_message.raise_()
        self.show_messages_area.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chat"))
        self.input_message.setPlaceholderText(_translate("MainWindow", "Type your message here"))
        self.show_messages_area.setPlainText(_translate("MainWindow", "                               Welcome to chat!"))
