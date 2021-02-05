from tkinter import *
from StorenButton import StorenButton

#Klasse Storen Controller (Bedieneinheit für eine Store)-------------------------------------------------------
class StorenController:
    def __init__(self, window, serial, x, y, label, serPortTop, serPortUp, serPortDown, serPortButtom):
        
        label = Label(window, text=label,font="Helvetica 20 bold")
        label.place(x=x,y=y)
        
        StorenButton(window, serial,'▲\n▲',x,y+40,serPortTop)   #Einzelne Storentaster aus Klasse Button erzeugen
        StorenButton(window, serial, '▲', x,y+140, serPortUp)
        StorenButton(window, serial, '▼', x,y+240, serPortDown)
        StorenButton(window, serial, '▼\n▼', x,y+340, serPortButtom)