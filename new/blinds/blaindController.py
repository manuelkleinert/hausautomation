from tkinter import Frame, Label, TOP, LEFT, N, NW
from .blaindButton import blaindButton

class BlaindController(Frame):
    def __init__(self, master, label='', serPortTop='', serPortUp='', serPortDown='', serPortButtom=''):
        Frame.__init__(self, master)
        
        label = Label(self, text=label, font="Helvetica 10 bold")
        label.pack(side=TOP, anchor=N)
        
        blaindButton(self, '▲\n▲', serPortTop)
        blaindButton(self, '▲', serPortUp)
        blaindButton(self, '▼', serPortDown)
        blaindButton(self, '▼\n▼', serPortButtom)

        self.pack(side = LEFT, anchor = NW, padx = 10, pady = 15)