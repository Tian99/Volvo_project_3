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
		self.raw = None
		self.merged = None
		uic.loadUi('./ui/MainWindow.ui', self)
		self.setWindowTitle('Main')
		self.Address.textChanged.connect(self.enable)
		self.Address.textChanged.connect(self.disable_generate)
		self.Claim_address.textChanged.connect(self.enable)
		self.Claim_address.textChanged.connect(self.disable_generate)
		self.time.textChanged.connect(self.enable)
		self.time.textChanged.connect(self.disable_generate)
		self.Compile.clicked.connect(self.disable)
		self.Compile.clicked.connect(self.file_input)
		self.Compile.clicked.connect(self.enable_generate)
		self.Generate.clicked.connect(self.visualization)
		self.All_locs.itemClicked.connect(self.add_task)
		self.Chosen_locs.itemClicked.connect(self.remove_task)

		self.show()

	#May change something later when it runs on windows 
	def file_input(self):
		self.Generate.setDisabled(False)
		address = self.Address.text()
		claim_address = self.Claim_address.text()
		time = self.time.text()
		print(type(address))
		self.All_locs.clear()
		self.Chosen_locs.clear()
		#Check if the file exists
		if path.exists(address) and path.exists(claim_address):
			print('File scan successfully')
			try:
				self.f = pd.read_pickle(address)
				self.c_f = pd.read_pickle(claim_address)
			except ModuleNotFoundError:
				mkmsg('Wrong format')
				return
			#Change the time zone
			if 'YYYY' in self.time.text():
				print('Nothing entered')
				low = self.c_f['Vehicle Assembly Date'].min().date()
				high = self.c_f['Vehicle Assembly Date'].max().date()
				text = str(low).replace('-','/')+':'+str(high).replace('-','/')

				print(low)
				print(high)
				self.time.setText(text)
			else: 
				trange = self.time.text()
				print(trange)
				low = trange.split(':')[0]
				high = trange.split(':')[1]
				#Change the current file to the updated file
				mask = (self.c_f['Vehicle Assembly Date'] >= low) & (self.c_f['Vehicle Assembly Date'] <= high)
				self.c_f = self.c_f.loc[mask]
		else:
			print(address)
			print(claim_address)
			mkmsg('No such file existed, try again')
			return
		self.raw = format_assign(self.f)
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
		
	def enable_generate(self):
		self.Generate.setDisabled(False)

	def disable_generate(self):
		self.Generate.setDisabled(True)

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