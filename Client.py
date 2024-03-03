import socket, sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
class login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 472)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 190, 181, 31))
        self.lineEdit.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 220, 121, 51))
        self.pushButton_7.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_7.setText(_translate("Dialog", "Connect"))

class client(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 469)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 180, 191, 71))
        self.pushButton_2.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 180, 181, 71))
        self.pushButton.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 250, 181, 71))
        self.pushButton_3.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 250, 191, 71))
        self.pushButton_4.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 320, 181, 71))
        self.pushButton_5.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 320, 191, 71))
        self.pushButton_6.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 181, 31))
        self.lineEdit.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 90, 121, 51))
        self.pushButton_7.setStyleSheet("font: 12pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(127, 127, 127);\n"
"text-decoration: underline;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 160, 101, 21))
        self.label.setStyleSheet("background-color: none;\n"
"text-decoration: underline;\n"
"font: 12pt \"Impact\";")
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 10, 75, 23))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.pushButton_8.setObjectName("pushButton_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog) 

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "FACEBOOK"))
        self.pushButton.setText(_translate("Dialog", "GOOGLE"))
        self.pushButton_3.setText(_translate("Dialog", "YOUTUBE"))
        self.pushButton_4.setText(_translate("Dialog", "PYCHARM"))
        self.pushButton_5.setText(_translate("Dialog", "INTELLIJ"))
        self.pushButton_6.setText(_translate("Dialog", "CLION"))
        self.pushButton_7.setText(_translate("Dialog", "Rechrche in Google"))
        self.label.setText(_translate("Dialog", "Quick Buttons:"))
        self.pushButton_8.setText(_translate("Dialog", "EXIT"))




def open_brave(socket_server):
    socket_server.send("google".encode())
def open_fb(socket_server):
    socket_server.send("facebook".encode())
def open_yb(socket_server):
    socket_server.send("youtube".encode())
def open_Pycharm(socket_server):
    socket_server.send("PyCharm".encode())
def open_intelliJ(socket_server):
    socket_server.send("intelliJ".encode())
def open_Clion(socket_server):
    socket_server.send("Clion".encode())
def search(socket_server,ui):
    socket_server.send(("search"+ui.lineEdit.text()).encode())
def stop(socket_server):
    socket_server.send("stop".encode())
    exit()
def log(socket_server,ui1,window1):
    server_host = ui1.lineEdit.text()
    name = "wassim"
    socket_server.connect((server_host, sport))
    socket_server.send(name.encode())
    window1.close()


socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080




app=QApplication(sys.argv)

window=QDialog()
ui=client()
ui.setupUi(window)
ui.pushButton.clicked.connect(lambda:open_brave(socket_server))
ui.pushButton_2.clicked.connect(lambda:open_fb(socket_server))
ui.pushButton_3.clicked.connect(lambda:open_yb(socket_server))
ui.pushButton_4.clicked.connect(lambda:open_Pycharm(socket_server))
ui.pushButton_5.clicked.connect(lambda:open_intelliJ(socket_server))
ui.pushButton_6.clicked.connect(lambda:open_Clion(socket_server))
ui.pushButton_7.clicked.connect(lambda :search(socket_server,ui))
ui.pushButton_8.clicked.connect(lambda:stop(socket_server))



window.show()
window1=QDialog()
ui1=login()
ui1.setupUi(window1)
ui1.pushButton_7.clicked.connect(lambda :log(socket_server,ui1,window1))
window1.show()

app.exec_()
