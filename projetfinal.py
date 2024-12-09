from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
from login import password_change_window, userid_change_window
from seance import affich_seance,supprim_seance
from coursgest import cours_gest
from cliengest import client_gest
from profgest import gestion_prof
from inscriptionprincipal import affich_inscription
from sallegest import gestion_salle
from update_groupe import update_groupe
from afficher_tableau import table_window
from ListAbs import list_absence
from PyQt5.QtCore import QEvent
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolButton
login_totale = False
import mysql.connector as sql
from datetime import date
db = sql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
cursor = db.cursor()
cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
from PyQt5.QtCore import QDate,QDateTime
from PyQt5 import *
from PyQt5.QtWidgets import QMenu,QAction,QComboBox,QCheckBox,QMessageBox
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QDialog, QComboBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt,QSize
import sys
from PyQt5.QtGui import QColor,QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QTimer,QUrl
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
#login page:
class Loginpage(QWidget):
    global login_totale
    def __init__(self):
        super().__init__()

        print("Host:" + os.getenv('DB_HOST'))
        self.login_successful = False
        self.setWindowTitle('Login')
        self.resize(365,250)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("icons/password.png"))
        #username:
        self.label1 = QLabel('<font size="8"> UserId </font>',self)
        self.label1.move(28,25)
        self.text1 = MyLineEdit(self)
        self.text1.move(190,35)
        self.text1.resize(130,30)
        self.text1.textChanged.connect(self.text_changed)
        self.text1.setPlaceholderText('Entrer UserId')
        # self.text1.setStyleSheet("background-color: #D3D3D3")



        #password:
        self.label2 = QLabel('<font size="8"> Password </font>',self)
        self.label2.move(10,75)
        self.text2 = MyLineEdit(self)
        self.text2.setPlaceholderText('Entrer Password')
        # self.text2.setStyleSheet("background-color: #D3D3D3")

        self.text2.move(190,90)
        self.text2.resize(130,30)
        self.text2.setEchoMode(QLineEdit.Password)
        self.text2.textChanged.connect(self.text_changed)
        #button:
        self.button = QPushButton('Login',self)
        self.button.move(65,140)
        self.button.resize(220,50)
        self.button.setDisabled(True)

        self.button.clicked.connect(self.login)
        self.text3 = None
        self.text4 = None
        self.eye_btn = QToolButton(self)
        self.eye_btn.setIcon(QIcon('icons/oeil.png'))
        self.eye_btn.move(325, 90)
        self.eye_btn.clicked.connect(self.toggle_password_visibility)
    def toggle_password_visibility(self):
        if self.text2.echoMode() == QLineEdit.Password:
            self.text2.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setIcon(QIcon('icons/cacher.png'))
        else:
            self.text2.setEchoMode(QLineEdit.Password)
            self.eye_btn.setIcon(QIcon('icons/oeil.png')) 
    def text_changed(self):
        if self.text1.text() and self.text2.text():
            self.button.setDisabled(False)
        else:
            self.button.setDisabled(True)
    def closeEvent(self, event):   
            event.accept()
            if self.login_successful == False:
                app.quit()

    def close_app(self):
        self.close()
    def login(self):
        with open("login.txt","r+") as f:
            A = f.readlines()
            if self.text4 != None:
                self.text4.hide()
            if self.text1.text() != A[0].strip() or self.text2.text() != A[1].strip():
                # self.text3.hide()
                self.text4 = QLabel(self)
                self.text4.setText(f"Mot de passe incorrect.")
                self.text4.setStyleSheet("font-size: 20px; font-family: Arial; color: red;")
                self.text4.move(80, 205)
                self.text4.show()
                self.text2.clear()
            else:
                self.text3 = QLabel(self)
                self.text3.setText(f"Welcome")
                self.text3.setStyleSheet("font-size: 25px; font-family: Arial; color: green;")
                self.text3.move(130, 205)
                self.text3.show()
                self.login_successful = True
                QTimer.singleShot(1000, self.close)
                
                
         
#searching clients widget:
class search_client(QWidget):
    def __init__(self):
        super().__init__()
        self.combo = QComboBox(self)
        self.combo.resize(200, 25)
        self.combo.move(100, 50)
        self.combo.addItems(["", "id_client", "nom", "telephone", "email"])
        self.combo.currentTextChanged.connect(self.combo_changed)

        self.label = QLabel("Veuillez entrer votre :", self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet("color: red")
        self.label.move(100, 20)

        self.textbox = QLineEdit(self)
        self.textbox.resize(200, 25)
        self.textbox.move(100, 80)

        self.button = QPushButton("Rechercher", self)
        self.button.resize(100, 25)
        self.button.move(100, 120)
        self.button.clicked.connect(self.button_clicked)

        self.table = QTableWidget(self)
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nom", "Prenom", "Email","Téléphone"])
        self.table.resize(400, 200)
        self.table.move(100, 160)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.button)
        self.vbox.addWidget(self.table)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.vbox)

    def combo_changed(self):
        text = self.combo.currentText()
        self.label.setText(f"Veuillez entrer votre {text}:")
    def button_clicked(self):
        text = self.combo.currentText()
        search_param = self.textbox.text()
        cursor = db.cursor()
        cursor.execute(f"SELECT  * FROM Client WHERE {text} = %s", (search_param,))
        clients = cursor.fetchall()
        self.table.setRowCount(len(clients))
        for i, client in enumerate(clients):
            row = [str(c) for c in client]
            for j, data in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(data))
        self.show()
