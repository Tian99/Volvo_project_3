import os
import sys
import time
import application
from os import path
import pandas as pd
from Dutils import mkmsg
from pandas import DataFrame as df
from map_construct import construct
from excel_formatting import format_assign
from PyQt5 import uic, QtCore, QtGui, QtWidgets

class Map(QtWidgets.QMainWindow):
	def __init__(self):

		super().__init__()
		#Define the variable
		self.Selected_loc = {}
		self.f = None
		self.c_f = None
		self.merged = None
		uic.loadUi('./ui/MainWindow.ui', self)
		self.setWindowTitle('Main')
		self.Address.textChanged.connect(self.enable)
		self.Claim_address.textChanged.connect(self.enable)
		self.Compile.clicked.connect(self.disable)
		self.Compile.clicked.connect(self.file_input)
		self.Generate.clicked.connect(self.generate)
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

	def generate(self):
		count = 0
		self.Selected_loc.clear()
		for index in range(self.Chosen_locs.count()):
			print(index)
			current = self.Chosen_locs.item(index).text()
			#There are redudant part numbers in the file, dont know if thats a problem
			partno_collections = self.raw.loc[self.raw['loc_2'] ==  current]['PARTNO']

			vehicle1 = 2 if 'Vehicle 2' in current else 1

			for i in partno_collections:
				if vehicle1 == 2:
					length = len(self.c_f.loc[(self.c_f['Causal Part Number'] == str(i)) & (self.c_f['Vehicle Model Family'] == 'Mack Refuse')])
				else:
					length = len(self.c_f.loc[(self.c_f['Causal Part Number'] == str(i)) & (self.c_f['Vehicle Model Family'] != 'Mack Refuse')])
				count += length

				print(i)
				print('==================================')
				print(count)

			self.Selected_loc[current] = count
			#Remember to refresh the count
			count = 0

		print(self.Selected_loc)
		#Get all the partnumber from the selected_loc
		self.App = application.App(self.Selected_loc, self.loc_1)
		sys.exit(self.App.exec_())
		#Match the locations with the claim
		exit()

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