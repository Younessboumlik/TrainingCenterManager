from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
import mysql.connector as sql
from datetime import date
db = sql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
cursor = db.cursor()
from PyQt5.QtCore import QDate,QDateTime
from PyQt5 import *
from PyQt5.QtWidgets import QMenu,QAction,QComboBox,QCheckBox,QMessageBox
import sys
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget, QDialog, QComboBox, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor,QIcon
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox,QGridLayout,QTextEdit
from functools import partial
id_group_absence = []
option_jour = [ "","lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
list_id_clients = []
list_id_clients_abs = []
list_per_rest_1_seance = []
grp = None
list_per_rest_0_seance = []
cur = db.cursor()
# class fenetre(QMainWindow):
class fenetre(QtWidgets.QWidget):
   global db
   global cursor,cur
   def __init__(self, list_a, list_b):
        super().__init__()

        # Créer deux zones de texte
        # self.text_edit1 = QTextEdit()
        # self.text_edit2 = QTextEdit()
        self.table_frame = QtWidgets.QFrame(self)
        self.table_frame_layout = QtWidgets.QVBoxLayout(self.table_frame)
        self.table_frame.setGeometry(QtCore.QRect(0, 0, 1000, 890))        
        self.table = QTableWidget(self)
        self.table.setStyleSheet("background-color: white;")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setRowCount(0)
        self.table.resize(1200, 1200)
        self.table.move(500, 70)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["          Nom_Client          ","          Prénom_Client          ",
                                              "                    Groupe                    ","1 seance restee" ,"          Nom_Client          ","          Prénom_Client          ",
                                              "                    Groupe                    ","seront supprimes"])
        self.table_frame_layout.addWidget(self.table)
        for i, row in enumerate(list_a):
                nom,prenom, groupe = row
                self.table.setRowCount(i + 1)
                self.table.setItem(i, 0, QTableWidgetItem(str(nom)))
                self.table.setItem(i, 1, QTableWidgetItem(str(prenom)))
                self.table.setItem(i, 2, QTableWidgetItem(str(groupe)))
        for i, row in enumerate(list_b):
                nom,prenom, groupe = row
                self.table.setRowCount(i + 1)
                self.table.setItem(i, 4, QTableWidgetItem(str(nom)))
                self.table.setItem(i, 5, QTableWidgetItem(str(prenom)))
                self.table.setItem(i, 6, QTableWidgetItem(str(groupe)))

        # Ajouter les informations des clients aux zones de texte
        # for info in list_a:
            # self.text_edit1.append(f"Nom : {info[0]}, Prénom : {info[1]}, Groupe : {info[2]}")
        # for info in list_b:
            # self.text_edit2.append(f"Nom : {info[0]}, Prénom : {info[1]}, Groupe : {info[2]}")

        # Créer un layout vertical et y ajouter les zones de texte
        # layout = QVBoxLayout()
        # layout.addWidget(self.text_edit1)
        # layout.addWidget(self.text_edit2)

        # Créer un widget pour contenir le layout
        # widget = QWidget()
        # widget.setLayout(layout)

        # Définir le widget comme le widget central de la fenêtre
        # self.setCentralWidget(widget)
