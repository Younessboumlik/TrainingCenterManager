from PyQt5 import *
from PyQt5.QtWidgets import QMenu,QAction,QComboBox,QCheckBox,QMessageBox
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QDialog, QComboBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor,QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QTimer,QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
import mysql.connector as sql
from datetime import date
from PyQt5 import QtCore
db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
cursor = db.cursor()
cursor1 = db.cursor()
cursor2 = db.cursor()

class window_seance(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ajouter Seance")
        self.setWindowIcon(QIcon("icons/education.png"))
        self.resize(700,900)
        self.move(600,30)
        self.setFixedSize(self.size())
        # le texte :
        self.text = QLabel(self)
        self.text.setText("Le jour de la seance:")
        self.text.resize(250,200)
        self.text.move(230,-50)
        self.text.setStyleSheet("font-size: 25px")
        #combobox :
        self.combobox = QComboBox(self)
        self.combobox.move(270,90)
        self.combobox.resize(170,40)
        self.combobox.addItems(["","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"])
        self.combobox.setEditable(True)
        # le texte 1:
        self.text1 = QLabel(self)
        self.text1.setText("L'heure de la seance:")
        self.text1.resize(250,100)
        self.text1.move(230,120)
        self.text1.setStyleSheet("font-size: 25px")
        #combobox 1:
        self.combobox1 = QComboBox(self)
        self.combobox1.move(270,210)
        self.combobox1.resize(170,40)
        self.combobox1.addItems(["","09:00-11:00","15:00-17:00","17:00-19:00","19:00-21:00","21:00-23:00"])
        #using signals to connect combobox 1 and 2 to the function.
        self.combobox1.activated.connect(self.salle_empty)
        self.combobox.activated.connect(self.salle_empty)
        # le texte 2:
        self.text2 = QLabel(self)
        self.text2.setText("La salle de la seance:")
        self.text2.resize(250,100)
        self.text2.move(230,240)
        self.text2.setStyleSheet("font-size: 25px")
        #combobox 2:
        self.combobox2 = QComboBox(self)
        self.combobox2.move(270,320)
        self.combobox2.resize(170,40)        
        # le texte 3:
        self.text3 = QLabel(self)
        self.text3.setText("Le niveau:")
        self.text3.resize(250,80)
        self.text3.move(120,360)
        self.text3.setStyleSheet("font-size: 25px")
        #combobox 3:
        self.combobox3 = QComboBox(self)
        self.combobox3.move(100,430)
        self.combobox3.resize(170,40)
        # le texte 4:
        self.text4 = QLabel(self)
        self.text4.setText("Le libele:")
        self.text4.resize(250,80)
        self.text4.move(400,360)
        self.text4.setStyleSheet("font-size: 25px")
        #combobox 4:
        self.combobox4 = QComboBox(self)
        self.combobox4.move(380,430)
        self.combobox4.resize(170,40)
        #connection des boutons:
        self.niveau()
        self.combobox3.activated.connect(self.libele)
        # le texte 5:
        self.text5 = QLabel(self)
        self.text5.setText("Le groupe:")
        self.text5.resize(250,60)
        self.text5.move(290,465)
        self.text5.setStyleSheet("font-size: 25px")
        #combobox 4:
        self.combobox5 = QComboBox(self)
        self.combobox5.move(258,521)
        self.combobox5.resize(170,40)
        #connection des boutons:
        self.combobox4.activated.connect(self.groupe)
        self.combobox.activated.connect(self.groupe)
        self.combobox1.activated.connect(self.groupe)
        #id prof:
        self.text6 = QLabel(self)
        self.text6.setText("Id Prof:")
        self.text6.setStyleSheet("font-size: 25px;")
        self.text6.move(300,580)
        self.combobox6 = QComboBox(self)
        self.combobox6.move(250,625)
        self.combobox6.resize(170,40)

        #button:
        self.button1 = QPushButton("Ajouter La Seance",self)
        self.button1.setDisabled(True)
        self.button1.move(200,700)
        self.button1.resize(300,70)
        self.button1.clicked.connect(self.ajouter_seance)
        self.combobox.currentTextChanged.connect(self.on_text_changed)
        self.combobox1.currentTextChanged.connect(self.on_text_changed)
        self.combobox2.currentTextChanged.connect(self.on_text_changed)
        self.combobox3.currentTextChanged.connect(self.on_text_changed)
        self.combobox4.currentTextChanged.connect(self.on_text_changed)
        self.combobox5.currentTextChanged.connect(self.on_text_changed)
        self.combobox6.currentTextChanged.connect(self.on_text_changed)
        self.combobox.activated.connect(self.prof)
        self.combobox1.activated.connect(self.prof)
        self.combobox4.currentTextChanged.connect(self.prof)

    #salle empty pour un jour et une heure determiner:
    def salle_empty(self):
        jour_seance = self.combobox.currentText()
        heure_seance = self.combobox1.currentText()
        self.combobox2.clear()
        self.combobox2.addItem("")
        cursor.execute("select nom_salle from salle where id_salle not in (select id_salle from seance where jour_seance = %s and heure_seance = %s);", (jour_seance, heure_seance))
        for salle in cursor.fetchall():
            self.combobox2.addItem(str(salle[0]))
    #affichage des niveau de la base de donnes:
    def niveau(self):
        cursor.execute("select niv_scol from cours group by niv_scol")
        self.combobox3.addItem("")
        for i in cursor.fetchall():
            self.combobox3.addItem(str(i[0]))
    #affichage de matiere:
    def libele(self):
        self.combobox4.clear()
        self.combobox4.addItem("")
        cursor.execute("select libele from cours where niv_scol = %s",(self.combobox3.currentText(),))
        for i in cursor.fetchall():
            self.combobox4.addItem(str(i[0]))
    def groupe(self):

        self.combobox5.clear()
        self.combobox5.addItem("")
        # cursor.execute("select id_groupe from groupe where nbr_clients > min_clients and id_cours in (select id_cours from cours where libele = %s and niv_scol = %s) and id_groupe not in (select id_groupe from seance where jour_seance = %s and heure_seance = %s)",(self.combobox4.currentText(),self.combobox3.currentText(),str(self.combobox.currentText()),str(self.combobox1.currentText())))
        cursor.execute("select id_groupe from groupe where nbr_clients > min_clients and id_cours in (select id_cours from cours where libele = %s and niv_scol = %s) and id_groupe not in (select id_groupe from seance)",(self.combobox4.currentText(),self.combobox3.currentText()))
        for i in cursor.fetchall():
            self.combobox5.addItem(str(i[0]))
    def on_text_changed(self):
        if self.combobox.currentText() and self.combobox1.currentText() and self.combobox2.currentText() and self.combobox3.currentText() and self.combobox4.currentText() and self.combobox5.currentText() and self.combobox6.currentText():
            self.button1.setDisabled(False)
        else:
            self.button1.setDisabled(True)
    def ajouter_seance(self):
        global db
        global cursor
        cursor1 = db.cursor()
        cursor1.execute("select id_salle from salle where nom_salle = %s",(self.combobox2.currentText(),))
        id_salle = cursor1.fetchall()[0][0]
        cursor2 = db.cursor()
        cursor2.execute("select id_cours from cours where libele = %s and niv_scol = %s",(self.combobox4.currentText(),self.combobox3.currentText()))
        id_cours = cursor2.fetchall()[0][0]
        # print(self.combobox5.currentText(),id_salle,id_cours,self.textbox6.text(),self.combobox.currentText(),self.combobox1.currentText())
        cursor.execute("insert into seance(id_groupe,id_salle,id_cours,id_professeur,jour_seance,heure_seance) values(%s,%s,%s,%s,%s,%s);",
                       (int(self.combobox5.currentText()),int(id_salle),int(id_cours),int(self.combobox6.currentText()),
                        str(self.combobox.currentText()),str(self.combobox1.currentText())))
        db.commit()
        # db.close()
        # db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        # cursor = db.cursor()  
        self.text5 = QLabel(self)
        self.text5.setText(f"Le seance a été bien créé.")
        self.text5.setStyleSheet("font-size: 20px; font-family: Arial; color: green;")
        self.text5.move(230, 750)
        self.text5.resize(500,100)
        #ajouter le texte a l ecran:
        self.layout().addWidget(self.text5)
        #clearing comboboxes:
        self.combobox3.clear()
        self.combobox4.clear()
        self.combobox5.clear()
        self.combobox6.clear()
        self.combobox.clear()
        self.combobox.addItems(["","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"])
        self.combobox1.clear()
        self.combobox1.addItems(["","09:00-11:00","15:00-17:00","17:00-19:00","19:00-21:00","21:00-23:00"])
        self.combobox2.clear()

    def prof(self):
        self.combobox6.clear()
        titre = "%" + self.combobox4.currentText() +"%"
        cursor.execute("select id_professeur from professeur where titre like %s and id_professeur not in (select id_professeur from seance where jour_seance = %s and heure_seance = %s)"
                       ,(titre, str(self.combobox.currentText()),str(self.combobox1.currentText())))
        self.combobox6.addItem("")
        for i in cursor.fetchall():
            self.combobox6.addItem(str(i[0]))
class delete_seance(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Supprimer Seance")
            self.setWindowIcon(QIcon("icons/education.png"))
            self.resize(600,500)
            self.move(600,30)
            self.setFixedSize(self.size())
            # le texte 3:
            self.text3 = QLabel(self)
            self.text3.setText("Le niveau:")
            self.text3.resize(250,50)
            self.text3.move(100,30)
            self.text3.setStyleSheet("font-size: 25px")
            #combobox 3:
            self.combobox3 = QComboBox(self)
            self.combobox3.move(80,80)
            self.combobox3.resize(170,40)
            # le texte 4:
            self.text4 = QLabel(self)
            self.text4.setText("Le libele:")
            self.text4.resize(250,30)
            self.text4.move(380,40)
            self.text4.setStyleSheet("font-size: 25px")
            #combobox 4:
            self.combobox4 = QComboBox(self)
            self.combobox4.move(355,80)
            self.combobox4.resize(170,40)
            # le texte 5:
            self.text5 = QLabel(self)
            self.text5.setText("Le groupe:")
            self.text5.resize(250,60)
            self.text5.move(245,135)
            self.text5.setStyleSheet("font-size: 25px")
            #combobox 4:
            self.combobox5 = QComboBox(self)
            self.combobox5.move(228,181)
            self.combobox5.resize(170,40)
            # le texte 1:
            self.text1 = QLabel(self)
            self.text1.setText("L'heure de la seance:")
            self.text1.resize(245,80)
            self.text1.move(350,230)
            self.text1.setStyleSheet("font-size: 25px")
            #combobox 3:
            self.combobox1 = QComboBox(self)
            self.combobox1.move(355,300)
            self.combobox1.resize(170,40)
            self.combobox1.setEnabled(False)
            # le texte 1:
            self.text4 = QLabel(self)
            self.text4.setText("Le jour de la seance:")
            self.text4.resize(250,80)
            self.text4.move(50,230)
            self.text4.setStyleSheet("font-size: 25px")
            #combobox 2:
            self.combobox2 = QComboBox(self)
            self.combobox2.move(80,300)
            self.combobox2.resize(170,40)
            self.combobox2.setEnabled(False)
            
            self.niveau()
            self.combobox3.activated.connect(self.libele)
            self.combobox4.activated.connect(self.groupe)
            # self.combobox.activated.connect(self.groupe)
            self.combobox3.activated.connect(self.groupe)
            self.combobox5.activated.connect(self.heure_jour)
            #button:
            self.button1 = QPushButton("Supprimer La Seance",self)
            self.button1.setDisabled(True)
            self.button1.move(155,360)
            self.button1.resize(300,70)
            self.combobox1.currentTextChanged.connect(self.on_text_changed)
            self.combobox2.currentTextChanged.connect(self.on_text_changed)
            self.combobox3.currentTextChanged.connect(self.on_text_changed)
            self.combobox4.currentTextChanged.connect(self.on_text_changed)
            self.combobox5.currentTextChanged.connect(self.on_text_changed)
            self.button1.clicked.connect(self.supprimer_seance)
        def on_text_changed(self):
            if self.combobox1.currentText() and self.combobox2.currentText() and self.combobox3.currentText() and self.combobox4.currentText() and self.combobox5.currentText():
                self.button1.setDisabled(False)
            else:
                self.button1.setDisabled(True)

        def supprimer_seance(self):
            cursor.execute("delete from seance where id_groupe = %s",(self.combobox5.currentText(),))
            db.commit()
            db.close()
            db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
            cursor = db.cursor()  
            self.combobox1.clear()
            self.combobox2.clear()
            self.combobox3.clear()
            self.combobox4.clear()
            self.combobox5.clear()
            self.niveau()
            self.text5 = QLabel(self)
            self.text5.setText(f"Le seance  du groupe a été bien supprimer.")
            self.text5.setStyleSheet("font-size: 20px; font-family: Arial; color: green;")
            self.text5.move(150, 400)
            self.text5.resize(500,100)
            self.text5.show()

            
            
        def niveau(self):
            cursor.execute("select niv_scol from cours group by niv_scol")
            self.combobox3.addItem("")
            for i in cursor.fetchall():
                self.combobox3.addItem(str(i[0]))
        #affichage de matiere:
        def libele(self):
            self.combobox1.clear()
            self.combobox2.clear()
            self.combobox4.clear()
            self.combobox4.addItem("")
            cursor.execute("select libele from cours where niv_scol = %s",(self.combobox3.currentText(),))
            for i in cursor.fetchall():
                self.combobox4.addItem(str(i[0]))

        def groupe(self):
            self.combobox1.clear()
            self.combobox2.clear()
            self.combobox5.clear()
            self.combobox5.addItem("")
            # cursor.execute("select id_groupe from groupe where nbr_clients > min_clients and id_cours in (select id_cours from cours where libele = %s and niv_scol = %s) and id_groupe not in (select id_groupe from seance where jour_seance = %s and heure_seance = %s)",(self.combobox4.currentText(),self.combobox3.currentText(),str(self.combobox.currentText()),str(self.combobox1.currentText())))
            cursor.execute("select id_groupe from groupe where id_cours in (select id_cours from cours where libele = %s and niv_scol = %s) and id_groupe not in (select id_groupe from seance)",(self.combobox4.currentText(),self.combobox3.currentText()))
            for i in cursor.fetchall():
                self.combobox5.addItem(str(i[0]))
        def heure_jour(self):
            self.combobox1.clear()
            self.combobox2.clear()
            cursor.execute("select jour_seance from seance where id_groupe = %s",(self.combobox5.currentText(),))
            for i in cursor.fetchall():
                self.combobox2.addItem(i[0])
            cursor.execute("select heure_seance from seance where id_groupe = %s",(self.combobox5.currentText(),))
            for i in cursor.fetchall():
                self.combobox1.addItem(i[0])

seance_window = None
drop_seance = None
def affich_seance():
   global seance_window
   seance_window = window_seance()
   seance_window.setWindowModality(QtCore.Qt.ApplicationModal)
   seance_window.show()
def supprim_seance():
   global drop_seance
   drop_seance = delete_seance()
   drop_seance.setWindowModality(QtCore.Qt.ApplicationModal)
   drop_seance.show()

# app = QApplication(sys.argv)
# affich_seance()
# app.exec_()