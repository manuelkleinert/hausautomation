from tkinter import LEFT, BOTH
from tkinter.ttk import Notebook, Frame

class Taps(Notebook):
    '''
    Taps classe inherit tk notebook
    Create a Tapbar and add new taps
    '''
    def __init__(self, *args):
        Notebook.__init__(self, *args)
        self.pack(expand = True, fill = BOTH)

    def addTap(self, title, tapFrame = None):
        '''
        Add new tap
        :param title: String, set tap title
        :param tapFrame: Frame, add your content Frame (optional)
        '''

        if not tapFrame:
            tapFrame = Frame(self)
            tapFrame.pack(side = LEFT, fill = BOTH, expand = True)
            
        self.add(tapFrame, text = title)
        return tapFrame