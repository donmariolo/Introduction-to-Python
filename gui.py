# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:47:43 2016

@author: marioromero
"""

from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QVBoxLayout, QHBoxLayout)

class Form(QWidget):
    def __init__(self, nombre, parent=None):
        super(Form, self).__init__(parent)
        
        self.nameLabel = QLabel("Yuhuuu!")
        self.nameLabel2 = QLabel(nombre)
        
        self.horizontal = QWidget()
        self.horizontalLayout = QHBoxLayout()
        self.horizontal.setLayout(self.horizontalLayout)
        
        self.numeros = []
        for i in range(1,11):
            self.numeros.append(QLabel("{}".format(i)))
            self.horizontalLayout.addWidget(self.numeros[-1])
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.nameLabel)
        self.mainLayout.addWidget(self.nameLabel2)
        self.mainLayout.addWidget(self.horizontal)
        
        self.setLayout(self.mainLayout)
        
        self.setWindowTitle("Hola")
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    screen = Form("Mario")
    screen.show()
    sys.exit(app.exec_())