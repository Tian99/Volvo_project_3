from PyQt5 import QtWidgets


def mkmsg(msg, icon=QtWidgets.QMessageBox.Critical):
    """
    dialog box to send an error or warning message
    """
    # persistent to this function so not eaten by GC
    if not hasattr(mkmsg, 'win'):
        mkmsg.win = QtWidgets.QMessageBox()
    mkmsg.win.setIcon(icon)
    mkmsg.win.setText(msg)
    print("mkmsg: " + msg)
    mkmsg.win.show()

# def buffering_strip():
#     if not hasattr(mkmsg, 'win'):
#         mkmsg.win = QtWidgets.QMessageBox()
#     mkmsg.win.setText('0')
#     mkmsg.win.show()

