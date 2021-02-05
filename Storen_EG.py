#Klasse Storen Erdgeschoss -----------------------------------------------------------------------------------------------------------------------
#Stand 1.12.2020

#Klassen/Module Importieren
from tkinter import *
from StorenController import StorenController
from Storen_OG import Storen_OG



#Klasse
class Storen_EG:
    def __init__(self,serial):
        self.serial = serial  #übername schnittstelle von übergabewert
        

    def Fenster1(self):                                                         #Funktion/Methode
        fenster = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
        fenster.title('Storen EG')                                              #Titel des fensters definieren
        fenster.geometry('1920x1080')
        #fenster.geometry('1000x500')
              
                      
        #Fenster-Texte definieren
        s_label1 = Label(fenster, text="Storen EG",font = "Helvetica 25 bold")
        s_label1.place(x=230,y=5)
            
               
        #Storenbedieneinheiten für EG erzeugen
        #Info Übergabewerte: fenster,Serielle komm.,Position,Name,KDO Ganz Auf,KDO Auf,KDO Zu,KDO Ganz ZU
        StorenController(fenster, self.serial, 80, 120, 'Esszimmer', 'DIB_114', 'DIB_112', 'DIB_113', 'DIB_115')
        StorenController(fenster, self.serial, 380, 120, 'Küche', 'DIB_110', 'DIB_108', 'DIB_109', 'DIB_111')
        StorenController(fenster, self.serial, 80, 580, 'Wohnz. Links', 'DIB_106', 'DIB_104', 'DIB_105', 'DIB_107')
        StorenController(fenster, self.serial, 380, 580,'Wohnz. Rechts', 'DIB_102', 'DIB_100', 'DIB_101', 'DIB_103')

        
        #Storen Bedienung OG/DG Aufrufen-------------------------------
        def button17():                                                  #Befehl für Storen OG aufrufen
            storen_og = Storen_OG(self.serial)                           #Instanz der Klasse Storen OG erzeugen und Ser.-Schnittstelle übergeben
            storen_og.Fenster1()                                         #Instanz aufrufen
        button17 = Button(fenster, text='OG / DG',font= "Helvetica 20 bold",                                       
        width=8,height=1,bg= "light grey",activebackground= "sky blue",command = button17)
        button17.place(x=380,y=60)


        def button20():                                                  #Befehl für Home (fenster abbauen und schliessen)
            fenster.destroy()                                            #Fenster Abbauen
        button20 = Button(fenster, text='⬅',font = "Helvetica 20 bold",                                       
        width=8,height=1,bg= "light grey",activebackground= "sky blue",command = button20)
        button20.place(x=80,y=60)