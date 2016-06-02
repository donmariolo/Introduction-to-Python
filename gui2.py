# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:20:30 2016

@author: marioromero
"""

from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout,QPushButton, QMessageBox, QLineEdit)

class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.nameLabel = QLabel("Introduce tu nombre:")
        self.nameField = QLineEdit()
        self.sayHiButton = QPushButton("Saludar")
        self.buttonLayout = QVBoxLayout()
        self.buttonLayout.addWidget(self.nameLabel)
        self.buttonLayout.addWidget(self.nameField)
        self.buttonLayout.addWidget(self.sayHiButton)
        # Aqui conectamos la se~nal al slot
        self.sayHiButton.clicked.connect(self.sayHi)
        self.setLayout(self.buttonLayout)
        self.setWindowTitle("Ahora con se~nales!")
        
    def sayHi(self):
        if self.nameField.text() == "":
            QMessageBox.warning(self, "Error", "No ha introducido nada en el campo.")
        else:
            QMessageBox.information(self, "Bienvenido", "Hola, {}.".format(self.nameField.text()))

    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    screen = Form()
    screen.show()
    sys.exit(app.exec_())
    
    """
    Modi
car la funcion sayHi para que veri
que el contenido del
campo editable (el metodo text() devuelve el texto
introducido). Si el campo de texto esta vaco, lanzar un
mensaje de aviso (QMessageBox.warning), si contiene algo de
texto lanzar el mensaje de informacion 'Hola' seguido del texto
introducido.
"""