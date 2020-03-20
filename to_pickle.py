import os
from filter import general_filtering
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

def read(filename):
	data = pd.read_excel(filename)
	if 'Claims' in filename:
		data = general_filtering(data)
		data.to_pickle('input/claims.pkl')
	else:
		data.to_pickle('input/data.pkl')
	print('finish converting')

read('input/locations.xlsx')
read('input/claims.xlsx') 
