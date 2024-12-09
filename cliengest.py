from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QVBoxLayout,QWidget,QTableWidgetItem,QPushButton,QScrollArea
from PyQt5.QtGui import QColor,QIcon
from PyQt5 import QtCore
import sys
import mysql.connector
global db 
global cursor
db = mysql.connector.connect(host=os.getenv('DB_HOST'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), database=os.getenv('DB_NAME'))
cursor=db.cursor()
class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        super(MyLineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.focusNextChild()
class Clientgest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/user.png"))

        # Window properties
        self.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.setWindowTitle("Sys gestion Clients")
        # self.setStyleSheet("background-color: silver")
        self.setStyleSheet("background-color: #D3D3D3")
        self.setFixedSize(self.size())
        # Title frame
        self.title_frame = QtWidgets.QLabel(self)
        self.title_frame.setText("Liste Des Clients")
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
        self.gender_label = QtWidgets.QLabel(self.manage_frame, text="Sexe:",styleSheet='font-weight: bold')
        self.add_btn = QtWidgets.QPushButton(self.manage_frame, text="Ajouter Client", styleSheet="QPushButton {background-color: #0000FF; color: white;} QPushButton:hover{background-color:white ; color: #0000FF;}")
        self.update_btn = QtWidgets.QPushButton(self.manage_frame, text="Modifier Client",styleSheet="QPushButton {background-color: #008000; color: white;} QPushButton:hover{background-color:white ; color: #008000;}")
        self.clear_btn=QtWidgets.QPushButton(self.manage_frame, text="Vider les champs",styleSheet="QPushButton {background-color: #CB4335; color: white;} QPushButton:hover{background-color:white ; color: #CB4335;}")
        
        self.id_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff",alignment=QtCore.Qt.AlignCenter)
        self.id_entry.setPlaceholderText("Veulliez entrer l'identifiant")
        self.name_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.name_entry.setPlaceholderText("Veulliez entrer le nom")
        self.prenom_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.prenom_entry.setPlaceholderText("Veulliez entrer le prénom")
        self.email_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.email_entry.setPlaceholderText("Veulliez entrer l'email")
        self.phone_entry = QtWidgets.QLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.phone_entry.setPlaceholderText("Veulliez entrer le num")
        # Combobox for gender
        self.gender_combo = QtWidgets.QComboBox(self.manage_frame)
        self.gender_combo.addItems(["","male", "femele"])
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
        self.manage_frame_layout.addWidget(self.gender_label)
        self.manage_frame_layout.addWidget(self.gender_combo)
        self.manage_frame_layout.addWidget(self.add_btn)
        self.manage_frame_layout.addWidget(self.update_btn)
        self.manage_frame_layout.addWidget(self.clear_btn)
        self.manage_frame_layout.setSpacing(10) # Espacement de 10 pixels entre les boutons
        
        
        # Button Frame
        self.button_frame = QtWidgets.QFrame(self)
        self.button_frame.setGeometry(QtCore.QRect(10, 700, 300, 300))  # Move button frame to the left edge
        self.button_frame.setStyleSheet("background-color: white")

        # Buttons
        style_sheet = "color: white; background-color: #2980B9;"  # Adjust colors as needed
        self.del_btn = QtWidgets.QPushButton(self.button_frame, text="Supprimer Client", styleSheet="background-color: #FF0000; color: white")
        self.delete_label = QtWidgets.QLabel(self.button_frame, text="Supprimer Client:",styleSheet='font-weight: bold')
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
        self.add_btn.clicked.connect(self.add_client)
        self.del_btn.clicked.connect(self.delete_client)
        self.update_btn.clicked.connect(self.update_client)
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
        self.table.setHorizontalHeaderLabels(["          ID_Client          ", "          Nom_Client          ","          Prénom_Client          ",
                                              "                    Email                    ","          Telphone          ","   Sexe   "])
        self.table_frame_layout.addWidget(self.table)

    def button_clicked(self):
        cursor.execute(f"SELECT  * FROM client ")
        cg = cursor.fetchall()
        self.table.setRowCount(len(cg))  # Explicitly set the number of rows
        for i, elm in enumerate(cg):
                row = [str(c) for c in elm]   
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))  
        self.table.resizeColumnsToContents() 
        self.show()
    def add_client(self):
        
        id = self.id_entry.text()
        name = self.name_entry.text()
        prenom = self.prenom_entry.text()
        email = self.email_entry.text()
        phone = self.phone_entry.text()
        gender = self.gender_combo.currentText()
        try:
            cursor.execute("insert client(id_client,nom,prenom,email,telephone,sexe) values(%s,%s,%s,%s,%s,%s)",
                            (id,name,prenom,email,phone,gender))
            db.commit()
            QtWidgets.QMessageBox.information(self, "Succès", "Client ajouté avec succès")
        except:
            QtWidgets.QMessageBox.warning(self,"Erreur","Il y a une erreur lors de l'exécution de l'opération. Veuillez vérifier votre saisie.")
            

        # db.close()
        # db = mysql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
        # cursor = db.cursor()  
        # Display success message
        
    def delete_client(self):
        # Get input data
        id = self.delete_entry.text()
        reply = QMessageBox.warning(self, 'Confirmation', 
                                 "Êtes-vous sûr de vouloir supprimer ce cours?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM client WHERE id_client = %s", (id,))
            db.commit()
            # db.close()
            # db = mysql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
            # cursor = db.cursor()  
            self.delete_entry.clear()
        # Display success message
        QtWidgets.QMessageBox.information(self, "Succès", "Client supprimé avec succès")
    def update_client(self):
        # Get input data
        id = self.id_entry.text()
        name = self.name_entry.text()
        prenom = self.prenom_entry.text()
        email = self.email_entry.text()
        phone = self.phone_entry.text()
        gender = self.gender_combo.currentText()
        try:
            cursor.execute(f"""UPDATE client
                            SET nom = '{name}', prenom = '{prenom}', email = '{email}', telephone='{phone}' , sexe = '{gender}'
                            WHERE id_client = {id}""")
            db.commit()
            # db.close()
            # db = mysql.connect(host = os.getenv('DB_HOST'),user = os.getenv('DB_USER'),passwd  = os.getenv('DB_PASSWORD'),database = os.getenv('DB_NAME'))
            # cursor = db.cursor()  
            QtWidgets.QMessageBox.information(self, "Succès", "Client mis à jour avec succès")
        except:
            QtWidgets.QMessageBox.warning(self,"Erreur","Il y a une erreur lors de l'exécution de l'opération. Veuillez vérifier votre saisie.")

    def clear_inputs(self):
        # Clear all input fields
        self.id_entry.clear()
        self.name_entry.clear()
        self.prenom_entry.clear()
        self.email_entry.clear()
        self.phone_entry.clear()
        self.gender_combo.setCurrentIndex(0)

    def close(self):
        self.destroy()
        
win = None
def client_gest():
    global win
    win =Clientgest()
    win.resize(700,700)
    # win.setStyleSheet("background-image: url(preview.jpg)")
    # win.move(0,0)
    win.setWindowTitle("Gestion Des Clients")
    win.setWindowModality(QtCore.Qt.ApplicationModal)
    win.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    client_gest()
    app.exec_()