import os
import sys
import time
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

		uic.loadUi('./ui/MainWindow.ui', self)
		self.setWindowTitle('Main')
		self.Compile.clicked.connect(self.file_input)
		# #Later could change it to a drop box
		# raw = pd.read_pickle('input/data.pkl')
		# print('finished reading pickle')

		# #First change the formatting of the excel file
		# raw = format_assign(raw)
		# print('Finished formatting')

		# loc_collections = construct(raw)
		# print('Finished constructing')

		self.show()

	def file_input(self):
		address = self.Address.text()
		print(type(address))
		#Check if the file exists
		if path.exists(address):
			print('File scan successfully')
			try:
				f = pd.read_pickle(address)
			except ModuleNotFoundError:
				mkmsg('Wrong format')
				return
		else:
			print(address)
			mkmsg('No such file existed, try again')
			return
		#Starting formatting the file
		raw = format_assign(f)


#The code download called everything
if __name__ == '__main__':

	APP = QtWidgets.QApplication([])

	if len(sys.argv) > 1:
		WINDOW = Map(config_file=sys.argv[1])
	else:
		WINDOW = Map()

	sys.exit(APP.exec_())