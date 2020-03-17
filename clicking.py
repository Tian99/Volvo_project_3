import application
from generate import generate
import sys

def buttonClicked(raw, c_f, top_loc, next_loc_dic, loc_2, loc_3, loc_4, loc_5, level, Top, title, parent, stop):
    if level > 4:
        mkmsg('Reaching the end')
        # App.exec_()
    #Need to maintain the Top as always the loc_1
    print(top_loc)
    title = top_loc
    #Now we know that it's in the absolute top location
    if next_loc_dic == loc_2:
        Top = top_loc
    top_dic = generate(next_loc_dic[top_loc], raw, c_f, level , Top)
    print(next_loc_dic[top_loc])
    #Close the previous application
    stop()
    App = application.App(raw, c_f, top_dic, next_loc_dic, loc_2, loc_3, loc_4, loc_5, level, Top, title, parent, stop)
    App.exec_()