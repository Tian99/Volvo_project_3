from PyQt5.QtWidgets import QApplication, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from functools import partial
from PyQt5.QtCore import pyqtSlot
from clicking import buttonClicked
from Dutils import mkmsg
import sys

class App(QtWidgets.QDialog):

    def __init__(self, raw, c_f, location, loc_1, loc_2, loc_3, loc_4, loc_5, level, Top, title, parent, stop = None):
        super(App, self).__init__(parent)
        self.location = location
        self.level = level + 1
        self.Top = Top
        self.raw = raw
        self.c_f = c_f
        self.loc_1 = loc_1
        self.loc_2 = loc_2
        self.loc_3 = loc_3
        self.loc_4 = loc_4
        self.loc_5 = loc_5
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

    def get_details(self):
        print('Implementing')
        selected = self.parent().location[self.title]
        selected.to_excel('output/detail.xlsx')
        

    def stop(self):
        self.hide()
    def start(self):
        self.parent().show()
        self.destroy()
        print('Working on it')
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        button_D = QPushButton('ShowDetails')
        button_R = QPushButton('<-- Return')
        #Add the return button in the end
        #Add show detail no matter what
        if self.parent() != None:
            layout.addWidget(button_R)
            layout.addWidget(button_D)
            button_R.clicked.connect(self.start)
        
        for i in self.location:
            if self.level < 5:
                button = QPushButton('{}\n\n#Claims:{}'.format(i, len(self.location[i])))
                layout.addWidget(button)
                if self.level  == 1:
                    search_loc = self.loc_2
                elif self.level == 2:
                    search_loc = self.loc_3
                elif self.level == 3:
                    search_loc = self.loc_4
                elif self.level == 4:
                    search_loc = self.loc_5

            else:
                print(self.level)
                button = QPushButton('<-- Return')
                button.clicked.connect(self.start)
                break
            button.clicked.connect(partial(buttonClicked, self.raw, self.c_f, i, search_loc, self.loc_2, self.loc_3, self.loc_4, self.loc_5, self.level, self.Top, self.title, self, self.stop))
        button_D.clicked.connect(self.get_details)
        self.horizontalGroupBox.setLayout(layout)
    # App = App(self.loc_2[top_loc], loc_1, loc_2, loc_3, loc_4)
    # sys.exit(App.exec_())

