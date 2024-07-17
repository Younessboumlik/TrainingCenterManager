from PyQt5.QtCore import QDate,QDateTime
from PyQt5 import QtCore
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
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import mysql.connector as sql
from datetime import date
niv = None
libele = None
service = None
id_group = None
de_test = 0
nbr_seance = 1
id_client = None
done = False
groups_wanted = []
groups_wanted_n_active = []
groupes_selected = []
db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
cursor = db.cursor()

class new_win(QtWidgets.QWidget):
   def __init__(self):
    super().__init__()
    self.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
    self.setFixedSize(self.size())
    self.setWindowTitle("Inscription")
    self.setWindowIcon(QIcon("icons/inscrire.png"))
    
    
    self.manage_frame = QtWidgets.QFrame(self)
    self.manage_frame.setStyleSheet("background-color: white")
    self.manage_frame.setGeometry(QtCore.QRect(10, 0, 400, 800))
    self.manage_frame2 = QtWidgets.QFrame(self)
    self.manage_frame2.setStyleSheet("background-color: white")
    self.manage_frame2.setGeometry(QtCore.QRect(600, 50, 1200, 900))
    self.manage_frame3 = QtWidgets.QFrame(self)
    self.manage_frame3.setStyleSheet("background-color: white")
    self.manage_frame3.setGeometry(QtCore.QRect(10, 800, 400, 200))
    
    
    self.option_matiere = None
    
   #  self.resize(1100,1000)
   #  self.move(340,20)
   #  self.setFixedSize(self.size())
    #search client part
    
    self.combo_box1 = QComboBox(self.manage_frame)
    

    self.label = QLabel("  Veuillez entrer :", self.manage_frame2)
    self.label.setFont(QtGui.QFont("Sanserif", 12))
    self.label11 = QLabel("  Entrez l'identifiant :", self.manage_frame)
    self.label11.setFont(QtGui.QFont("Sanserif", 12))
    self.label.setStyleSheet("color: red")
    self.label.move(50, 20)
    self.label.resize(300,40)
    #service label:
    self.label1 = QLabel("Choisir un service :", self.manage_frame)
    self.label1.setFont(QtGui.QFont("Sanserif", 10))
    self.label1.setStyleSheet("color: red")
    self.label1.move(20, 130)
    self.label1.resize(300,40)
    #niveau label:
    self.label2 = QLabel("Choisir un niveau :", self.manage_frame)
    self.label2.setFont(QtGui.QFont("Sanserif", 10))
    self.label2.setStyleSheet("color: red")
    self.label2.move(20, 310)
    self.label2.resize(300,40)
    #libele label:
    self.label3 = QLabel("Choisir une matière :", self.manage_frame)
    self.label3.setFont(QtGui.QFont("Sanserif", 10))
    self.label3.setStyleSheet("color: red")
   #  self.label3.move(20, 400)
   #  self.label3.resize(300,40)
    #libele label:
    self.label4 = QLabel("Choisir un groupe :", self.manage_frame)
    self.label4.setFont(QtGui.QFont("Sanserif", 10))
    self.label4.setStyleSheet("color: red")
   #  self.label4.move(20, 500)
   #  self.label4.resize(300,40)
    #libele label:
    self.label5 = QLabel("Nombre de séances :", self.manage_frame)
    self.label5.setFont(QtGui.QFont("Sanserif", 12))
    self.label5.setStyleSheet("color: red")
    self.label6 = QLabel("Groupe supplémentaire :", self.manage_frame)
    self.label6.setFont(QtGui.QFont("Sanserif", 12))
    self.label6.setStyleSheet("color: red")
   #  self.label5.move(270, 400)
   #  self.label5.resize(300,40)
    self.checkBox4 = QCheckBox('Séance de Test ', self.manage_frame)
   #  self.checkBox4.setGeometry(500, 420, 400, 300)
    self.checkBox4.stateChanged.connect(self.check_checked_box)
    # check boxes for service
    self.checkBox1 = QCheckBox('Soutien scolaire', self.manage_frame)
    self.checkBox1.stateChanged.connect(self.submit_choice_check)
    self.checkBox2 = QCheckBox('Langues', self.manage_frame)
    self.checkBox2.stateChanged.connect(self.submit_choice_check)
    self.checkBox3 = QCheckBox('Soft skils', self.manage_frame)
    self.checkBox3.stateChanged.connect(self.submit_choice_check)
   #  self.checkBox1.setGeometry(50, 180, 150, 18)
   #  self.checkBox2.setGeometry(50, 230, 150, 18)
   #  self.checkBox3.setGeometry(50, 280, 150, 18)
    self.textbox_id_clt = QLineEdit(self.manage_frame)
    self.textbox_id_clt.setPlaceholderText("Veulliez entrer l'identifiant")
    
    self.combo_box = QComboBox(self.manage_frame)
    self.combo_box2 = QComboBox(self.manage_frame)
    self.textbox4 = QLineEdit(self.manage_frame)
    self.textbox4.setPlaceholderText("Veulliez entrer le nombre de séances")
    
    self.textbox4.resize(300,50)
    self.textbox4.move(200,500)
    
    self.textbox4.textChanged.connect(self.submit_nbr_seance)
    
    self.combo = QComboBox(self.manage_frame2)
    self.combo.resize(50, 85)
   #  self.combo.move(600, 50)
    self.combo.addItems(["", "id_client", "nom", "telephone", "email"])
    self.combo.currentTextChanged.connect(self.combo_changed)    
    self.button = QPushButton(self.manage_frame2, text="Rechercher",styleSheet="background-color: #FFA500; color: black")
    self.button.resize(100, 25)
    self.button.move(600, 120)
    self.button.clicked.connect(self.button_clicked)
    self.exit_btn=QtWidgets.QPushButton(self.manage_frame3, text="Quitter:",styleSheet="background-color: #FF0000; color: white")
    self.table = QTableWidget(self.manage_frame2)
    self.table.setRowCount(0)
    self.table.setColumnCount(5)
    self.table.setHorizontalHeaderLabels(["          ID          ", 
                                          "          Nom          ", 
                                          "          Prenom          ",
                                          "                    Email                    ",
                                          "          Téléphone          "])
   #  self.table.resize(800, 200)
    self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
   
   #  self.table.move(300, 160)
    self.textbox = QLineEdit(self.manage_frame2)
    self.textbox.setPlaceholderText("Veulliez entrer l'élément choisi pour la recherche")
    
    self.textbox.resize(20, 25)
    self.textbox.move(600, 80)
   #  self.text_clt = QtWidgets.QLabel(self.manage_frame2)
    self.textbox_id_clt.resize(300,50)
    self.textbox_id_clt.move(50,75)
    self.textbox_id_clt.textChanged.connect(self.verif_id_client)
    self.btn_update_inscription = QtWidgets.QPushButton(self.manage_frame3,text="Update inscription",styleSheet="background-color: #008000; color: white")
    self.exit_btn.clicked.connect(self.close)
    self.btn_update_inscription .move(800,620)
    self.btn_update_inscription.resize(230,80) 
    self.btn_update_inscription.setDisabled(True)
    self.btn_update_inscription.clicked.connect(self.update_inscri_clicked)
    #boutton inscription 
    
    self.btn_inscription = QtWidgets.QPushButton(self.manage_frame3, text="Inscription", styleSheet="background-color: #0000FF; color: white")
    self.btn_inscription .move(600,620)
    self.btn_inscription .resize(300,80)
    self.btn_inscription.setDisabled(True)
    self.btn_inscription.clicked.connect(self.inscription_clicked)
    self.btn_inscription .show() 
    self.combo_box_gr = QComboBox(self.manage_frame)
    self.combo_box_gr.setEditable(True)
    self.combo_box_gr.activated.connect(self.on_combobox_select_groups)
    self.combo_box_gr.move(600,760)
    self.combo_box2.resize(200,30)
    
   #  self.vbox = QVBoxLayout()
   #  self.vbox.addWidget(self.combo)
   #  self.vbox.addWidget(self.label)
   #  self.vbox.addWidget(self.textbox)
   #  self.vbox.addWidget(self.button)
   #  self.vbox.addWidget(self.table)
    
        
    
    
    


    self.manage_frame_layout = QtWidgets.QVBoxLayout(self.manage_frame)
   #  self.manage_frame_layout.addWidget(self.combo)
   #  self.manage_frame_layout.addWidget(self.label)
    
    self.manage_frame_layout.addWidget(self.label11)
    self.manage_frame_layout.addWidget(self.textbox_id_clt)
    self.manage_frame_layout.addWidget(self.label1)
    
    
    self.manage_frame_layout.addWidget(self.checkBox1)
    self.manage_frame_layout.addWidget(self.checkBox2)
    self.manage_frame_layout.addWidget(self.checkBox3)
    self.manage_frame_layout.addWidget(self.label2)
    self.manage_frame_layout.addWidget(self.combo_box)
    
    self.manage_frame_layout.addWidget(self.label3)
    self.manage_frame_layout.addWidget(self.combo_box1)
    
    self.manage_frame_layout.addWidget(self.label4)
    self.manage_frame_layout.addWidget(self.combo_box2)
    
    
    self.manage_frame_layout.addWidget(self.checkBox4)
    self.manage_frame_layout.addWidget(self.label5)
    self.manage_frame_layout.addWidget(self.textbox4)
    self.manage_frame_layout.addWidget(self.label6)
    self.manage_frame_layout.addWidget(self.combo_box_gr)
    
    
    
    self.manage_frame_layout.setSpacing(5) # Espacement de 10 pixels entre les boutons
    self.man2= QtWidgets.QVBoxLayout(self.manage_frame2)
    self.man2.addWidget(self.combo)
    self.man2.addWidget(self.label)
   #  self.man2.addWidget(self.text_clt)
    
    self.man2.addWidget(self.textbox)
    self.man2.addWidget(self.button)
    self.man2.addWidget(self.table)
    self.man2.setSpacing(50) # Espacement de 10 pixels entre les boutons
    
    
    

    self.man3= QtWidgets.QVBoxLayout(self.manage_frame3)
    self.man3.addWidget(self.btn_inscription)
    self.man3.addWidget(self.btn_update_inscription)
    self.man3.addWidget(self.exit_btn)
    
    spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    self.man2.addItem(spacer)


    







   #  self.central_widget = QWidget()
    # self.setCentralWidget(self.central_widget)
    # self.central_widget.setLayout(self.vbox)
    #text box id client 

    #nombre de seance 

    #buton update inscription 

    #self.setStyleSheet("background-image: url(preview.jpg)")
    #check box for test seance 

    #combo boxes
    self.combo_box.setEditable(True)
    # self.combo_box.addItems(self.option_niv)
    self.combo_box.activated.connect(self.on_combobox_change)
    self.combo_box.move(20,370)
    self.combo_box.resize(200,30)
    self.combo_box1.setEditable(True)
    self.combo_box1.activated.connect(self.on_combobox_change_libele)
    self.combo_box1.move(20,460)
    self.combo_box1.resize(200,30)
    self.combo_box2.setEditable(True)
    self.combo_box2.move(20,560)
    self.combo_box2.resize(200,30)
    self.combo_box2.activated.connect(self.choosen_id_groups)
    #combo box for groups wanted
   def close(self):
        self.destroy()

   def on_combobox_select_groups(self):
      global cursor,db
      chosed =self.sender().currentText()
      groupes_selected.append(chosed)
      if chosed in groups_wanted:
       groups_wanted.remove(chosed)
      else :
          groups_wanted_n_active.remove(chosed)
      self.combo_box_gr.clear()
      self.combo_box_gr.insertItems(0,groups_wanted)
      color_1 = QColor("green")
      for i in range(len(groups_wanted)):
       self.combo_box_gr.setItemData(i, color_1, Qt.BackgroundRole)
      for i in range(len(groups_wanted)):
       self.combo_box_gr.setItemData(i, "avtivee", Qt.ToolTipRole) 
      self.combo_box_gr.addItems(groups_wanted_n_active)
      color_2 = QColor("red")
      for i in range(len(groups_wanted),len(groups_wanted_n_active)+len(groups_wanted_n_active)):
       self.combo_box_gr.setItemData(i, color_2, Qt.BackgroundRole)
      for i in range(len(groups_wanted),len(groups_wanted_n_active)+len(groups_wanted_n_active)):
       self.combo_box_gr.setItemData(i, "non avtivee", Qt.ToolTipRole)

   def update_inscri_clicked(self):
      global db,nbr_seance
      cur = db.cursor()
      cur.execute("select id_cours from groupe where id_groupe = %s",(id_group,))
      id_cours = next(cur)[0]
      cur.execute("select nombre_seances from inscription where id_client = %s and id_cours = %s",(id_client,id_cours))
      nbr_scie_exist = next(cur)[0]
      nbr_seance = int(nbr_seance) + int(nbr_scie_exist)
      current_date=date.today()
      info = (nbr_seance,1,current_date,de_test,id_client,id_cours)
      
      db.cursor().execute("insert into appartenir(id_client,id_groupe) values(%s,%s)",(id_client,id_group))
      cur.execute("select nbr_clients from groupe where id_groupe = %s",(id_group,))
      nbr_clients = next(cur)[0]
      db.cursor().execute("update groupe set nbr_clients = %s where id_groupe = %s",(int(nbr_clients+1),id_group))
      db.cursor().execute("UPDATE inscription set nombre_seances = %s,Absences_Tolérées=%s,Date_inscription = %s, de_test = %s where id_client = %s and id_cours= %s",info)
      for i in groupes_selected:
       cur.execute("select nbr_clients from groupe where id_groupe = %s",(i,))
       nbr_clients = next(cur)[0]
       db.cursor().execute("update groupe set nbr_clients = %s where id_groupe = %s",(int(nbr_clients+1),i))
       db.cursor().execute("insert into appartenir(id_client,id_groupe) values(%s,%s)",(id_client,i))
      db.commit()
      cursor.execute("FLUSH TABLES users;")
      db.close()
      db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
      cursor = db.cursor() 
      mssg = QMessageBox()
      mssg.setIcon(QMessageBox.Information)
      stri =str(id_group)
      for i in groupes_selected:
         stri += "," + str(i)
      mssg.setText("l'inscription est ressite et voila votre groupes :" + stri)
      mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      mssg.exec_()
      db.commit()
      cursor.execute("FLUSH TABLES users;")
      db.close()
      db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
      cursor = db.cursor() 
      
   def inscription_clicked(self):
      global db,cursor
      cur = db.cursor()
      cur.execute("select id_cours from groupe where id_groupe = %s",(id_group,))
      id_cours = next(cur)[0]
      current_date=date.today()
      info = (nbr_seance,1,de_test,200,id_client,id_cours,current_date)
      
      db.cursor().execute("insert into inscription(nombre_seances,Absences_Tolérées,de_test,Prix_test,id_client,id_cours,Date_inscription) values(%s,%s,%s,%s,%s,%s,%s)",info)
      db.cursor().execute("insert into appartenir(id_client,id_groupe) values(%s,%s)",(id_client,id_group))
      cur.execute("select nbr_clients from groupe where id_groupe = %s",(id_group,))
      nbr_clients = next(cur)[0]
      db.cursor().execute("update groupe set nbr_clients = %s where id_groupe = %s",(int(nbr_clients+1),id_group))
      for i in groupes_selected:
       cur.execute("select nbr_clients from groupe where id_groupe = %s",(i,))
       nbr_clients = next(cur)[0]
       db.cursor().execute("update groupe set nbr_clients = %s where id_groupe = %s",(int(nbr_clients+1),i))
       db.cursor().execute("insert into appartenir(id_client,id_groupe) values(%s,%s)",(id_client,i))
      db.commit()
      cursor.execute("FLUSH TABLES users;")
      db.close()
      db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
      cursor = db.cursor()  
      mssg = QMessageBox()
      mssg.setIcon(QMessageBox.Information)
      stri =str(id_group)
      for i in groupes_selected:
         stri += "," + str(i)
      mssg.setText("l'inscription est ressite et voila votre groupes :" + stri)
      mssg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
      mssg.exec_()
   def combo_changed(self):
        global cursor,db
        text = self.combo.currentText()
        self.label.setText(f"Veuillez entrer votre {text}:")
   def button_clicked(self):
        global cursor,db
        text = self.combo.currentText()
        search_param = self.textbox.text()
        cursor = db.cursor()
        cursor.execute(f"SELECT  * FROM Client WHERE {text} = %s", (search_param,))
        clients = cursor.fetchall()
        self.table.setRowCount(len(clients))  # Explicitly set the number of rows
        for i, client in enumerate(clients):
            row = [str(c) for c in client]
        # Loop through each data element and set the corresponding cell value
            for j, data in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(data))
        self.table.resizeColumnsToContents() 
            
        self.show() 
   def verif_id_client(self):
      
      global id_client,cursor,db
      try :
       id_client = int (self.textbox_id_clt.text())
       if done and service != None and libele!= None and id_group!= None and niv != None:
          self.btn_inscription.setDisabled(False)
          self.btn_update_inscription.setDisabled(False)
      except Exception : 
        id_client = None
        self.btn_inscription.setDisabled(True)
        self.btn_update_inscription.setDisabled(True)
   def check_checked_box(self):
     global de_test,done,cursor,db
     
     if self.checkBox4.isChecked():
      done = True
      self.textbox4.setDisabled(True)
      de_test = 1
      if  service != None and libele!= None and id_group!= None and niv != None and id_client != None:
       
       self.btn_inscription.setDisabled(False)
     else:
         de_test = 0
         done = False
         self.textbox4.setDisabled(False) 
         self.btn_inscription.setDisabled(True)
   def choosen_id_groups(self):
      global id_group,cursor,db
      id_group = self.sender().currentText()
      self.combo_box_gr.clear()
      
      if id_group in groups_wanted:
       groups_wanted.remove(id_group)
      else :
          groups_wanted_n_active.remove(id_group)
      
      self.combo_box_gr.insertItems(0,groups_wanted)
      color_1 = QColor("green")
      for i in range(len(groups_wanted)):
       self.combo_box_gr.setItemData(i, color_1, Qt.BackgroundRole)
      for i in range(len(groups_wanted)):
       self.combo_box_gr.setItemData(i, "avtivee", Qt.ToolTipRole) 
      self.combo_box_gr.addItems(groups_wanted_n_active)
      color_2 = QColor("red")
      for i in range(len(groups_wanted),len(groups_wanted_n_active)+len(groups_wanted_n_active)):
       self.combo_box_gr.setItemData(i, color_2, Qt.BackgroundRole)
      for i in range(len(groups_wanted),len(groups_wanted_n_active)+len(groups_wanted_n_active)):
       self.combo_box_gr.setItemData(i, "non avtivee", Qt.ToolTipRole)

      
   def submit_nbr_seance(self):
      global niv,id_group,libele,service,de_test,nbr_seance,id_client,done,cursor,db
      curs = db.cursor()
      curs.execute("select min_seances from service where libele_service = %s ",(service,)) 
      nbr_seance= self.textbox4.text()
      min_seance = next(curs)[0]
      try :
       if nbr_seance != '':
        if int(nbr_seance) >= int(min_seance):
           done = True
        else :
              done = False
        if done and service != None and libele!= None and id_group!= None and niv != None and id_client != None:
        
         self.btn_inscription.setDisabled(False)
         self.btn_update_inscription.setDisabled(False)
        else:
           self.btn_inscription.setDisabled(True)
           self.btn_update_inscription.setDisabled(True)
       else :
           nbr_seance = 1
           self.btn_inscription.setDisabled(True)
           self.btn_update_inscription.setDisabled(True)
      except Exception:
              pass

   def submit_choice_check(self):
     global service,db,cursor
     if self.checkBox1.isChecked():
        service = "soutien_scolaire"
        self.checkBox2.setDisabled(True)
        self.checkBox3.setDisabled(True)
        self.checkBox1.setDisabled(False)
     elif self.checkBox2.isChecked():
        self.checkBox1.setDisabled(True)
        self.checkBox3.setDisabled(True)
        self.checkBox2.setDisabled(False)
        service = "langues"  
     elif self.checkBox3.isChecked():
        self.checkBox1.setDisabled(True)
        self.checkBox2.setDisabled(True)
        self.checkBox3.setDisabled(False)
        service = "soft_skills"
     if not self.checkBox1.isChecked() and not self.checkBox2.isChecked() and not self.checkBox3.isChecked():
        self.checkBox1.setDisabled(False)
        self.checkBox2.setDisabled(False)
        self.checkBox3.setDisabled(False)

     self.option_niv = self.execute_query(service)
     self.combo_box.clear()
     self.combo_box.insertItems(0,self.option_niv)
     

   def on_combobox_change(self):
     global db,cursor
     option = [""]
     global cursor
     global niv
     niv = self.sender().currentText()
     cursor2 = db.cursor()
     cursor2.execute("select libele from cours where niv_scol = %s; ",(str(niv),))
     for i in cursor2 :

      option += [i[0]]
     self.combo_box1.clear()
     self.combo_box1.addItems(option)
   def on_combobox_change_libele(self):
    global cursor,db
    
    option = ['']
    option_n_activ = ['']
    global db
    global libele
    global niv,groups_wanted,groups_wanted_n_active
    libele = self.sender().currentText()
    if libele != '':
     cursor3 = db.cursor()
     
     #cursor3.execute("select id_groupe from groupe where id_cours = (select id_cours from cours where libele = %s and niv_scol = %s) and nbr_clients < max_clients;)",(str(niv),str(libele)))
     cursor3.execute("SELECT id_groupe FROM groupe WHERE id_cours = (SELECT id_cours FROM cours WHERE libele = %s AND niv_scol = %s) AND nbr_clients < max_clients and nbr_clients >= min_clients ;", (str(libele), str(niv)))
     
     for i in cursor3 :
      option += [str(i[0])]
     cursor3.execute("SELECT id_groupe FROM groupe WHERE id_cours = (SELECT id_cours FROM cours WHERE libele = %s AND niv_scol = %s) and  nbr_clients < min_clients ;", (str(libele), str(niv)))
     for i in cursor3 :
      option_n_activ += [str(i[0])]
     if option == [''] and option_n_activ ==['']:
       self.btn = QtWidgets.QPushButton("add group",self)
       self.btn.move(260,500)
       self.btn.resize(100,100)
       self.btn.setStyleSheet("background-color:green ;border :2px solid black; border-radius :50px;")
       self.btn.clicked.connect(self.add_group)
       self.btn.show()
     else :   
      self.combo_box2.clear() 
      groups_wanted = option
      groups_wanted_n_active = option_n_activ
      self.combo_box2.insertItems(0,option)
      color_1 = QColor("green")
      for i in range(len(option)):
       self.combo_box2.setItemData(i, color_1, Qt.BackgroundRole)
      for i in range(len(option)):
       self.combo_box2.setItemData(i, "avtivee", Qt.ToolTipRole) 
      self.combo_box2.addItems(option_n_activ)
      color_2 = QColor("red")
      for i in range(len(option),len(option)+len(option_n_activ)):
       self.combo_box2.setItemData(i, color_2, Qt.BackgroundRole)
      for i in range(len(option),len(option)+len(option_n_activ)):
       self.combo_box2.setItemData(i, "non avtivee", Qt.ToolTipRole)
   def execute_query(self,service):
     option = [""]
     global cursor
     cursor.execute("select niv_scol from cours where id_service = (select id_service from service where libele_service = %s) group by niv_scol;",(service,))
     for i in cursor :

      option += [i[0]]
     
     return option  
   def add_group(self):
     global niv,libele,groups_wanted_n_active,id_group
     global db,cursor
     a = db.cursor()
     a.execute("SELECT id_cours FROM cours WHERE libele = %s AND niv_scol = %s",(str(libele),str(niv)))
     id_cours = next(a)[0]
     db.cursor().execute("insert into groupe (nbr_clients,id_cours) values (%s ,%s)",(0,int(id_cours)))
     a= db.cursor()
     a.execute("select id_groupe from groupe where id_cours = %s",(int(id_cours),))
     for i in a:
      id_group = i[0]
     groups_wanted_n_active.append(str(id_group))
     self.combo_box2.insertItem(0,str(id_group))
     color_2 = QColor("red")
     self.combo_box_gr.setItemData(0, color_2, Qt.BackgroundRole)
     self.combo_box_gr.setItemData(0, "non avtivee", Qt.ToolTipRole)
     db.commit()
     cursor.execute("FLUSH TABLES users;")
     db.close()
     db = sql.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
     cursor = db.cursor()  
     self.btn.hide()
   def initialise(self):
      global niv,libele,service,id_group,de_test,nbr_seance,id_client,done,groups_wanted,groupes_selected,groups_wanted_n_active
      niv = None
      libele = None
      service = None
      id_group = None
      de_test = 0
      nbr_seance = 1
      id_client = None
      done = False
      groups_wanted = []
      groups_wanted_n_active = []
      groupes_selected = []
      self.checkBox1.setDisabled(False)
      self.checkBox2.setDisabled(False)
      self.checkBox3.setDisabled(False)
      self.checkBox4.setDisabled(False)
      self.textbox4.setDisabled(False)
      self.textbox4.clear()
      self.textbox_id_clt.clear()
      self.combo_box.clear()
      self.combo_box1.clear()
      self.combo_box2.clear()
      self.combo_box_gr.clear()
def affich_inscription():
   global cursor,db

   global window_inscription
   window_inscription = new_win() 
   window_inscription.setWindowModality(QtCore.Qt.ApplicationModal)

   window_inscription.show() 
# app = QtWidgets.QApplication(sys.argv)
# affich_inscription()
# app.exec_()
# if __name__=='__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     win =new_win()
#     win.resize(700,700)
#     # win.setStyleSheet("background-image: url(preview.jpg)")
#     # win.move(0,0)
#     win.setWindowTitle("centre de formation")
    
#     win.show()
#     app.exec_()
if __name__ == "__main__":
   app = QtWidgets.QApplication(sys.argv)
   affich_inscription()
   app.exec_()