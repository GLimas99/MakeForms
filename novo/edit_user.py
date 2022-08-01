# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 800)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("color:rgb(200, 200, 255);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_popup = QtWidgets.QFrame(self.top_bar)
        self.frame_popup.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_popup.setStyleSheet("background-color: rgb(57, 173, 84);\n"
"border-radius:5px;")
        self.frame_popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_popup.setObjectName("frame_popup")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_popup)
        self.horizontalLayout_3.setContentsMargins(0, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_submit = QtWidgets.QLabel(self.frame_popup)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.lbl_submit.setFont(font)
        self.lbl_submit.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_submit.setObjectName("lbl_submit")
        self.horizontalLayout_3.addWidget(self.lbl_submit)
        self.pushButton = QtWidgets.QPushButton(self.frame_popup)
        self.pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_popup)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_area = QtWidgets.QFrame(self.content)
        self.edit_area.setMaximumSize(QtCore.QSize(450, 800))
        self.edit_area.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"border-radius: 10px")
        self.edit_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_area.setObjectName("edit_area")
        self.logo = QtWidgets.QFrame(self.edit_area)
        self.logo.setGeometry(QtCore.QRect(119, 0, 211, 90))
        self.logo.setStyleSheet("background-image: url(:/Logo_yellow/Images/logorocha_360x90.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.txt_name = QtWidgets.QLineEdit(self.edit_area)
        self.txt_name.setGeometry(QtCore.QRect(85, 90, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_name.setFont(font)
        self.txt_name.setStyleSheet("QLineEdit{\n"
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
        self.txt_name.setMaxLength(32)
        self.txt_name.setObjectName("txt_name")
        self.txt_email = QtWidgets.QLineEdit(self.edit_area)
        self.txt_email.setGeometry(QtCore.QRect(85, 150, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_email.setFont(font)
        self.txt_email.setStyleSheet("QLineEdit{\n"
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
        self.txt_email.setMaxLength(32)
        self.txt_email.setObjectName("txt_email")
        self.txt_oldpass = QtWidgets.QLineEdit(self.edit_area)
        self.txt_oldpass.setGeometry(QtCore.QRect(85, 210, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_oldpass.setFont(font)
        self.txt_oldpass.setStyleSheet("QLineEdit{\n"
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
        self.txt_oldpass.setMaxLength(32)
        self.txt_oldpass.setObjectName("txt_oldpass")
        self.txt_newpass = QtWidgets.QLineEdit(self.edit_area)
        self.txt_newpass.setGeometry(QtCore.QRect(85, 270, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_newpass.setFont(font)
        self.txt_newpass.setStyleSheet("QLineEdit{\n"
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
        self.txt_newpass.setMaxLength(32)
        self.txt_newpass.setObjectName("txt_newpass")
        self.btn_save = QtWidgets.QPushButton(self.edit_area)
        self.btn_save.setGeometry(QtCore.QRect(85, 640, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("QPushButton{\n"
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
        self.btn_save.setObjectName("btn_save")
        self.btn_return = QtWidgets.QPushButton(self.edit_area)
        self.btn_return.setGeometry(QtCore.QRect(30, 20, 41, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(18)
        self.btn_return.setFont(font)
        self.btn_return.setStyleSheet("QPushButton{\n"
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
        self.btn_return.setObjectName("btn_return")
        self.txt_name_2 = QtWidgets.QLineEdit(self.edit_area)
        self.txt_name_2.setGeometry(QtCore.QRect(85, 330, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_name_2.setFont(font)
        self.txt_name_2.setStyleSheet("QLineEdit{\n"
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
        self.txt_name_2.setMaxLength(32)
        self.txt_name_2.setObjectName("txt_name_2")
        self.txt_cpf = QtWidgets.QLineEdit(self.edit_area)
        self.txt_cpf.setGeometry(QtCore.QRect(85, 390, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_cpf.setFont(font)
        self.txt_cpf.setStyleSheet("QLineEdit{\n"
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
        self.txt_cpf.setMaxLength(32)
        self.txt_cpf.setObjectName("txt_cpf")
        self.txt_crea = QtWidgets.QLineEdit(self.edit_area)
        self.txt_crea.setGeometry(QtCore.QRect(85, 570, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_crea.setFont(font)
        self.txt_crea.setStyleSheet("QLineEdit{\n"
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
        self.txt_crea.setMaxLength(32)
        self.txt_crea.setObjectName("txt_crea")
        self.txt_celular = QtWidgets.QLineEdit(self.edit_area)
        self.txt_celular.setGeometry(QtCore.QRect(85, 450, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_celular.setFont(font)
        self.txt_celular.setStyleSheet("QLineEdit{\n"
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
        self.txt_celular.setMaxLength(32)
        self.txt_celular.setObjectName("txt_celular")
        self.txt_smpuge = QtWidgets.QLineEdit(self.edit_area)
        self.txt_smpuge.setGeometry(QtCore.QRect(85, 510, 280, 50))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        self.txt_smpuge.setFont(font)
        self.txt_smpuge.setStyleSheet("QLineEdit{\n"
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
        self.txt_smpuge.setMaxLength(32)
        self.txt_smpuge.setObjectName("txt_smpuge")
        self.horizontalLayout.addWidget(self.edit_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15);")
        self.bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setContentsMargins(0, 0, 6, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_version = QtWidgets.QLabel(self.bottom)
        self.lbl_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.verticalLayout_2.addWidget(self.lbl_version)
        self.label_2 = QtWidgets.QLabel(self.bottom)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit User"))
        self.lbl_submit.setText(_translate("MainWindow", "ENVIADO"))
        self.txt_name.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.txt_email.setPlaceholderText(_translate("MainWindow", "EMAIL"))
        self.txt_oldpass.setPlaceholderText(_translate("MainWindow", "OLD PASSWORD"))
        self.txt_newpass.setPlaceholderText(_translate("MainWindow", "NEW PASSWORD"))
        self.btn_save.setText(_translate("MainWindow", "SAVE"))
        self.btn_return.setText(_translate("MainWindow", "↩"))
        self.txt_name_2.setPlaceholderText(_translate("MainWindow", "NAME"))
        self.txt_cpf.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.txt_crea.setPlaceholderText(_translate("MainWindow", "CREA"))
        self.txt_celular.setPlaceholderText(_translate("MainWindow", "CELULAR"))
        self.txt_smpuge.setPlaceholderText(_translate("MainWindow", "SMPUGE"))
        self.lbl_version.setText(_translate("MainWindow", "V 1.1"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" vertical-align:super;\">Created by Gustavo Lima</span></p></body></html>"))
import file_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
