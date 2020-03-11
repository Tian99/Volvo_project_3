from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from functools import partial
from PyQt5.QtCore import pyqtSlot
import sys

class App(QtWidgets.QDialog):

    def __init__(self, location, loc_1):
        super(App, self).__init__()
        self.location = location
        self.loc_1 = loc_1
        self.title = 'Application'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 1000
        self.initUI()
        # self.findButton()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createGridLayout()
        
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        
        for i in self.location:
            button = QPushButton('{}\n\n#Claims:{}'.format(i, self.location[i]))
            layout.addWidget(button)
            button.clicked.connect(partial(self.buttonClicked, i))

        self.horizontalGroupBox.setLayout(layout)

    def buttonClicked(self, top_loc):
        print(top_loc)


