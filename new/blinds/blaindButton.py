from tkinter import Button
from helper.connection import Connection

class blaindButton(Button):
    def __init__(self, master, name, port):
        Button.__init__(self, master, text = name, width = 8, height = 3, command = self.buttonEvent)
        
        self.pack()

        self.port = port
        self.connection = Connection()
    
    def buttonEvent(self):
        print(self.port)
        self.connection.write(self.port)