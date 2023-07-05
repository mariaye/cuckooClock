# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoteWindow(object):
    def setupUi(self, NoteWindow):
        NoteWindow.setObjectName("NoteWindow")
        NoteWindow.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(NoteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame#frame{\n"
"border:5px solid rgb(113, 85, 51);\n"
"border-radius:20px;\n"
"background-color:rgb(255, 237, 194);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QFrame{\n"
"background-color:rgba(0,0,0,0);\n"
"border:None;\n"
"}")
        self.textEdit.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color:rgb(187, 187, 187);\n"
"    border-bottom-left-radius:15px;\n"
"    border-bottom-right-radius:15px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: None;\n"
"    background-color:rgb(199, 185, 111);\n"
"    border-bottom-left-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(101, 101, 55);\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/imgs/icons/zuidahua.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(51)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("color:rgb(92, 92, 92);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        NoteWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NoteWindow)
        QtCore.QMetaObject.connectSlotsByName(NoteWindow)

    def retranslateUi(self, NoteWindow):
        _translate = QtCore.QCoreApplication.translate
        NoteWindow.setWindowTitle(_translate("NoteWindow", "Notes - Cuckoo Clock"))
        self.label.setText(_translate("NoteWindow", "                 drag here"))
import need.icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoteWindow = QtWidgets.QMainWindow()
    ui = Ui_NoteWindow()
    ui.setupUi(NoteWindow)
    NoteWindow.show()
    sys.exit(app.exec_())