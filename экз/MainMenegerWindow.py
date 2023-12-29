from PyQt5 import QtCore, QtGui, QtWidgets


class WindowMeneger(QtWidgets.QMainWindow):
    def setupUi(self, WindowMeneger):
        WindowMeneger.setObjectName("WindowMeneger")
        WindowMeneger.resize(886, 662)
        self.centralwidget = QtWidgets.QWidget(WindowMeneger)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(0, 201, 871, 421))
        self.tableView_2.setObjectName("tableView_2")
        WindowMeneger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(WindowMeneger)
        self.statusbar.setObjectName("statusbar")
        WindowMeneger.setStatusBar(self.statusbar)

        self.retranslateUi(WindowMeneger)
        QtCore.QMetaObject.connectSlotsByName(WindowMeneger)

    def retranslateUi(self, WindowMeneger):
        _translate = QtCore.QCoreApplication.translate
        WindowMeneger.setWindowTitle(_translate("WindowMeneger", "Менеджер "))
