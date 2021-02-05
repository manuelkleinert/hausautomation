#Klasse Storen Obergeschoss/Dachgeschoss ------------------------------------------------------------------------------
#Stand 1.12.2020

#Klassen/Module Importieren
from tkinter import *
from StorenController import StorenController


#Klasse
class Storen_OG:
    def __init__(self,serial):
        self.serial = serial
        

    def Fenster1(self):                                                         #Funktion/Methode
        fenster = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
        fenster.title('Storen OG + DG')                                         #Titel des fensters definieren
        fenster.geometry('1920x1080')
        #fenster.geometry('1000x500')
              
        
        #Fenster-Texte definieren
        s_label1 = Label(fenster, text="Storen OG + DG",font = "Helvetica 25 bold")
        s_label1.place(x=200,y=5)
            
               
        #Storenbedieneinheiten für OG und DG erzeugen
        #Info Übergabewerte: fenster,Serielle komm.,Position,Name,KDO Ganz Auf,KDO Auf,KDO Zu,KDO Ganz ZU
        StorenController(fenster, self.serial, 80, 120, 'Eltern', 'DIB_16', 'DIB_14', 'DIB_15', 'DIB_17')
        StorenController(fenster, self.serial, 380, 120, 'Zimmer Lina', 'DIB_12', 'DIB_10', 'DIB_11', 'DIB_13')
        StorenController(fenster, self.serial, 80, 580, 'Zimmer Anic', 'DIB_306', 'DIB_304', 'DIB_305', 'DIB_307')
        StorenController(fenster, self.serial, 380, 580,'Dachgesch.', 'DIB_302', 'DIB_300', 'DIB_301', 'DIB_303')

        
#         #Storen Bedienung .... Aufrufen-------------------------------
#         def button1():                                                  #Befehl für Storen OG aufrufen
#             storen_og = Storen_OG()                                      #Instanz der klasse Storen OG erzeugen
#             storen_og.Fenster1()                                         #Instanz aufrufen
#         button1 = Button(fenster, text='OG / DG',font= "Helvetica 20 bold",                                       
#         width=8,height=1,bg= "light grey",activebackground= "sky blue",command = button1)
#         button1.place(x=380,y=60)


        def button2():                                                  #Befehl für Home (fenster abbauen und schliessen)
            fenster.destroy()                                            #Fenster Abbauen
        button2 = Button(fenster, text='⬅',font = "Helvetica 20 bold",                                       
        width=8,height=1,bg= "light grey",activebackground= "sky blue",command = button2)
        button2.place(x=80,y=60)


