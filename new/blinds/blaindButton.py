from tkinter import Button
from helper.SerialConnection import SerialConnection

class blaindButton(Button):
    def __init__(self, master, name, port):
        Button.__init__(self, master, text = name, command = self.buttonEvent)
        self.pack()

        self.port = port
        self.connection = SerialConnection()

    
    def buttonEvent(self):
        self.connection.write(self.port)