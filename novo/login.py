# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/logo_preto.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color:rgb(200, 200, 255);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.frame_error.setFont(font)
        self.frame_error.setStyleSheet("background-color: rgb(255, 11, 15);\n"
"border-radius:5px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_error = QtWidgets.QLabel(self.frame_error)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lbl_error.setFont(font)
        self.lbl_error.setStyleSheet("")
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.horizontalLayout_3.addWidget(self.lbl_error)
        self.btn_x = QtWidgets.QPushButton(self.frame_error)
        self.btn_x.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_x.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    background-image: url(:/Close_Image/Images/cil-x.png);\n"
"    background-position:center;\n"
"    \n"
"    background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(50, 50, 50);\n"
"    color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(35, 35, 35);\n"
"    color: rgb(255, 255, 127);\n"
"}")
        self.btn_x.setText("")
        self.btn_x.setObjectName("btn_x")
        self.horizontalLayout_3.addWidget(self.btn_x)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius: 10px")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.logo = QtWidgets.QFrame(self.login_area)
        self.logo.setGeometry(QtCore.QRect(119, 0, 211, 90))
        self.logo.setMaximumSize(QtCore.QSize(281, 281))
        self.logo.setStyleSheet("background-image: url(:/Logo_yellow/Images/logorocha_360x90.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(165, 100, 120, 120))
        self.avatar.setStyleSheet("QFrame{\n"
"    background-image: url(:/Avatar/Images/logo-crop.svg);\n"
"    border-radius: 60px;\n"
"    border: 10px solid rgb(255, 207, 0);\n"
"}\n"
"QFrame:hover{\n"
"    border: 10px solid rgb(163, 163, 0);\n"
"}")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.txt_user = QtWidgets.QLineEdit(self.login_area)
        self.txt_user.setGeometry(QtCore.QRect(85, 240, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.txt_user.setMaxLength(32)
        self.txt_user.setObjectName("txt_user")
        self.txt_password = QtWidgets.QLineEdit(self.login_area)
        self.txt_password.setGeometry(QtCore.QRect(85, 300, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_password.setFont(font)
        self.txt_password.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.txt_password.setMaxLength(32)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.cbox_save = QtWidgets.QCheckBox(self.login_area)
        self.cbox_save.setGeometry(QtCore.QRect(85, 370, 281, 22))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.cbox_save.setFont(font)
        self.cbox_save.setStyleSheet("QCheckBox::indicator{\n"
"    border: 3px solid rgb(100, 100, 100);\n"
"    width: 15px;\n"
"    height:15px;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    border: 3px solid rgb(195, 156, 0);\n"
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.cbox_save.setObjectName("cbox_save")
        self.btn_conect = QtWidgets.QPushButton(self.login_area)
        self.btn_conect.setGeometry(QtCore.QRect(90, 420, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.btn_conect.setFont(font)
        self.btn_conect.setStyleSheet("QPushButton{\n"
"    background-color:rgb(50, 50, 50);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.btn_conect.setObjectName("btn_conect")
        self.btn_submit = QtWidgets.QPushButton(self.login_area)
        self.btn_submit.setGeometry(QtCore.QRect(90, 490, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.btn_submit.setFont(font)
        self.btn_submit.setStyleSheet("QPushButton{\n"
"    background-color:rgb(50, 50, 50);\n"
"    border:2px solid rgb(60, 60, 60);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.btn_submit.setObjectName("btn_submit")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setContentsMargins(0, 6, 4, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_version = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_version.setFont(font)
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.verticalLayout_2.addWidget(self.label_version)
        self.label_lima = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(7)
        self.label_lima.setFont(font)
        self.label_lima.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_lima.setObjectName("label_lima")
        self.verticalLayout_2.addWidget(self.label_lima)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RR ENGENHARIA"))
        self.lbl_error.setText(_translate("MainWindow", "ERROR"))
        self.txt_user.setPlaceholderText(_translate("MainWindow", "USER"))
        self.txt_password.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.cbox_save.setText(_translate("MainWindow", "SAVE USER"))
        self.btn_conect.setText(_translate("MainWindow", "CONNECT TO RR ENGENHARIA"))
        self.btn_submit.setText(_translate("MainWindow", " NEW USER"))
        self.label_version.setText(_translate("MainWindow", "V 1.1"))
        self.label_lima.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" vertical-align:super;\">Created by Gustavo Lima</span></p></body></html>"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())