from tkinter import Frame, Label
from .blaindButton import blaindButton

class BlaindController(Frame):
    def __init__(self, master, label='', serPortTop='', serPortUp='', serPortDown='', serPortButtom=''):
        Frame.__init__(self, master)
        self.pack()
        
        label = Label(self, text=label, font="Helvetica 20 bold")
        label.pack()
        
        blaindButton(self, '▲\n▲', serPortTop)
        blaindButton(self, '▲', serPortUp)
        blaindButton(self, '▼', serPortDown)
        blaindButton(self, '▼\n▼', serPortButtom)