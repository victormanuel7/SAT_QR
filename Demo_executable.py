#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi

class QR_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Examinador.ui', self)
        self.pushButton.clicked.connect(self.browsefiles)
    
    def browsefiles(self):
        file=QFileDialog.getOpenFileName(self, 'Open File', r'C:\Users\Daniel Arias\Documents')
        self.filename.setText(file[0])

if __name__=='__main__':
    app=QApplication(sys.argv)
    GUI= QR_GUI()
    GUI.show()
    sys.exit(app.exec())
    
#Examinador.ui es un archico .ui y tiene que se creado en Pyqt5 Designer