#edit to pass to the next edit:
class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        super(MyLineEdit, self).keyPressEvent(event)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.focusNextChild()
#La fenetre proncipale:
class main_classe(QMainWindow):
    global win
    def __init__(self):
        super().__init__()
        # self.showMaximized()
        menubar = self.menuBar()
        self.setWindowTitle("Centre De Formations")
        self.setWindowIcon(QIcon("icons/centre.png"))
        button = QPushButton(self)
        button.setIcon(QIcon('button-01.png'))
        button.move(0,460)
        button.setIconSize(QSize(550,1050))  
        button.resize(550, 165)
        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
            }
        """)
        button.raise_()
        button.clicked.connect(table_window)
        button2 = QPushButton(self)
        button2.setIcon(QIcon('button2-01.png'))
        button2.move(1370,460)
        button2.setIconSize(QSize(550,1050))  
        button2.resize(550, 165) 
        button2.setStyleSheet("""
            QPushButton {
                background-color: transparent;
            }
        """)

        button2.clicked.connect(affich_inscription)
        # widget.setStyleSheet("background-image: url(background);")
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("background")))
        self.setPalette(palette)

        #menu bar choises:
        clients = menubar.addMenu("Client")
        prof = menubar.addMenu("Professeur")
        cours = menubar.addMenu("Cours")
        salle = menubar.addMenu('Salle')
        seance = menubar.addMenu('Seance')
        feuille_absence = menubar.addMenu("Feuille D'absence")
        update = menubar.addMenu("Update Groupe")
        settings = menubar.addMenu("Configuration")
        about = menubar.addMenu("About")

        #les sous choixes de menubar:
        client_inscription = QAction(QIcon('icons/icone1.png'),"Gestion des Clients",self)
        proffeseur_inscription = QAction(QIcon('icons/prof.png'),"Gestion des Proffesseurs",self)
        # inscription_new = QAction(QIcon('icons/add-user.png'),"Inscrire Client",self)
        change_password = QAction(QIcon('icons/key.png'),"Changer MDP",self)
        change_userId = QAction(QIcon('icons/user.png'),"Changer UserID",self)
        seance1 = QAction(QIcon('icons/education'),"Ajouter Seance",self)
        seance2 = QAction(QIcon('icons/delete'),"Supprimer Seance",self)
        aboutinfo = QAction(QIcon('icons/info'),"About",self)
        quiter_programme = QAction(QIcon('icons/quit'),"Quiter le Programme",self)
        gestion_cours = QAction(QIcon('icons/cours'),"Gestion des Cours",self)
        salle_gestion = QAction(QIcon('icons/classroom.png'),"Gestion des Salles",self)
        groupe_update = QAction(QIcon("icons/changes.png"),"Update des Groupes",self)
        abs = QAction(QIcon('icons/absence.png'),"Feuille Abscence",self)

        #liason des choix avec les sous choix:
        settings.addAction(change_password)
        settings.addAction(change_userId)
        clients.addAction(client_inscription)
        prof.addAction(proffeseur_inscription)
        seance.addAction(seance1)
        # seance.addAction(seance2)
        salle.addAction(salle_gestion)
        about.addAction(quiter_programme)
        about.addAction(aboutinfo)
        cours.addAction(gestion_cours)
        feuille_absence.addAction(abs)
        # inscription.addAction(inscription_new)
        update.addAction(groupe_update)
        #liaison des sous choix avec leus fonctions:
        seance2.triggered.connect(supprim_seance)
        client_inscription.triggered.connect(client_gest)
        proffeseur_inscription.triggered.connect(gestion_prof)
        seance1.triggered.connect(affich_seance)
        change_password.triggered.connect(password_change_window)
        change_userId.triggered.connect(userid_change_window)
        quiter_programme.triggered.connect(self.fermer_programme)
        gestion_cours.triggered.connect(cours_gest)
        salle_gestion.triggered.connect(gestion_salle)
        # inscription_new.triggered.connect(affich_inscription)
        groupe_update.triggered.connect(update_groupe)
        abs.triggered.connect(list_absence)

        self.move(400,100)
        self.resize(1000,800)
        self.setWindowTitle("Centre De Formations")
    def fermer_programme(self):
        self.close()

new_window_client = None 
window_inscription = None  
window_inscription_prof = None
main_window = None
login = None
main_window2 = None


def page_login():
   global login
   login = Loginpage()
   login.setWindowModality(Qt.ApplicationModal)
   login.show()
def main():
   global main_window2
   main_window2 = main_classe()
   main_window2.showMaximized()
   main_window2.show()

   
app = QtWidgets.QApplication(sys.argv)
main()
page_login()
app.exec_()