# class feulle_absence(QtWidgets.QWidget):
class feulle_absence(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/absence.png"))

        self.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.setWindowTitle("Feuille d'absence")
        # self.setStyleSheet("background-color: silver")
        self.setStyleSheet("background-color: #D3D3D3")
        self.setFixedSize(self.size())
        self.setWindowTitle("Informations sur les clients")
        #self.setStyleSheet("background-image: url(absen.jpg)")
        self.resize(700,900)
        self.setFixedSize(self.size())
        self.title_frame = QtWidgets.QLabel(self)
        self.title_frame.setText("Feuille d'absence")
        self.title_frame.setStyleSheet("background-color: #1AAECB; color: white; font: 14pt monospace")
        self.title_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.title_frame.setFixedHeight(70)
        layout = QtWidgets.QVBoxLayout(self)
        # Add title_frame to the layout
        layout.addWidget(self.title_frame)
        layout.addStretch(1)
        # Set the layout for the parent widget
        self.setLayout(layout)
        self.manage_frame = QtWidgets.QFrame(self)
        self.manage_frame.setStyleSheet("background-color: white")
        self.manage_frame.setGeometry(QtCore.QRect(20, 90, 400, 600))
        self.man2 = QtWidgets.QFrame(self)
        self.man2.setStyleSheet("background-color: white")
        self.man2.setGeometry(QtCore.QRect(580, 90, 400, 600))
        global cur,option_jour        
        self.list_check=[]
        self.combo_box_jour = QComboBox(self.manage_frame)
        self.combo_box_jour.setEditable(True)
        self.combo_box_jour.insertItems(0,option_jour)
        self.combo_box_jour.move(350,50)
        self.text_jour = QLabel(self.manage_frame,styleSheet='font-weight: bold')
        self.text_jour.setText("choisir le jour ")
        self.text_sem = QLabel(self.manage_frame,styleSheet='font-weight: bold')
        self.text_sem.setText("Entrez le Numéro de la semaine actuelle :")
        self.combo_box_jour.activated.connect(self.on_combobox_choose_date)
        self.combo_box_gr_abs = QComboBox(self.manage_frame)
        self.combo_box_gr_abs.setEditable(True)
        self.combo_box_gr_abs.move(350,110)
        self.text_gr_abs = QLabel(self.manage_frame,styleSheet='font-weight: bold')
        self.text_gr_abs.setText("choisir le groupe ")
        self.text_gr_abs.move(350,80)
        self.combo_box_gr_abs.activated.connect(self.on_show_check_clients)
        self.text_box_semaine = QLineEdit(self.manage_frame)
        self.text_box_semaine.setPlaceholderText("Veulliez entrer le numéro de la semaine")
        self.text_box_semaine.textChanged.connect(self.if_text_chaged)
        self.manage_frame_layout = QtWidgets.QVBoxLayout(self.manage_frame)
        self.manage_frame_layout.addWidget(self.text_sem)
        self.manage_frame_layout.addWidget(self.text_box_semaine)
        self.manage_frame_layout.addWidget(self.text_jour)
        self.manage_frame_layout.addWidget(self.combo_box_jour)
        self.manage_frame_layout.addWidget(self.text_gr_abs)
        self.manage_frame_layout.addWidget(self.combo_box_gr_abs)
        self.man2_layout = QtWidgets.QVBoxLayout(self.man2)
        self.butt_valid_abs = QtWidgets.QPushButton("Valider l'absence",self.man2,styleSheet="background-color: #FFA500; color: black")
        self.butt_valid_abs.move(600,600)
        self.butt_valid_abs.resize(200,60) 
        self.butt_valid_abs.clicked.connect(self.valide_absence)  
         
    def if_text_chaged(self):
       global num_semaine,db,cur,cursor
       num_semaine =  self.text_box_semaine.text()
       
    def on_combobox_choose_date(self):
       
       global cur,id_group_absence,db,cursor
       jour = self.sender().currentText()
       cur.execute("select id_groupe from seance where jour_seance = %s",(jour,))
       id_group_absence = []
       for i in cur :
         id_group_absence += [str(i[0])]
       
       self.combo_box_gr_abs.clear()
       self.combo_box_gr_abs.insertItems(0,id_group_absence)
    def on_show_check_clients(self):
       global list_id_clients,grp,db,cursor,cur
       grp = self.sender().currentText()
       cur.execute("SELECT nom, prenom, id_client FROM client WHERE id_client IN (SELECT id_client FROM appartenir WHERE id_groupe = %s);",(grp,))
       line = 110
       for check in self.list_check:
        self.check_box_client.hide()
       self.list_check = []
       for i in cur :
          list_id_clients +=[str(i[2])]
          self.check_box_client = QCheckBox(f"{i[0]} {i[1]}",self.man2)
          self.man2_layout.addWidget(self.check_box_client)
          
          id = i[2]
          self.check_box_client.stateChanged.connect(partial(self.on_stateChanged,id))
          self.check_box_client.move(50,50+line)
          self.check_box_client.resize(500,500)
        #   self.check_box_client.resize(200,200)
          self.list_check += [self.check_box_client]
          self.check_box_client.show() 
          line+=50
       self.man2_layout.addWidget(self.butt_valid_abs)
        
         
       
      

    def on_stateChanged(self,id):
              global list_id_clients_abs,db,cursor,cur
              list_id_clients_abs += [str(id)]
    def valide_absence(self):
       global  list_id_clients,list_id_clients_abs,cur,grp,list_per_rest_1_seance,list_per_rest_0_seance,db,cursor,cur
       cur.execute("select id_cours from groupe where id_groupe = %s",(grp,))
       id_crs = next(cur)[0]
       cur.execute("select id_seance from seance where id_groupe = %s",(grp,))
       idseance = next(cur)[0]
       for id in list_id_clients :
        
        cur.execute("select nombre_seances,Absences_Tolérées from inscription where id_client= %s and id_cours = %s",(id,id_crs))
        for i in cur :
           info = i
        nbr_sea,abs_tol = info
        if id in list_id_clients_abs:
               if int(abs_tol) == 1:
                cur.execute("update inscription  set Absences_Tolérées = %s where id_client= %s and id_cours = %s",(int(abs_tol)-1,id,id_crs))
                db.commit()
               else :
                  cur.execute("update inscription  set nombre_seances = %s where id_client= %s and id_cours = %s",(int(nbr_sea)-1,id,id_crs)) 
                  db.commit()
                  
               cur.execute("insert into feuille_absence(id_client,id_seance,num_semaine,date_feuille,est_present) values (%s,%s,%s,%s,%s)",(id,idseance,num_semaine,date.today(),0)) 
               db.commit()  
        else :
            cur.execute("update inscription  set nombre_seances = %s where id_client= %s and id_cours = %s",(int(nbr_sea)-1,id,id_crs))
            db.commit()
            cur.execute("insert into feuille_absence(id_client,id_seance,num_semaine,date_feuille,est_present) values (%s,%s,%s,%s,%s)",(id,idseance,num_semaine,date.today(),1))   
            db.commit()
        if (int(nbr_sea)-1 == 1):
                     list_per_rest_1_seance+=[(id,grp)]    
        if (int(nbr_sea)-1 == 0):
                     cur.execute("select id_groupe from appartenir where id_client = %s and id_groupe IN (select id_groupe  from groupe where id_cours = %s)",(id,id_crs))
                     group_cour = list(cur)
                     for elem in group_cour:
                        if str(elem[0]) != grp:
                           list_per_rest_0_seance+=[(id,elem[0])]
                     list_per_rest_0_seance+=[(id,grp)]
       db.commit()
       db.close()
       db = sql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
       cursor = db.cursor()  
       cur = db.cursor()
       for check in self.list_check:
          check.hide()
       self.list_check = []  
       id_group_absence.remove(str(grp))
       grp = None
       list_id_clients = []
       list_id_clients_abs = []
       self.combo_box_gr_abs.clear()
       self.combo_box_gr_abs.insertItems(0,id_group_absence)
       if id_group_absence == []:
          self.collect_drop(list_per_rest_1_seance,list_per_rest_0_seance)
    def collect_drop(self,sean_1_left,sean_0_left):
       
       global fen,db,cur,cursor
       client_name_1 = []
       client_name_0 = []
       for i in sean_1_left:
          cur.execute("select nom,prenom from client where id_client = %s",(i[0],))
          info_1 = next(cur)
          client_name_1 +=[(info_1[0],info_1[1],i[1])]
       for i in sean_0_left:
          cur.execute("select nom,prenom from client where id_client = %s",(i[0],))
          info_0 = next(cur)
          client_name_0 +=[(info_0[0],info_0[1],i[1])]
          cur.execute("delete  from appartenir where id_client = %s and id_groupe = %s;",(i[0],i[1]))
          db.commit()
          cur.execute("select nbr_clients from groupe where id_groupe = %s;",(i[1],))
          nbr_cl = next(cur)[0]
          cur.execute("update groupe set nbr_clients = %s where id_groupe = %s;",(int(nbr_cl)-1,i[1]))
          db.commit()
       db.close()
       db = sql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
       cursor = db.cursor()  
       cur = db .cursor()
       fen = None   
       fen = fenetre(client_name_1,client_name_0)
       fen.show()
win = None
def list_absence():
    global win
   #  app = QtWidgets.QApplication(sys.argv)
    win =feulle_absence()
    win.resize(700,700)
    win.move(350,130)
    # win.move(0,0)
    win.setWindowTitle("Feuille d'absence")
   #  win.setWindowModality(QtCore.Qt.ApplicationModal)
    win.show()
   #  app.exec_()
# list_absence()
