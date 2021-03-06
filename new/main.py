from tkinter import Tk, Frame, Label
from helper.taps import Taps
from blinds.blaindsFrame import blaindsFrame
from temperature.db import Db
from temperature.statisticFrame import StatisticFrame

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        
        master.title('Temperature Statistics')
        
        # Tutorial Add a new Temperature
        self.db = Db()
        
        # Template add new Station
        # self.db.addStation('Garten')
        
        # Template add temperature
        # self.db.addTemperature(1, 24.25)
        
        # Create new Tapbar
        tabs = Taps(self)
        
        # Add home Tap
        tapHome = tabs.addTap('Home Controlls')
        homeText = Label(tapHome, text="Home Content")
        homeText.pack()

        # Add blinds Tap
        tabs.addTap('Storen', blaindsFrame())
        
        # Add Temperature Tap
        tabs.addTap('Temperature Statistics', StatisticFrame())

app = Application(Tk())
app.mainloop()
