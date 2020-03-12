import application
from generate import generate
import sys

def buttonClicked(raw, c_f, top_loc, next_loc_dic, loc_2, loc_3, loc_4, title):
    print(top_loc)
    title = top_loc
    top_dic = generate(next_loc_dic[top_loc], raw, c_f, top_loc)
    print(loc_2[top_loc])
    App = application.App(raw, c_f, top_dic, next_loc_dic, loc_2, loc_3, loc_4, title)
    App.exec_()