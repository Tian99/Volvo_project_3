import os
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

def read(filename):
	data = pd.read_excel(filename)
	if 'Claims' in filename:
		data.to_pickle('input/claims.pkl')
	else:
		data.to_pickle('input/data.pkl')
	print('finish converting')

read('input/ALL - SR603 - W2008 (W20081).xlsx')
read('input/2019-12 Mack Claims.xlsx') 
