from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import mysql.connector as sql
from datetime import date

from PyQt5.QtCore import QDate,QDateTime
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import *
from PyQt5.QtWidgets import QMenu,QAction,QComboBox,QCheckBox,QMessageBox
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QDialog, QComboBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor,QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QTimer,QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
#window showing all tables:
class win_Afftables(QMainWindow):
    global db
    db = sql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
    cursor = db.cursor()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afficher Tableau")
        self.setWindowIcon(QIcon("icons/table.png"))
        self.showMaximized()

        self.combo = QComboBox(self)
        self.combo.resize(200, 25)
        self.combo.move(100, 50)
        self.combo.addItems(["","appartenir", "Client", "Cours",
                             "Feuille_absence", "Groupe","Inscription",
                             "professeur","Salle","Seance","Service"])
        self.combo.currentTextChanged.connect(self.combo_changed)

        self.label = QLabel("Choisissez la table à afficher :", self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet("color: red")
        self.label.move(100, 20)

        # self.textbox = QLineEdit(self)
        # self.textbox.resize(200, 25)
        # self.textbox.move(100, 80)

        self.button = QPushButton("Afficher", self,styleSheet="background-color: #FFA500; color: black")
        self.button.resize(100, 25)
        self.button.move(100, 120)
        self.button.clicked.connect(self.button_clicked)

        self.table = QTableWidget(self)
        # self.table.setRowCount(0)
        # self.table.setColumnCount(5)
        # self.table.setHorizontalHeaderLabels(["ID", "Nom", "Prenom", "Email","Téléphone"])
        # self.table.resize(400, 200)
        # self.table.move(100, 160)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.label)
        # self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.table)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.vbox)

    def combo_changed(self):
        text = self.combo.currentText()
        self.label.setText(f"la table {text}:")
    def button_clicked(self):
        text = self.combo.currentText()
        cursor = db.cursor()
        # cursor.execute(f"SELECT  * FROM {text} ")
        # self.table = QTableWidget(self)
        # self.vbox.addWidget(self.table)
        self.table.setRowCount(0)
        self.table.resize(1300, 1300)
        self.table.move(100, 160)
        # search_param = self.textbox.text()
        if text == 'appartenir':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Client", "ID_Groupe","","","","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Client':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Client", "Nom","Prénom","Email","Telephone","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Cours':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Cours","Libele","Niv_Scol","Prix","ID_Service","Sexe",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Feuille_absence':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["DateFeuille","Est_Présent?","ID_Client","ID_Seance","","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))   
        if text == 'Groupe':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Groupe","NombreClients","Min_Clients","Max_Clients","ID_Cours","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))                                
        if text == 'Inscription':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["NombreSeances","AbsancesTolerees","Est_TEST?",
                                                  "PrixTEST","ID_Client","ID_Seance","DateInscr"])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))                                                            
        if text == 'professeur':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Prof","NOM_Prof","Prenom_Prof","Tel_Prof",
                                                  "Email_Prof","Titre_Prof",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Salle':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Salle","NOM_Salle","Type_Salle","","","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Seance':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Seance","ID_Groupe","ID_Salle",
                                                  "ID_Cours","ID_Prof","Jour","heure"])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))
        if text == 'Service':
            cursor.execute(f"SELECT  * FROM {text} ")
            self.table.setColumnCount(7)
            self.table.setHorizontalHeaderLabels(["ID_Service","Libele_Service","Min_Seances","","","",""])
            cg = cursor.fetchall()
            self.table.setRowCount(len(cg))  # Explicitly set the number of rows
            for i, elm in enumerate(cg):
                row = [str(c) for c in elm]
            # Loop through each data element and set the corresponding cell value
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))                                                                                                                                                                                                                                                                         
        self.show()
main_window = None

def table_window():
   global main_window
   main_window = win_Afftables()
   main_window.setWindowModality(Qt.ApplicationModal)


   main_window.show()