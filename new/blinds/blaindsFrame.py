from tkinter import Frame, Label
from .blaindController import BlaindController

class blaindsFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()

        s_label1 = Label(self, text="Storen EG", font = "Helvetica 10 bold")
        s_label1.pack()       

        BlaindController(self, 'Esszimmer', 'DIB_114', 'DIB_112', 'DIB_113', 'DIB_115')
        BlaindController(self, 'Küche', 'DIB_110', 'DIB_108', 'DIB_109', 'DIB_111')
        BlaindController(self, 'Wohnz. Links', 'DIB_106', 'DIB_104', 'DIB_105', 'DIB_107')
        BlaindController(self,'Wohnz. Rechts', 'DIB_102', 'DIB_100', 'DIB_101', 'DIB_103')