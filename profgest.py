from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QVBoxLayout,QWidget,QTableWidgetItem,QPushButton,QScrollArea
from PyQt5.QtGui import QColor,QIcon
import sys
import mysql.connector
global db 
global cursor
db = mysql.connector.connect(host="localhost", user="root", password="Dlsfifaftspes21.", database="gestion_de_centre")
cursor=db.cursor()
class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        super(MyLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.focusNextChild()
class ProfGest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/prof.png"))
        # Window properties
        self.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.setWindowTitle("Gestion Des Professeurs")
        # self.setStyleSheet("background-color: silver")
        self.setStyleSheet("background-color: #D3D3D3")
        self.setFixedSize(self.size())
        # Title frame
        self.title_frame = QtWidgets.QLabel(self)
        self.title_frame.setText("Liste Des Profs")
        self.title_frame.setStyleSheet("background-color: #1AAECB; color: white; font: 14pt monospace")
        self.title_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.title_frame.setFixedHeight(70)
        # self.title_frame.setFixedWidth(800)
        # self.title_frame.move(500,30)
        # Create a QVBoxLayout for the parent widget (self in your case)
        layout = QtWidgets.QVBoxLayout(self)
        # Add title_frame to the layout
        layout.addWidget(self.title_frame)
        layout.addStretch(1)
        # Set the layout for the parent widget
        self.setLayout(layout)
        # Management Frame
        self.manage_frame = QtWidgets.QFrame(self)
        self.manage_frame.setStyleSheet("background-color: white")
        self.manage_frame.setGeometry(QtCore.QRect(10, 0, 300, 600))  # Move manage_frame to the top left edge
        
        # Labels and entries
        self.id_label = QtWidgets.QLabel(self.manage_frame, text="ID :",styleSheet='font-weight: bold')
        self.name_label = QtWidgets.QLabel(self.manage_frame, text="Nom :",styleSheet='font-weight: bold')
        self.prenom_label = QtWidgets.QLabel(self.manage_frame, text="Prénom:",styleSheet='font-weight: bold')
        self.email_label = QtWidgets.QLabel(self.manage_frame, text="Email:",styleSheet='font-weight: bold')
        self.phone_label = QtWidgets.QLabel(self.manage_frame, text="Telephone:",styleSheet='font-weight: bold')
        self.titre_label = QtWidgets.QLabel(self.manage_frame, text="Titre:",styleSheet='font-weight: bold')
        # self.gender_label = QtWidgets.QLabel(self.manage_frame, text="Sexe:",styleSheet='font-weight: bold')
        self.add_btn = QtWidgets.QPushButton(self.manage_frame, text="Ajouter Prof", styleSheet="background-color: #0000FF; color: white")
        self.update_btn = QtWidgets.QPushButton(self.manage_frame, text="Modifier Prof",styleSheet="background-color: #008000; color: white")
        self.clear_btn=QtWidgets.QPushButton(self.manage_frame, text="Vider les champs",styleSheet="background-color: #CB4335; color: white")
        
        self.id_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff",alignment=QtCore.Qt.AlignCenter)
        self.id_entry.setPlaceholderText("Veulliez entrer l'identifiant")
        self.name_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.name_entry.setPlaceholderText("Veulliez entrer le nom")
        self.prenom_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.prenom_entry.setPlaceholderText("Veulliez entrer le prénom")
        self.email_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.email_entry.setPlaceholderText("Veulliez entrer l'email")
        self.phone_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.phone_entry.setPlaceholderText("Veulliez entrer le num")
        self.titre_entry = QtWidgets.QLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.titre_entry.setPlaceholderText("Veulliez entrer les compétances")
        # Combobox for gender
        # self.gender_combo = QtWidgets.QComboBox(self.manage_frame)
        # self.gender_combo.addItems(["","male", "femele"])
        # Layout management
        self.manage_frame_layout = QtWidgets.QVBoxLayout(self.manage_frame)
        self.manage_frame_layout.addWidget(self.id_label)
        self.manage_frame_layout.addWidget(self.id_entry)
        self.manage_frame_layout.addWidget(self.name_label)
        self.manage_frame_layout.addWidget(self.name_entry)
        self.manage_frame_layout.addWidget(self.prenom_label)
        self.manage_frame_layout.addWidget(self.prenom_entry)
        self.manage_frame_layout.addWidget(self.email_label)
        self.manage_frame_layout.addWidget(self.email_entry)
        self.manage_frame_layout.addWidget(self.phone_label)
        self.manage_frame_layout.addWidget(self.phone_entry)
        self.manage_frame_layout.addWidget(self.titre_label)
        self.manage_frame_layout.addWidget(self.titre_entry)
        # self.manage_frame_layout.addWidget(self.gender_label)
        # self.manage_frame_layout.addWidget(self.gender_combo)
        self.manage_frame_layout.addWidget(self.add_btn)
        self.manage_frame_layout.addWidget(self.update_btn)
        self.manage_frame_layout.addWidget(self.clear_btn)
        self.manage_frame_layout.setSpacing(10) # Espacement de 10 pixels entre les boutons
        
        
        # Button Frame
        self.button_frame = QtWidgets.QFrame(self)
        self.button_frame.setGeometry(QtCore.QRect(10, 700, 300, 300))  
        self.button_frame.setStyleSheet("background-color: white")

        # Buttons
        style_sheet = "color: white; background-color: #2980B9;" 
        self.del_btn = QtWidgets.QPushButton(self.button_frame, text="Supprimer Prof", styleSheet="background-color: #FF0000; color: white")
        self.delete_label = QtWidgets.QLabel(self.button_frame, text="Supprimer Prof:",styleSheet='font-weight: bold')
        self.delete_entry = QtWidgets.QLineEdit(self.button_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.delete_entry.setPlaceholderText("Veulliez entrer l'identifiant")
        self.exit_btn=QtWidgets.QPushButton(self.button_frame, text="Quitter",styleSheet="background-color: #FFA500; color: black")
        self.button_frame_layout = QtWidgets.QVBoxLayout(self.button_frame) # Remplacez par QHBoxLayout
        self.suppZone_label = QtWidgets.QLabel(self.button_frame)
        self.suppZone_label.setText("Suppression")
        self.suppZone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.suppZone_label.setFont(QtGui.QFont("Deco", 14))
        self.suppZone_label.setStyleSheet(style_sheet)  
        self.button_frame_layout.addWidget(self.suppZone_label) 
        self.button_frame_layout.addWidget(self.delete_label)
        self.button_frame_layout.addWidget(self.delete_entry)
        self.button_frame_layout.addWidget(self.del_btn)
        self.button_frame_layout.addWidget(self.exit_btn)
        self.button_frame_layout.setSpacing(30) # Espacement de 10 pixels entre les boutons
        self.button_frame_layout.setAlignment(QtCore.Qt.AlignTop) # Aligne les boutons en haut
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_frame_layout.addItem(spacer)

        # Button actions
        self.add_btn.clicked.connect(self.add_Prof)
        self.del_btn.clicked.connect(self.delete_Prof)
        self.update_btn.clicked.connect(self.update_Prof)
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.exit_btn.clicked.connect(self.close)
        
        self.button = QPushButton("Actualiser", self)
        self.button.setStyleSheet('''
                                            background-color: #87CEEB;
                                            border: 3px solid #333333;
                                            border-radius: 10px;
                                            color: #000000;
                                            text-align: center;
                                            font-size: 20px;
                                            padding: 10px;
                                            width: 150px;
                                                                                ''')
        self.button.resize(150, 60)
        self.button.move(80, 620)
        self.button.clicked.connect(self.button_clicked)
        
        #___________Table
        self.table_frame = QtWidgets.QFrame(self)
        self.table_frame_layout = QtWidgets.QVBoxLayout(self.table_frame)
        self.table_frame.setGeometry(QtCore.QRect(450, 70, 1300, 890))        
        self.table = QTableWidget(self)
        self.table.setStyleSheet("background-color: white;")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setRowCount(0)
        self.table.resize(1300, 1300)
        self.table.move(500, 70)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["          ID_Prof          ", "          Nom_Prof          ","          Prénom_Prof          ",
                                              "                   Telephone                     ","          Email          ","   Titre   "])
        self.table_frame_layout.addWidget(self.table)

    def button_clicked(self):
        global cursor,db

        cursor.execute(f"SELECT  * FROM professeur ")
        cg = cursor.fetchall()
        self.table.setRowCount(len(cg))  
        for i, elm in enumerate(cg):
                row = [str(c) for c in elm]   
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))  
        self.table.resizeColumnsToContents() 
        self.show()
    def add_Prof(self):
        global cursor,db

        # Get input data
        id = self.id_entry.text()
        name = self.name_entry.text()
        prenom = self.prenom_entry.text()
        email = self.email_entry.text()
        phone = self.phone_entry.text()
        titre = self.titre_entry.text()
        # gender = self.gender_combo.currentText()
        cursor.execute("insert professeur(nom_prof,prenom_prof,email_prof,tel_prof,titre) values(%s,%s,%s,%s,%s)",
                       (name,prenom,email,phone,titre))
        db.commit()
        # db.close()
        # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        # cursor = db.cursor()  
        # Display success message
        QtWidgets.QMessageBox.information(self, "Succès", "Prof ajouté avec succès")
    def delete_Prof(self):
        global cursor,db

        # Get input data
        id = self.delete_entry.text()
        reply = QMessageBox.warning(self, 'Confirmation', 
                                 "Êtes-vous sûr de vouloir supprimer ce Prof?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # cursor = db.cursor()
            cursor.execute(f"DELETE FROM professeur WHERE id_professeur = %s", (id,))
            db.commit()
            # db.close()
            # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
            # cursor = db.cursor()  
            self.delete_entry.clear()
        # Display success message
        QtWidgets.QMessageBox.information(self, "Succès", "Prof supprimé avec succès")
    def update_Prof(self):
        global cursor,db

        # Get input data
        id = self.id_entry.text()
        name = self.name_entry.text()
        prenom = self.prenom_entry.text()
        email = self.email_entry.text()
        phone = self.phone_entry.text()
        titre = self.titre_entry.text()
        # gender = self.gender_combo.currentText()
        cursor.execute(f"""UPDATE professeur
                           SET nom_prof = '{name}', prenom_prof = '{prenom}', email_prof = '{email}', tel_prof='{phone}' , titre = '{titre}'
                           WHERE id_professeur = {id}""")
        db.commit()
        # db.close()
        # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        # cursor = db.cursor()  
        QtWidgets.QMessageBox.information(self, "Succès", "Prof mis à jour avec succès")

    def clear_inputs(self):
        global cursor,db
        # Clear all input fields
        self.id_entry.clear()
        self.name_entry.clear()
        self.prenom_entry.clear()
        self.email_entry.clear()
        self.phone_entry.clear()
        self.titre_entry.clear()
        # self.gender_combo.setCurrentIndex(0)

    def close(self):
        self.destroy()
        
win = None
def gestion_prof():
    global win
    # app = QtWidgets.QApplication(sys.argv)
    win =ProfGest()
    win.resize(700,700)
    # win.setStyleSheet("background-image: url(preview.jpg)")
    # win.move(0,0)
    # win.setWindowTitle("centre de formation")
    win.setWindowModality(QtCore.Qt.ApplicationModal)
    win.show()
    # app.exec_()