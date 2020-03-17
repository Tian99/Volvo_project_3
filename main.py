import os
import sys
import time
import application
from os import path
import pandas as pd
from Dutils import mkmsg
from pandas import DataFrame as df
from generate import generate
from map_construct import construct
from excel_formatting import format_assign
from PyQt5 import uic, QtCore, QtGui, QtWidgets

class Map(QtWidgets.QMainWindow):
	def __init__(self):

		super().__init__()
		#Define the variable
		self.f = None
		self.c_f = None
		self.merged = None
		uic.loadUi('./ui/MainWindow.ui', self)
		self.setWindowTitle('Main')
		self.Address.textChanged.connect(self.enable)
		self.Claim_address.textChanged.connect(self.enable)
		self.Compile.clicked.connect(self.disable)
		self.Compile.clicked.connect(self.file_input)
		self.Generate.clicked.connect(self.visualization)
		self.All_locs.itemClicked.connect(self.add_task)
		self.Chosen_locs.itemClicked.connect(self.remove_task)

		self.show()

	#May change something later when it runs on windows 
	def file_input(self):
		address = self.Address.text()
		claim_address = self.Claim_address.text()
		print(type(address))
		#Check if the file exists
		if path.exists(address) and path.exists(claim_address):
			print('File scan successfully')
			try:
				self.f = pd.read_pickle(address)
				self.c_f = pd.read_pickle(claim_address)
			except ModuleNotFoundError:
				mkmsg('Wrong format')
				return
		else:
			print(address)
			print(claim_address)
			mkmsg('No such file existed, try again')
			return
		#Starting formatting the file
		try:
			self.raw = pd.read_pickle("input/raw.pkl")
			# Do something with the file
		except IOError:
			print("Creating new file")
			self.raw = format_assign(self.f)
			print("Writing file to input")
			self.raw.to_pickle('input/raw.pkl')
		#Construct the map
		loc_collections = construct(self.raw)

		self.loc_1 = loc_collections[0]
		self.loc_2 = loc_collections[1]
		self.loc_3 = loc_collections[2]
		self.loc_4 = loc_collections[3]
		self.loc_5 = loc_collections[4]
		print('locations separated')

		self.loc_chosen()

	def visualization(self):
		#Level is usued to keep track of which location we are currently on
		"""
		level 1 --> loc_1, so on and so forth
		"""
		level = 0
		Selected_loc = generate(self.Chosen_locs, self.raw, self.c_f, level, Top=None)
		#Get all the partnumber from the selected_loc
		App = application.App(self.raw, self.c_f, Selected_loc, self.loc_1, self.loc_2, self.loc_3, self.loc_4, self.loc_5, level, Top = None, title = 'Root', parent = None)
		App.exec_()
		#Match the locations with the claim

	def enable(self):
		self.Compile.setDisabled(False)

	def disable(self):
		self.Compile.setDisabled(True)

	def loc_chosen(self):
		for i in self.loc_1:
			print(i)
			if i != 'NULL':
				self.All_locs.addItem(i)

	def add_task(self, item):
		print("add task %s" % item.text())
		rowi = self.All_locs.row(item)
		self.All_locs.takeItem(rowi)
		self.Chosen_locs.addItem(item.text())

	def remove_task(self, item):
		print("add task %s" % item.text())
		rowi = self.Chosen_locs.row(item)
		self.Chosen_locs.takeItem(rowi)
		self.All_locs.addItem(item.text())

#The code download called everything
if __name__ == '__main__':

	APP = QtWidgets.QApplication([])

	if len(sys.argv) > 1:
		WINDOW = Map(config_file=sys.argv[1])
	else:
		WINDOW = Map()

	sys.exit(APP.exec_())