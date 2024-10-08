# import tkinter as tk
# from model import patient
#
# window = tk.Tk()
# window.geometry("500x500")
# window.title("Python Hospital App")
# myLabel = tk.Label(window, text="Hospital App")
# myLabel.pack()
#
# tk.mainloop()
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

from guibuilder import component

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = component.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    component.start_up()
