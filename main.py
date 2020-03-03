import sys
import pandas as pd
from pandas import DataFrame as df
from map_construct import construct
from excel_formatting import format_assign
# from PyQt5 import uic, QtCore, QtGui, QtWidgets

class Map(QtWidgets.QMainWindow):
	def __init__(self):

		super().__init__()

		#Later could change it to a drop box
		print('start reading excel file')
		raw = pd.read_excel('input/ALL - SR603 - W2008 (W20081).xlsx')
		print('finished reading excel')

		#First change the formatting of the excel file
		raw = format_assign(raw)
		print('Finished formatting')

		loc_collections = construct(raw)
		print('Finished constructing')

		uic.loadUi('./ui/MainWindow.ui', self)


#The code download called everything
if __name__ == '__main__':

	APP = QtWidgets.QApplication([])

	if len(sys.argv) > 1:
		WINDOW = Map(config_file=sys.argv[1])
	else:
		WINDOW = Map()

	WINDOW.show()
	sys.exit(APP.exec_())