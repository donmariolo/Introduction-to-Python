# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:28:35 2016

@author: marioromero
"""

from PyQt5 import QtWidgets, uic
import funciones_conversortemperatura as fc

FormClasses = uic.loadUiType("conversortemperatura.ui")

class MyWindowClass(FormClasses[1], FormClasses[0]):

    def __init__(self, parent=None):
        FormClasses[1].__init__(self, parent)
        self.setupUi(self)
        
        self.c2fPushButton.clicked.connect(self.c2f)
        self.f2cPushButton.clicked.connect(self.f2c)        
        
    def c2f(self):
        valor = self.cDoubleSpinBox.value()
        self.fDoubleSpinBox.setValue(fc.c2fconversor(valor))
        
    def f2c(self):
        valor = self.fDoubleSpinBox.value()
        self.cDoubleSpinBox.setValue(fc.f2cconversor(valor))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()