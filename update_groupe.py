from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QTableWidget,QVBoxLayout,QWidget,QTableWidgetItem,QPushButton,QScrollArea
from PyQt5.QtGui import QColor,QIcon
import sys
import mysql.connector
global db 
global cursor
db = mysql.connector.connect(host="localhost", user="root", password="Dlsfifaftspes21.", database="gestion_de_centre")
cursor=db.cursor()
class UpdateGRP(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/changes.png"))
        self.setWindowTitle("Update Groupe")
        # Window properties
        self.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        # self.setStyleSheet("background-color: silver")
        self.setStyleSheet("background-color: #D3D3D3")
        self.setFixedSize(self.size())
        # Title frame
        self.title_frame = QtWidgets.QLabel(self)
        self.title_frame.setText("Mis à jour des clients en liste d'attente")
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
        self.button.move(30, 20)
        self.button.clicked.connect(self.button_clicked)
        #___________Table
        self.table_frame = QtWidgets.QFrame(self)
        self.table_frame_layout = QtWidgets.QVBoxLayout(self.table_frame)
        self.table_frame.setGeometry(QtCore.QRect(30, 100, 1850, 900))        
        self.table = QTableWidget(self)
        self.table.setStyleSheet("background-color: white;")
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table.setRowCount(0)
        self.table.resize(1300, 1300)
        self.table.move(500, 70)
        self.table.setColumnCount(12)
        self.table.setHorizontalHeaderLabels(["          ID_Client          ", 
                                              "          ID_Groupe         ",
                                              "          ID_Cours         ",
                                              "           Nom Cours       ",
                                                "niveau_scolaire",
                                                "id_seance",
                                                "   jour   ", 
                                                "    heure    ",
                                                " nom_client",
                                                "prenom_client", 
                                                "telephone_client", 
                                                "email_client"])
        self.table_frame_layout.addWidget(self.table)

    def updateGRP(self):
        global cursor,db

    # Obtenez tous les id_cours
        query = "SELECT DISTINCT id_cours FROM Groupe"
        cursor.execute(query)
        id_cours_list = cursor.fetchall()
        for id_cours_tuple in id_cours_list:
            id_cours = id_cours_tuple[0]  # Extract the value from the tuple
            # Obtenez tous les groupes de réserve pour ce cours
            query = "SELECT id_groupe FROM Groupe WHERE id_cours = %s AND nbr_clients < 4"
            cursor.execute(query, (id_cours,))
            groupes_reserve = cursor.fetchall()
            for id_groupe_reserve in groupes_reserve:
                id_groupe_reserve=id_groupe_reserve[0]
                # Obtenez tous les clients dans ce groupe de réserve
                query = "SELECT id_client FROM appartenir WHERE id_groupe = %s"
                cursor.execute(query, (id_groupe_reserve,))
                clients = cursor.fetchall()
                for id_client in clients:
                    id_client=id_client[0]
                    # Trouvez un groupe avec moins de 8 clients, en donnant la priorité aux groupes avec le plus de clients
                    query = "SELECT id_groupe FROM Groupe WHERE id_cours = %s AND nbr_clients BETWEEN 4 AND 7 ORDER BY nbr_clients DESC LIMIT 1"
                    cursor.execute(query, (id_cours,))
                    groupe = cursor.fetchone()

                    if groupe is not None:
                        # Un groupe avec moins de 8 clients existe, déplacez le client vers ce groupe
                        id_groupe = groupe[0]
                        query = "UPDATE appartenir SET id_groupe = %s WHERE id_client = %s AND id_groupe = %s"
                        cursor.execute(query, (id_groupe, id_client, id_groupe_reserve))
                        query = "UPDATE Groupe SET nbr_clients = nbr_clients + 1 WHERE id_groupe = %s"
                        cursor.execute(query, (id_groupe,))
                        query = "UPDATE Groupe SET nbr_clients = nbr_clients - 1 WHERE id_groupe = %s"
                        cursor.execute(query, (id_groupe_reserve,))
        db.commit()
        db.close()
        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        cursor = db.cursor()  
    def button_clicked(self):
        global cursor,db
        self.updateGRP()
        # Obtenez tous les id_cours
        query = "SELECT DISTINCT id_cours FROM Groupe"
        cursor.execute(query)
        id_cours_list = cursor.fetchall()
        for id_cours_tuple in id_cours_list:
            id_cours = id_cours_tuple[0]

            # Obtenez les nouveaux clients et leurs informations de cours
            query = ''' SELECT app.id_client, app.id_groupe, g.id_cours, c.libele,
                     c.niv_scol, s.id_seance, s.jour_seance, s.heure_seance,
                    cl.nom, cl.prenom, cl.telephone, cl.email
                        FROM appartenir app
                            JOIN Groupe g ON app.id_groupe = g.id_groupe
                            JOIN Cours c ON g.id_cours = c.id_cours
                            JOIN Seance s ON c.id_cours = s.id_cours
                            JOIN Client cl ON app.id_client = cl.id_client
                            WHERE app.id_groupe IN (
                                    SELECT id_groupe
                                    FROM Groupe
                                    WHERE id_cours = %s )'''
            cursor.execute(query, (id_cours,))
            cg = cursor.fetchall()
            # Ajoutez les nouveaux clients et leurs informations de cours à la table
            for i, row in enumerate(cg):
                id_client, id_groupe, id_cours, nom_cours, niveau_scolaire, id_seance, jour, heure, nom_client, prenom_client, telephone_client, email_client = row
                self.table.setRowCount(i + 1)
                self.table.setItem(i, 0, QTableWidgetItem(str(id_client)))
                self.table.setItem(i, 1, QTableWidgetItem(str(id_groupe)))
                self.table.setItem(i, 2, QTableWidgetItem(str(id_cours)))
                self.table.setItem(i, 3, QTableWidgetItem(nom_cours))
                self.table.setItem(i, 4, QTableWidgetItem(niveau_scolaire))
                self.table.setItem(i, 5, QTableWidgetItem(str(id_seance)))
                self.table.setItem(i, 6, QTableWidgetItem(jour))
                self.table.setItem(i, 7, QTableWidgetItem(heure))
                self.table.setItem(i, 8, QTableWidgetItem(nom_client))
                self.table.setItem(i, 9, QTableWidgetItem(prenom_client))
                self.table.setItem(i, 10, QTableWidgetItem(telephone_client))
                self.table.setItem(i, 11, QTableWidgetItem(email_client))
            self.table.resizeColumnsToContents() 
        db.commit()
        db.close()
        db = mysql.connector.connect(host = "localhost",user = "root",passwd = "Dlsfifaftspes21.",database = "gestion_de_centre")
        cursor = db.cursor()  

groupe_update = None
def update_groupe():
   global groupe_update
   groupe_update = UpdateGRP()
   groupe_update.setWindowModality(QtCore.Qt.ApplicationModal)

   groupe_update.show() 
