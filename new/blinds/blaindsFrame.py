from tkinter import Frame, Label
from .blaindController import BlaindController
from helper.titleFrame import TitleFrame

class blaindsFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()

        frameEg = TitleFrame(self, 'Storen EG')
        BlaindController(frameEg, 'Esszimmer', 'DIB_114', 'DIB_112', 'DIB_113', 'DIB_115')
        BlaindController(frameEg, 'Küche', 'DIB_110', 'DIB_108', 'DIB_109', 'DIB_111')
        BlaindController(frameEg, 'Wohnz. Links', 'DIB_106', 'DIB_104', 'DIB_105', 'DIB_107')
        BlaindController(frameEg,'Wohnz. Rechts', 'DIB_102', 'DIB_100', 'DIB_101', 'DIB_103')

        frameOg = TitleFrame(self, 'Storen OG / DG')
        BlaindController(frameOg, 'Eltern', 'DIB_16', 'DIB_14', 'DIB_15', 'DIB_17')
        BlaindController(frameOg, 'Zimmer Lina', 'DIB_12', 'DIB_10', 'DIB_11', 'DIB_13')
        BlaindController(frameOg, 'Zimmer Anic', 'DIB_306', 'DIB_304', 'DIB_305', 'DIB_307')
        BlaindController(frameOg,'Dachgesch.', 'DIB_302', 'DIB_300', 'DIB_301', 'DIB_303')