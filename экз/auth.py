
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Avtoriza(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, Avtoriza):
        Avtoriza.setObjectName("Avtoriza")
        Avtoriza.resize(400, 481)
        self.centralwidget = QtWidgets.QWidget(Avtoriza)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_auth = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_auth.setGeometry(QtCore.QRect(170, 330, 111, 41))
        self.pushButton_auth.setObjectName("pushButton_auth")
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(170, 390, 111, 41))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setGeometry(QtCore.QRect(110, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_log.setFont(font)
        self.label_log.setObjectName("label_log")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 180, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 90, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        Avtoriza.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Avtoriza)
        self.statusbar.setObjectName("statusbar")
        Avtoriza.setStatusBar(self.statusbar)

        self.retranslateUi(Avtoriza)
        QtCore.QMetaObject.connectSlotsByName(Avtoriza)

    def retranslateUi(self, Avtoriza):
        _translate = QtCore.QCoreApplication.translate
        Avtoriza.setWindowTitle(_translate("Avtoriza", "Авторизация "))
        self.pushButton_auth.setText(_translate("Avtoriza", "Вход"))
        self.pushButton_exit.setText(_translate("Avtoriza", "Выход"))
        self.label_log.setText(_translate("Avtoriza", "Введите логин "))
        self.label_2.setText(_translate("Avtoriza", "Введите пароль "))

# app = QApplication(sys.argv)
# window = Avtoriza()
# window.setupUi()
# window.show()
# app.exec()
    

