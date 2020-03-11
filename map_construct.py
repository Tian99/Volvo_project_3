import pandas as pd
from pandas import DataFrame as df

def construct(raw):
	big_map = {}
	location_2_c = {}
	location_3_c = {}
	location_4_c = {}
	location_5_c = {}
	#First get the instance of all the first level locations
	#Location_1 is a scam, starting with location_2
	location_1_c = raw['loc_2'].unique()
	every_2 = raw['loc_3'].unique()
	every_3 = raw['loc_4'].unique()
	every_4 = raw['loc_5'].unique()

	#This is aligned with the respect to the location above
	for i in location_1_c:
		location_2_c[i] = (raw.loc[raw['loc_2'] == i]['loc_3'].unique())

	for i in every_2:
		location_3_c[i] = (raw.loc[raw['loc_3'] == i]['loc_4'].unique())

	for i in every_3:
		location_4_c[i] = (raw.loc[raw['loc_4'] == i]['loc_5'].unique())

	for i in every_4:
		location_5_c[i] = (raw.loc[raw['loc_5'] == i]['loc_6'].unique())

	return [location_1_c, location_2_c, location_3_c, location_4_c, location_5_c]

	print(len(location_1_c))
	print(len(location_2_c))
	print(len(location_3_c))
	print(len(location_4_c))
	print(len(location_5_c))





