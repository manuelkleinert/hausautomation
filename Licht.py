from tkinter import *

class Licht:


##            ##  #Test ausgabe counter
##    #counter = 0 
##    def counter_label(label1):
##         label1 = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
##        test_label = Label(label1, text="Jupee",font = "Helvetica 20 bold")
##        test_label.place(x=10,y=120)                                                       
##          def count():
##            global counter
##            counter += 1
##            #label.place(x=100,y=120)
##            label.config(text=str(counter))
##            label.after(1000, count)
##          count()

    def L_Fenster1(self):                                              #Funktion/Methode
        fenster = Toplevel()                                                    #Zusatz Fenster erzeugen mit bef. toplevel
        fenster.title('Licht')                                                      #Titel des fensters definieren
        fenster.geometry('1920x1080')
        
        #Fenster-Inhalt definieren
        l_label1 = Label(fenster, text="Bedienung Licht",font = "Helvetica 40 bold")
        l_label1.place(x=80,y=10)
        
        w = Scale(fenster, from_=100, to=20)
        w.pack()
        w = Scale(fenster, from_=20, to=100)
        w.pack()

        def button8():                                                      #Befehl für Home (fenster abbauen und schliessen)
            fenster.destroy()                                            #Fenster Abbauen
        button8 = Button(fenster, text='Home',font = "Helvetica 50 bold",                                       
        width=10,height=4,bg= "cyan",activebackground= "cyan" ,command = button8)
        button8.place(x=1400,y=650)