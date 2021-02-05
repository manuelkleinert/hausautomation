from tkinter import *

#Klasse Heizung -------------------------------------------------------------------
class Heizen:

    def H_Fenster1(self):                                                       #Funktion/Methode
        fenster = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
        fenster.title('Heizung')                                                #Titel des fensters definieren
        fenster.geometry('1920x1080')
        
        
        #Fenster-Inhalt definieren
        h_label1 = Label(fenster, text="Bedienung Heizung",font = "Helvetica 40 bold")
        h_label1.place(x=80,y=10)
        
        EG_Soll = Scale(fenster, from_=100, to=0)
        EG_Soll.place(x=300,y=60)
        
        Buero_Soll = Scale(fenster, from_=25.0, to=15.0)
        Buero_Soll.place(x=550,y=60)
        
        DG_Soll= Scale(fenster, from_=25.0, to=15.0)
        DG_Soll.place(x=800,y=60)
        
        #Werte Schieberregler ausgeben
        #def show_values():
        
        
        def button1():
            read = (EG_Soll.get() * 100)    #Gelesener Wert von 0..100% mal 100 da immer 2 Kommastellen inklusive
            header = str.encode('ASW_01_')
            wert=  str.encode(str(read))
            #end=  str.encode('_')
            message = header + wert
            print (message)
            ser.write(message)
        button1 = Button(fenster, text='Übern SW1',font = "Helvetica 24 bold",                                       
        width=8,height=3,bg= "grey",activebackground= "grey" ,command = button1)
        button1.place(x=250,y=250)
        
                
        def button2():          
            read = Buero_Soll.get()
            header = str.encode('ASW_02_')
            wert=  str.encode(str(read))
            #end=  str.encode('_')
            message = header + wert
            print (message)
            ser.write(message)
        button2 = Button(fenster, text='Übern SW2',font = "Helvetica 24 bold",                                       
        width=8,height=3,bg= "grey",activebackground= "grey" ,command = button2)
        button2.place(x=450,y=250)


        def button8():                                                   #Befehl für Home (fenster abbauen und schliessen)
            fenster.destroy()                                            #Fenster Abbauen
        button8 = Button(fenster, text='Home',font = "Helvetica 50 bold",                                       
        width=10,height=4,bg= "cyan",activebackground= "cyan" ,command = button8)
        button8.place(x=1400,y=650)
