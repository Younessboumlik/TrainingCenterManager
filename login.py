from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit,QVBoxLayout,QToolButton
from PyQt5.QtCore import QTimer,Qt
from PyQt5.QtGui import QColor,QIcon

import sys
import time
#login page:
class MyLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        super(MyLineEdit, self).keyPressEvent(event)
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.focusNextChild()
class change_user_id(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Change Usr Id')
            self.resize(390, 300)
            self.setWindowIcon(QIcon("icons/password.png"))


            # User ID:
            self.label1 = QLabel('<font size="5"> User ID </font>', self)
            self.label1.move(10, 20)
            self.text1 = MyLineEdit(self)
            self.text1.setPlaceholderText('Entrer votre UserId')
            self.text1.move(170, 20)

            # ancien Password:
            self.label2 = QLabel('<font size="5"> Password </font>', self)
            self.label2.move(10, 80)
            self.text2 = MyLineEdit(self)
            self.text2.setEchoMode(QLineEdit.Password)
            self.text2.setPlaceholderText('Entrer votre Password')
            self.text2.move(170, 80)
            self.eye_btn = QToolButton(self)
            self.eye_btn.setIcon(QIcon('icons/oeil.png'))
            self.eye_btn.move(350, 80)
            self.eye_btn.clicked.connect(self.toggle_password_visibility)


            # nouveau UserId:
            self.label3 = QLabel('<font size="5"> New Usr Id </font>', self)
            self.label3.move(10, 140)
            self.text3 = MyLineEdit(self)
            # self.text3.setEchoMode(QLineEdit.Password)
            self.text3.setPlaceholderText('Entrer nouveau UserId')
            self.text3.move(170, 140)
            # Confirmation label:
            self.text1.textChanged.connect(self.not_empty)
            self.text2.textChanged.connect(self.not_empty)
            self.text3.textChanged.connect(self.not_empty)
            self.button = QPushButton('Done', self)
            self.button.move(80, 200)
            self.button.resize(200,50)

            self.button.clicked.connect(self.confirmation)
            self.button.setDisabled(True)
            self.label5 = None
        def toggle_password_visibility(self):
            if self.text2.echoMode() == QLineEdit.Password and self.text2.text():
                self.text2.setEchoMode(QLineEdit.Normal)
                self.eye_btn.setIcon(QIcon('icons/cacher.png'))
            else:
                self.text2.setEchoMode(QLineEdit.Password)
                self.eye_btn.setIcon(QIcon('icons/oeil.png')) 
        def close_app(self):
            self.close()
        def confirmation(self):
            if self.label5 != None:
                self.label5.hide()
            with open("login.txt","r+") as f:
                A = f.readlines()
                if self.text1.text() == A[0].strip() and self.text2.text() == A[1].strip():
                    with open("login.txt","w") as g:
                        g.write(self.text3.text())
                        g.write("\n")
                        g.write(self.text2.text())
                        self.label5 = QLabel('<font size="5"> Done </font>', self)
                        self.label5.setStyleSheet("font-size: 25px; font-family: Arial; color: green;")
                        self.label5.move(140, 245)                    
                        self.label5.show()
                        QTimer.singleShot(2000, self.close_app)
                else:
                    self.label5 = QLabel('<font size="5"> Wrong User Id or Password </font>', self)
                    self.label5.setStyleSheet("font-size: 20px; font-family: Arial; color: red;")
                    self.label5.move(2, 245)
                    self.label5.show()
                    self.text1.clear()
                    self.text2.clear()
                    self.text3.clear()

        def not_empty(self):
            if self.text1.text() and self.text2.text() and self.text3.text():
                self.button.setDisabled(False)
            else:
                self.button.setDisabled(True)

class change_password(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icons/password.png"))
        self.setWindowTitle('Change Password')
        self.resize(475, 380)

        # User ID:
        self.label1 = QLabel('<font size="5"> User ID </font>', self)
        self.label1.move(10, 20)
        self.text1 = MyLineEdit(self)
        self.text1.setPlaceholderText('Entrer votre UserId')
        self.text1.move(230, 20)

        # ancien Password:
        self.label2 = QLabel('<font size="5"> Old Password </font>', self)
        self.label2.move(10, 80)
        self.text2 = MyLineEdit(self)
        self.text2.setPlaceholderText('Entrer votre Password')
        self.text2.setEchoMode(QLineEdit.Password)
        self.text2.move(230, 80)
        self.eye_btn = QToolButton(self)
        self.eye_btn.setIcon(QIcon('icons/oeil.png'))
        self.eye_btn.move(415, 80)
        self.eye_btn.clicked.connect(self.toggle_password_visibility1)
        # nouveau Password:
        self.label3 = QLabel('<font size="5"> New Password </font>', self)
        self.label3.move(10, 140)
        self.text3 = MyLineEdit(self)
        self.text3.setPlaceholderText('Entrer le nouveau password')
        self.text3.setEchoMode(QLineEdit.Password)
        self.text3.move(230, 140)
        self.eye_btn2 = QToolButton(self)
        self.eye_btn2.setIcon(QIcon('icons/oeil.png'))
        self.eye_btn2.move(415, 140)
        self.eye_btn2.clicked.connect(self.toggle_password_visibility2)

        # confirmer password:
        self.label4 = QLabel('<font size="5"> Confirm Password </font>', self)
        self.label4.move(10, 200)
        self.text4 = MyLineEdit(self)
        self.text4.setPlaceholderText('Confirmer le password')
        self.text4.setEchoMode(QLineEdit.Password)
        self.text4.move(230, 200)
        self.eye_btn3 = QToolButton(self)
        self.eye_btn3.setIcon(QIcon('icons/oeil.png'))
        self.eye_btn3.move(415, 200)
        self.eye_btn3.clicked.connect(self.toggle_password_visibility3)

        # Confirmation button:
        self.button = QPushButton('Done', self)
        self.button.move(180, 260)
        self.button.clicked.connect(self.confirmation)
        self.button.setDisabled(True)
        self.label5 = None
        self.text1.textChanged.connect(self.not_empty)
        self.text2.textChanged.connect(self.not_empty)
        self.text3.textChanged.connect(self.not_empty)
        self.text4.textChanged.connect(self.not_empty)


        # Confirmation label:
    def toggle_password_visibility1(self):
        if self.text2.echoMode() == QLineEdit.Password and self.text2.text():
            self.text2.setEchoMode(QLineEdit.Normal)
            self.eye_btn.setIcon(QIcon('icons/cacher.png'))
        else:
            self.text2.setEchoMode(QLineEdit.Password)
            self.eye_btn.setIcon(QIcon('icons/oeil.png'))
    def toggle_password_visibility2(self):
        if self.text3.echoMode() == QLineEdit.Password and self.text3.text():
            self.text3.setEchoMode(QLineEdit.Normal)
            self.eye_btn2.setIcon(QIcon('icons/cacher.png'))
        else:
            self.text3.setEchoMode(QLineEdit.Password)
            self.eye_btn2.setIcon(QIcon('icons/oeil.png'))
    def toggle_password_visibility3(self):
        if self.text4.echoMode() == QLineEdit.Password and self.text4.text():
            self.text4.setEchoMode(QLineEdit.Normal)
            self.eye_btn3.setIcon(QIcon('icons/cacher.png'))
        else:
            self.text4.setEchoMode(QLineEdit.Password)
            self.eye_btn3.setIcon(QIcon('icons/oeil.png'))    
    def not_empty(self):
        if self.text1.text() and self.text2.text() and self.text3.text() and self.text4.text():
            self.button.setDisabled(False)
        else:
            self.button.setDisabled(True)
    def close_app(self):
        self.close()
    def confirmation(self):
        if self.label5 != None:
            self.label5.hide()

        with open("login.txt","r+") as f:
            A = f.readlines()
            if self.text3.text() == self.text4.text() and self.text1.text() == A[0].strip() and self.text2.text() == A[1].strip():
                with open("login.txt","w") as g:
                    g.write(self.text1.text())
                    g.write("\n")
                    g.write(self.text3.text())
                    self.label5 = QLabel('<font size="5"> Done </font>', self)
                    self.label5.setStyleSheet("font-size: 25px; font-family: Arial; color: green;")
                    self.label5.move(180, 320)                    
                    self.label5.show()
                    QTimer.singleShot(2000, self.close_app)


            elif self.text1.text() != A[0].strip() or self.text2.text() != A[1].strip():
                self.label5 = QLabel('<font size="5"> Wrong User Id or Password </font>', self)
                self.label5.setStyleSheet("font-size: 20px; font-family: Arial; color: red;")
                self.label5.move(55, 320)
                self.label5.show()
                self.text1.clear()
                self.text2.clear()
                self.text3.clear()
                self.text4.clear()
            elif self.text3.text() != self.text4.text():
                self.label5 = QLabel('<font size="5"> Pssword Not much </font>', self)
                self.label5.setStyleSheet("font-size: 20px; font-family: Arial; color: red;")
                self.label5.move(83, 320)
                self.label5.show()
changepassword = None

def password_change_window():
    global changepassword
    changepassword = change_password()
    changepassword.setWindowModality(Qt.ApplicationModal)

    changepassword.show()

changeuserid = None
def userid_change_window():
    global changeuserid
    changeuserid = change_user_id()
    changeuserid.setWindowModality(Qt.ApplicationModal)
    changeuserid.show()
# app = QApplication(sys.argv)
# userid_change_window()
# app.exec_()