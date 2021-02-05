from tkinter import *

#import serial

#Klasse Storen Teil1 -----------------------------------------------------------------------------------------------------------------------
class StorenButton:
    width=8
    height=3
    color="light grey"
    font="Helvetica 20 bold"
        
    def __init__(self,window, serial, name, x, y, serialCode):
        self.window = window
        self.serial= serial
        self.name = name
        self.posX = x
        self.posY = y
        self.serialCode = serialCode
        self.setButton()
        
    def setButton(self):
        button = Button(self.window, text=self.name, font=self.font,
                         width=self.width, height=self.height, bg=self.color, activebackground=self.color, command=self.buttonEvent)
        button.place(x=self.posX, y=self.posY)
        
    def buttonEvent(self):
        self.serial.write(str.encode(self.serialCode))
        