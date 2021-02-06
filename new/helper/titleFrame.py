from tkinter import Tk, Frame, Label, LEFT, GROOVE, NW, W

class TitleFrame(Frame):
    def __init__(self, master, title):
        frame = Frame(master)
        Frame.__init__(self, frame, relief = GROOVE, borderwidth = 2)

        Label(frame, text = title).place(relx = 0.04, rely = .05, anchor = W)

        self.pack(side = LEFT, anchor = NW, padx = 10, pady = 16)
        frame.pack(side = LEFT, anchor = NW)