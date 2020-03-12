from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from functools import partial
from PyQt5.QtCore import pyqtSlot
from clicking import buttonClicked
import sys

class App(QtWidgets.QDialog):

    def __init__(self, raw, c_f, location, loc_1, loc_2, loc_3, loc_4, title):
        super(App, self).__init__()
        self.location = location
        self.raw = raw
        self.c_f = c_f
        self.loc_1 = loc_1
        self.loc_2 = loc_2
        self.loc_3 = loc_3
        self.loc_4 = loc_4
        self.title = title
        self.left = 10
        self.top = 10
        self.width = 10
        self.height = 10
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
            button.clicked.connect(partial(buttonClicked, self.raw, self.c_f, i, self.loc_2, self.loc_2, self.loc_3, self.loc_4))

        self.horizontalGroupBox.setLayout(layout)
    # App = App(self.loc_2[top_loc], loc_1, loc_2, loc_3, loc_4)
    # sys.exit(App.exec_())

