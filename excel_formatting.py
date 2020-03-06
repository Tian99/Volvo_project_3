import pandas as pd
from pandas import DataFrame as df


def split(content, lis):
	try:
		content = content.split("\\")
	except AttributeError:
		for i in range(0, len(lis)):
			lis[i].append('NULL')
		return lis
		
	#Just adjusting the format:
	content[0] = content[0][1:]
	for i in range(0, len(content)):
		lis[i].append(content[i])

	return lis

def format_assign(raw):
	d = {}
	count = 0
	lis = [[] for i in range(0, 7)]

	for index, row in raw.iterrows():
		content = row['AALNAMECONCATENATED']
		lis = split(content, lis)

		print(count/len(raw)*100)

		count += 1
	print('finish spliting')

	for i in range(1, len(lis)):
		 d["loc_{0}".format(i)]=lis[i]
	new = df(d)
	print('finish formatting')

	raw = pd.concat([raw, new], axis = 1)
	#Combine two columns 
	raw['loc_4+5'] = raw['loc_4'] + '\\' + raw['loc_5']
	print('finish assigning')

	#Sort the dataframe
	raw.sort_values(by=['PARTNO'], inplace=True)
	print('finish sorting')

	raw.drop_duplicates(subset=['PARTNO', 'AALNAMECONCATENATED'], keep=False, inplace = True)
	print('Duplicates dropped')

	return raw


