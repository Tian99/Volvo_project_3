import numpy as np
from Dutils import mkmsg

def generate(Chosen_locs, raw, c_f, level, Top):
        count = 0
        Selected_loc = {}
        if type(Chosen_locs) == np.ndarray:

            if level  == 1:
                search_loc = 'loc_3'
            elif level == 2:
                search_loc = 'loc_4'
            elif level == 3:
                search_loc = 'loc_5'
            elif level == 4:
                search_loc = 'loc_6'

            else:
                mkmsg('That is all the locations existed')
                return

            for current in Chosen_locs:
                #There are redudant part numbers in the file, dont know if thats a problem
                partno_collections = raw.loc[raw[search_loc] ==  current]['PARTNO']

                vehicle1 = 2 if 'Vehicle 2' in Top else 1

                for i in partno_collections:
                    if vehicle1 == 2:
                        length = len(c_f.loc[(c_f['Causal Part Number'] == str(i)) & (c_f['Vehicle Model Family'] == 'Mack Refuse')])
                    else:
                        length = len(c_f.loc[(c_f['Causal Part Number'] == str(i)) & (c_f['Vehicle Model Family'] != 'Mack Refuse')])
                    count += length

                    print(i)
                    print('==================================')
                    print(count)

                Selected_loc[current] = count
                #Remember to refresh the count
                count = 0
            print(Selected_loc)
            return Selected_loc

        else:

            for index in range(Chosen_locs.count()):
                print(index)
                current = Chosen_locs.item(index).text()
                #There are redudant part numbers in the file, dont know if thats a problem
                partno_collections = raw.loc[raw['loc_2'] ==  current]['PARTNO']

                vehicle1 = 2 if 'Vehicle 2' in current else 1

                for i in partno_collections:
                    if vehicle1 == 2:
                        length = len(c_f.loc[(c_f['Causal Part Number'] == str(i)) & (c_f['Vehicle Model Family'] == 'Mack Refuse')])
                    else:
                        length = len(c_f.loc[(c_f['Causal Part Number'] == str(i)) & (c_f['Vehicle Model Family'] != 'Mack Refuse')])
                    count += length

                    print(i)
                    print('==================================')
                    print(count)

                Selected_loc[current] = count
                #Remember to refresh the count
                count = 0
                print(Selected_loc)
                #Need to keep track of the absolute first location to deal with vehicle 1 and vehicle 2 
            return Selected_loc