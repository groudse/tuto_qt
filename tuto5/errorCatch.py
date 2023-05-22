import sys

from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtWidgets import QApplication, QMessageBox, QLabel


con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("/home/contacts.sqlite")


app = QApplication(sys.argv)


if not con.open():
    QMessageBox.critical(
        None,
        "App Name - Error!",
        "Database Error: %s" % con.lastError().databaseText(),
    )
    sys.exit(1)


win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("App Name")
win.resize(200, 100)
win.show()

sys.exit(app.exec_())