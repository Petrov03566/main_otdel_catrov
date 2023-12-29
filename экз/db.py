
from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel, QSqlTableModel
from PyQt5.QtCore import Qt


def db_connect():
    db = QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName('Human_Department')
    db.setUserName('postgres')
    db.setPassword('student')
    db.open()

def get_model():
    model = QSqlTableModel()
    model.setTable("user")
    model.select()
    model.setHeaderData(0, Qt.Orientation.Horizontal, "имя")
    model.setHeaderData(1, Qt.Orientation.Horizontal, "фамилия")
    model.setHeaderData(2, Qt.Orientation.Horizontal, "отчество")
    model.setHeaderData(3, Qt.Orientation.Horizontal, "логин")
    model.setHeaderData(4, Qt.Orientation.Horizontal, "пароль")
    model.setHeaderData(5, Qt.Orientation.Horizontal, "должность")

    return model

def addUser(name, sname, tname, login, psw, job):
    queryUser = QSqlQuery()
    queryUser.exec(f"INSERT INTO public.User (name, secondname, thirstname, login, password, job_id) VALUES ('{name}', '{sname}', '{tname}', '{login}', '{psw}',{job}, '1')")