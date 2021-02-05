from tkinter import Frame
from .blaindController import BlaindController

class blaindsFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()

        BlaindController(self, 'demo')