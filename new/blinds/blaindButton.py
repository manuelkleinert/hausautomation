from tkinter import Button
from helper.serialConnection import SerialConnection

class blaindButton(Button):
    def __init__(self, master, name, port):
        Button.__init__(self, master, text = name, width = 8, height = 3, command = self.buttonEvent)
        
        self.pack()

        self.port = port
        self.connection = SerialConnection()
    
    def buttonEvent(self):
        self.connection.write(self.port)
        print(self.connection.read())