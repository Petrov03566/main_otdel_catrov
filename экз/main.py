import auth
import MainAdminWindow
import MainMenegerWindow
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class Login(auth.Avtoriza):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.pushButton_auth.clicked.connect(self.bnt_open)
        self.label=QLabel(self)
        self.label.move(0 ,0)
        
        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('Human_Department')
        db.setUserName('postgres')
        db.setPassword('student')
        db.open()


    def exet_1(self):
        self.close()
    def auth_2(self):
        self.close()

    def bnt_open(self):
        if self.lineEdit.text() == "admin" and self.lineEdit_2.text() =="1234":
            self.test = Adm()
            self.test.show()
            self.close()
        if  self.lineEdit.text() == "Meneger" and self.lineEdit_2.text() =="4321":
            self.test2 = Men()
            self.test2.show()
            self.close()

class Adm(MainAdminWindow.Ui_WindowAdmin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_dov.clicked.connect(self.add)
        self.pushButton.clicked.connect(self.refresh)
        self.pushButton_delete.clicked.connect(self.delete)
        query = QSqlTableModel()
        sql = "SELECT * FROM public.users"
        query.setTable("users")
        query.select()
        self.tableView.setModel(query)

    def add(self):
        query = QSqlQuery()
        query.exec(f"INSERT INTO public.users (name, secondname, thistname) VALUES ('{self.lineEdit.text()}', '{self.lineEdit_2.text()}','{self.lineEdit_3.text()}')")

    def refresh(self):
        query1 = QSqlTableModel()
        sql = "SELECT * FROM public.users"
        query1.setTable("users")
        query1.select()
        self.tableView.setModel(query1)

    def delete(self):
        query2 = QSqlTableModel()
        sql = "SELECT * FROM public.users"
        query2.setTable("users")
        selected = self.tableView.selectedIndexes()
        query2.select()
        self.tableView.setModel(query2)

        rows = set(index.row() for index in selected)
        rows = list(rows)
        rows.sort()
        if selected:
            first = rows[0]
            query2.removeRow(first)
            query2.select()
    

class Men(MainMenegerWindow.WindowMeneger):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        query = QSqlTableModel()
        sql = "SELECT * FROM public.users"
        query.setTable("users")
        query.select()
        self.tableView_2.setModel(query)
        


app =QApplication(sys.argv)
window =Login()
window.show()
app.exec()
     