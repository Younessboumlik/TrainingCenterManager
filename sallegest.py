from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QVBoxLayout,QWidget,QTableWidgetItem,QPushButton,QScrollArea
from PyQt5.QtGui import QColor,QIcon
# from PyQt5.Qt import ApplicatiomModal
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
class SalleGest(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/classroom.png"))
        # Window properties
        self.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.setWindowTitle("Gestion Des Salles")
        # self.setStyleSheet("background-color: silver")
        self.setStyleSheet("background-color: #D3D3D3")
        self.setFixedSize(self.size())
        # Title frame
        self.title_frame = QtWidgets.QLabel(self)
        self.title_frame.setText("Liste Des Salles")
        self.title_frame.setStyleSheet("background-color: #1AAECB; color: white; font: 14pt monospace")
        self.title_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.title_frame.setFixedHeight(70)
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
        self.name_label = QtWidgets.QLabel(self.manage_frame, text="Nom Salle :",styleSheet='font-weight: bold')
        self.type_label = QtWidgets.QLabel(self.manage_frame, text="Type:",styleSheet='font-weight: bold')
        self.add_btn = QtWidgets.QPushButton(self.manage_frame, text="Ajouter Salles", styleSheet="background-color: #0000FF; color: white")
        self.update_btn = QtWidgets.QPushButton(self.manage_frame, text="Modifier Salles",styleSheet="background-color: #008000; color: white")
        self.clear_btn=QtWidgets.QPushButton(self.manage_frame, text="Vider les champs",styleSheet="background-color: #CB4335; color: white")
        
        self.id_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff",alignment=QtCore.Qt.AlignCenter)
        self.id_entry.setPlaceholderText("Veulliez entrer l'identifiant")
        self.name_entry = MyLineEdit(self.manage_frame, styleSheet="background-color: #e6ffff", alignment=QtCore.Qt.AlignCenter)
        self.name_entry.setPlaceholderText("Veulliez entrer le nom de la salle")
        # Combobox for gender
        self.type_combo = QtWidgets.QComboBox(self.manage_frame)
        self.type_combo.addItems(["","P", "V"])
        # Layout management
        self.manage_frame_layout = QtWidgets.QVBoxLayout(self.manage_frame)
        self.manage_frame_layout.addWidget(self.id_label)
        self.manage_frame_layout.addWidget(self.id_entry)
        self.manage_frame_layout.addWidget(self.name_label)
        self.manage_frame_layout.addWidget(self.name_entry)
        self.manage_frame_layout.addWidget(self.type_label)
        self.manage_frame_layout.addWidget(self.type_combo)
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
        self.del_btn = QtWidgets.QPushButton(self.button_frame, text="Supprimer Salle", styleSheet="background-color: #FF0000; color: white")
        self.delete_label = QtWidgets.QLabel(self.button_frame, text="Supprimer Salle:",styleSheet='font-weight: bold')
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
        self.button_frame_layout.setSpacing(20) # Espacement de 10 pixels entre les boutons
        self.button_frame_layout.setAlignment(QtCore.Qt.AlignTop) # Aligne les boutons en haut
        spacer = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.button_frame_layout.addItem(spacer)

        # Button actions
        self.add_btn.clicked.connect(self.add_Salle)
        self.del_btn.clicked.connect(self.delete_Salle)
        self.update_btn.clicked.connect(self.update_Salle)
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
        self.table_frame.setGeometry(QtCore.QRect(630, 70, 650, 890))        
        self.table = QTableWidget(self)
        self.table.setStyleSheet("background-color: white;")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setRowCount(0)
        self.table.resize(1300, 1300)
        self.table.move(500, 70)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["          ID_Salle          ", "          Nom_Salle          ","          Typr_Salle          "])
        self.table_frame_layout.addWidget(self.table)

    def button_clicked(self):
        global cursor,db

        cursor.execute(f"SELECT  * FROM salle ")
        cg = cursor.fetchall()
        self.table.setRowCount(len(cg))  # Explicitly set the number of rows
        for i, elm in enumerate(cg):
                row = [str(c) for c in elm]   
                for j, data in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(data))  
        self.table.resizeColumnsToContents() 
        self.show()
    def add_Salle(self):
        global cursor,db

        # Get input data
        id = self.id_entry.text()
        name = self.name_entry.text()
        type = self.type_combo.currentText()
        cursor.execute("insert salle(nom_salle,type_salle) values(%s,%s)",
                       (name,type))
        db.commit()
        # db.close()
        # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        # cursor = db.cursor()  
        # Display success message
        QtWidgets.QMessageBox.information(self, "Succès", "Salle ajouté avec succès")
    def delete_Salle(self):
        global cursor,db

        # Get input data
        id = self.delete_entry.text()
        reply = QMessageBox.warning(self, 'Confirmation', 
                                 "Êtes-vous sûr de vouloir supprimer ce Salle?", 
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # cursor = db.cursor()
            cursor.execute(f"DELETE FROM salle WHERE id_salle = %s", (id,))
            db.commit()
            # db.close()
            # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
            # cursor = db.cursor()  
            self.delete_entry.clear()
        # Display success message
        QtWidgets.QMessageBox.information(self, "Succès", "Salle supprimé avec succès")
    def update_Salle(self):
        # Get input data
        id = self.id_entry.text()
        name = self.name_entry.text()
        type = self.type_combo.currentText()
        cursor.execute(f"""UPDATE salle
                           SET nom_salle = '{name}', type_salle = '{type}'
                           WHERE id_salle = {id}""")
        db.commit()
        # db.close()/
        # db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        # cursor = db.cursor()  
        QtWidgets.QMessageBox.information(self, "Succès", "Salle mis à jour avec succès")

    def clear_inputs(self):
        global cursor,db

        # Clear all input fields
        self.id_entry.clear()
        self.name_entry.clear()
        self.type_combo.setCurrentIndex(0)

    def close(self):
        self.destroy()
        

def gestion_salle():
   global window_inscription
   window_inscription = SalleGest()   
   window_inscription.setWindowModality(QtCore.Qt.ApplicationModal)
   window_inscription.show() 
# app = QtWidgets.QApplication(sys.argv)
# gestion_salle()
# app.exec_()
