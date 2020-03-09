def general_filtering(data):
	###################
	#First Level filtering
	#FIlter out the American side data
	data = data.loc[data['Vehicle Assembly Final Plant Code-Description'] == 'MT_93']
	
	return data