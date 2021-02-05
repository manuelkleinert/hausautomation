from tkinter import *

#Klasse System -------------------------------------------------------------------------------------------------------------
class System:
    
    def S_Fenster1(self):                                            #Funktion/Methode
        fenster = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
        fenster.title('System')                                   #Titel des fensters definieren
        fenster.geometry('1920x1080')
        
        #Fenster-Inhalt definieren
        sy_label1 = Label(fenster, text="System",font = "Helvetica 40 bold")
        sy_label1.place(x=80,y=10)
     
              
#         global input_b0                         #Test dem button 15 eine Farbe zuzuweisen nach aktivierung
#         if  input_b0 == 1:
#             color = "red"
#         else:
#             color = "light grey"

        def button15():                                                      #Befehl für aktivierung notbedienung
            ser.write(str.encode('39_'))
        button15 = Button(fenster, text='Notbed. Ein!',font = "Helvetica 16 bold",
                        width=10,height=1,bg="cyan" ,command = button15)       
        button15.place(x=25,y=130)

        def button16():                                                      #Befehl für deaktivierung notbedienung
            ser.write(str.encode('40_'))
        button16 = Button(fenster, text='Notbed. Aus',font = "Helvetica 16 bold",
        width=10,height=1,bg= "green",activebackground= "green" ,command = button16)       
        button16.place(x=25,y=190)
        
        def button20():                                                     #Befehl für Home (fenster abbauen und schliessen)                                                
            fenster.destroy()                                              #Fenster Abbauen
        button20 = Button(fenster, text='Home',font = "Helvetica 50 bold",                                       
        width=10,height=4,bg= "cyan",activebackground= "cyan",command = button20)
        button20.place(x=1400,y=650)
