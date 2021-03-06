# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Desktop\test_pyqt\proga\FinadaysTestEmotionColor\design\TextTestWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1101, 656)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setWindowOpacity(1.0)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QMainWindow\n"
"{\n"
"background: url(./res/text.png);\n"
"background-repeat: no-repeat;\n"
"}")
        Form.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        Form.setAnimated(True)
        Form.setDocumentMode(False)
        Form.setTabShape(QtWidgets.QTabWidget.Triangular)
        Form.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 340, 961, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 255, 180);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color : rgb(255, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.uploadFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.uploadFileButton.setGeometry(QtCore.QRect(70, 540, 961, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uploadFileButton.setFont(font)
        self.uploadFileButton.setStyleSheet("QPushButton{\n"
"background-color: rgba(0, 0, 255, 180);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"background-color : rgb(255, 0, 0);\n"
"}")
        self.uploadFileButton.setObjectName("uploadFileButton")
        self.messageText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messageText.setGeometry(QtCore.QRect(70, 160, 961, 161))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.messageText.setFont(font)
        self.messageText.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.messageText.setObjectName("messageText")
        self.answerText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.answerText.setGeometry(QtCore.QRect(70, 410, 961, 111))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.answerText.setFont(font)
        self.answerText.setStyleSheet("background-color: rgba(255, 255, 255, 150);")
        self.answerText.setReadOnly(True)
        self.answerText.setObjectName("answerText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 90, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(70, 130, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(440, 120, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(255,0,0)")
        self.errorLabel.setObjectName("errorLabel")
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "???????????????????????? ???? ??????????????????????"))
        self.pushButton.setText(_translate("Form", "??????????????????"))
        self.uploadFileButton.setText(_translate("Form", "?????????????????? ????????"))
        self.label.setText(_translate("Form", "?????????????? ??????????????????:"))
        self.checkBox.setText(_translate("Form", "?????????????????? ???????????????????? ??????????????????"))
        self.errorLabel.setText(_translate("Form", "?????????????? ?????????? ?? ???????? ????????"))
