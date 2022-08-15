# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_up.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Pop(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(340, 28))
        MainWindow.setMaximumSize(QtCore.QSize(340, 28))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_popup = QtWidgets.QFrame(self.frame)
        self.frame_popup.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_popup.setStyleSheet("background-color: rgb(57, 173, 84);\n"
"border-radius:5px;")
        self.frame_popup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_popup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_popup.setObjectName("frame_popup")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_popup)
        self.horizontalLayout_5.setContentsMargins(36, 0, 5, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_popup_2 = QtWidgets.QLabel(self.frame_popup)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        self.label_popup_2.setFont(font)
        self.label_popup_2.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_popup_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_popup_2.setObjectName("label_popup_2")
        self.horizontalLayout_5.addWidget(self.label_popup_2)
        self.close_popup_2 = QtWidgets.QPushButton(self.frame_popup)
        self.close_popup_2.setMaximumSize(QtCore.QSize(20, 20))
        self.close_popup_2.setStyleSheet("QPushButton{\n"
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
        self.close_popup_2.setObjectName("close_popup_2")
        self.horizontalLayout_5.addWidget(self.close_popup_2)
        self.horizontalLayout_2.addWidget(self.frame_popup)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_popup_2.setText(_translate("MainWindow", "EDITADO"))
        self.close_popup_2.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Pop()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
