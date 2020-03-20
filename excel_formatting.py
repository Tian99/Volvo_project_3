import pandas as pd
from pandas import DataFrame as df


def split_acc(raw):
	raw[['index', 'loc_1', 'loc_2', 'loc_3', 'loc_4', 'loc_5', 'loc_6']] = raw['AALNAMECONCATENATED'].str.split('\\', expand = True)
	return raw

def format_assign(raw):
	d = {}
	count = 0
	print('Start Spliting')
	raw = split_acc(raw)

	print('finish spliting')

	raw.drop_duplicates(subset=['PARTNO', 'AALNAMECONCATENATED'], keep = False, inplace = True)
	print('Duplicates dropped')

	return raw


