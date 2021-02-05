#Hausautomation Laubacher by Serge


#Version A1
#Kls 10.11.2019 erstes grafisches Panel auf Basis büssliküche umgebaut auf Python Version 3
#Kls 11.11.2019 Kommunikation empfang integer und bool läuft nun stabil
#Kls 25.08.2020 4 Storen gemacht Kommando werte aber noch mit Arduino abstimmen
#Version A2
#Kls und Manuel 23.10.2020 Klassen in eigenen Files erstellt und Storenbutton sauber gegliedert
#Version A3
#Kls 30.12.2020 Klassen Storen OG-DG erstellt

#################################################################################################################
#****************************************-------Initialisieren----------************************************************
#********************************************************************************************************************


#Info durch den Tkinter import mit import*  anstelle "import TKinter as tk" können die Grafikelemnte
#überall verwendet werden und ie Funktionen wie Button werden direkt erkennt. also nicht mit tk.Button

#Funktionen Importieren -------------------------------------------
import serial
from tkinter import *  #Grafikoberfläche TKinter importieren  //Achtung ab Pyhton 3.0 tkinter kleinschreiben sonst gross Tkinter!!!
from tkinter.filedialog import askopenfilename #Menübalken       /Achtung ab Python 3.0 tkinter.filedialog vorher tkfiledialog


#klassen (eigene Programm-Unterteile) importieren
#import class_storenbedienung   #Klasse importieren
from Storen_EG import Storen_EG
from Storen_OG import Storen_OG
from Heizen import Heizen
from Licht import Licht
from System import System

#Serialle Verbindung mit Arduino aufbauen ------------------------------
#Versuch über schnitstelle 0 oder allenfalls 1 die Verbindung aufzubauen
#timeout 0 verhindert das blockieren des Programms Sehr Wichtig!!!!!!
try: ser = serial.Serial('/dev/ttyACM0',9600,timeout=0)
except  serial.SerialException:
    ser = serial.Serial('/dev/ttyACM1',9600,timeout=0)
        



#****************************************-------Klassen----------****************************************************
#********************************************************************************************************************


#***************--------Methode zum Einlesen der Daten ab Seriell-Kommunikation---------****************
def empfangen():
    #Lokale Variablen definieren
    empfangsfach_i = 16  #Groesse des Empfangsfaches für integer Werte
    empfangsfach_b = 32 #Groesse des Empfangsfaches für Bool Werte
    input_i_array =([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])  #Input Array muss grösse von empfangsfach haben
    input_b_array =([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) #Input Array muss grösse von empfangsfach haben
    count_array = 0
    count_array_b = 0
    input_ser = " "

    #die Globalen Variablen müssen in der Methode erneut angegeben werden
    global input_i0, input_i1, input_i2, input_i3, input_i4,  input_i5,  input_i6,  input_i7   #Integer Werte
    global input_i8, input_i9, input_i10, input_i11, input_i12, input_i13, input_i14, input_i15
     
    global input_b0, input_b1,  input_b2, input_b3, input_b4, input_b5, input_b6, input_b7                #Binär Werte
    global input_b8, input_b9, input_b10, input_b11, input_b12, input_b13, input_b14, input_b15
    global input_b16, input_b17, input_b18, input_b19, input_b20, input_b21, input_b22, input_b23
    global input_b24, input_b25, input_b26, input_b27, input_b28, input_b29, input_b30, input_b31

    global gelesen #Merken dass Daten empfangen wurden

    
#daten lesen---------------------------------------------------------------------------------------------------------------
#     if gelesen == 0:        #Beim ersten start dem arduino mitteilen dass er daten senden soll
#         ser.write(str.encode('ASW_99_'))
#         print('ASW_99_')
#         gelesen = 1         

    

    #Daten von Serieller Schnittstelle von Arduino lesen
    input_ser = ser.readline()
    if len(input_ser) >0:              #Daten nur Abfragen wenn Serielle schnittstelle minimum z.b. 20 werte beinhaltet
        #print("receve_data")
        input_all = input_ser.strip(str.encode(",\r\n"))    #Koma und Enter Werte aus String entfernen (Filter)
        #print(input_all)

        #Integer lesen
        erkennung = (str.encode("SendAnalog"))       
        if input_all == erkennung:                 #Erkennung dass Integer Werte kommen
            analog_ok=0                              #Kontrovariable für setzen der Werte nach erfolgreichem lesen
            #ser.write(str.encode('ASW_99_'))          #An Arduino melden dass er nächste Telegramme senden darf Code ASW_99_
                                                    #vermutlich nicht mehr nötig da Raspi 4 sehr schnell ist, bremst nur
                       
            for counter in range(0,empfangsfach_i): #Schlaufe durchlaufen so lange bis Empfangsfachgrösse erreicht
                input_all = ser.readline()                                 
                input_filter = input_all.strip(str.encode(",\r\n"))    #Koma und Enter Werte aus String entfernen (Filter)
                if len(input_filter) >0 and (input_filter != (b'-')):  #Neue Anpassung Raspi4 offenbar so schnell dass Puffer geleert wird da Arduino langsamer sendet
                                                                       #Deshalb hier jeweils nochmal prüfen ob Daten schon in Empfangsfach sind                            
                                                                       #und auch nicht erst ein "-" vorzeichen im puffer von einer neg-Zahl ist
                    input_i = float(input_filter)
                    #print (input_i)
                    input_i_array [count_array] = input_i
                    count_array = count_array+1
                    if (count_array == empfangsfach_i):
                        analog_ok=1
                        
            #Daten auf Globale variabel schreiben   Werte werden nur geschrieben wenn alle sauber empfangen wurden    
            if (analog_ok):
                #print ("analog_ok")
                input_i0 = input_i_array[0]  #Anzeige Sekunden seit start Arduino UV
                input_i1 = input_i_array[1]  #Längste Zykluszeit Arduino UV
                input_i2 = input_i_array[2]  #Heizungsstufe anhand Regulierung
                input_i3 = input_i_array[3]  #Schieber Ist-Stellung in % des Haupt-Heizungsschiebers
                input_i4 = input_i_array[4]  #Restzeit bis Heizungsregler die Heizstufe erneut festlegt
                input_i5 = input_i_array[5]  #Trendwert Tempdiff zu leztem gespecherten h-Wert
                input_i6 = input_i_array[6]  #Fortlaufender h-Mittelwert Temp. Wohnzimmer
                input_i7 = input_i_array[7]  #Temperatur Wohnzimmer
                input_i8 = input_i_array[8]  #Feuchtigkeit Wohnzimmer
                input_i9 = input_i_array[9]  #Temperatur Garten-Kellerraum
                input_i10 = input_i_array[10]  #Anzeige Sekunden seit start Arduino EG
                input_i11 = input_i_array[11]  #Längste Zykluszeit Arduino EG
                input_i12 = input_i_array[12]  #Anzeige Sekunden seit start Arduino DG
                input_i13 = input_i_array[13]  #Längste Zykluszeit Arduino DG
                input_i14 = input_i_array[14]  #Temperatur DG
                input_i15 = input_i_array[15]  #Feuchtigkeit DG
                
                                #Input von Arduino in Serieller ausgabe Darstellen (für Diagnosezwecke) Macht alles langsam!
                diagnose = 0  # Diagnose ein oder ausschalten
                if diagnose ==1:
                    print ("Analog Inputs:")
                    print (input_i_array)
    
        #Daten von Serieller Schnittstelle von Arduino lesen
        input_all_b = input_ser.strip(str.encode(",\r\n"))    #Koma und Enter Werte aus String entfernen (Filter)
        
        #Daten von Serieller Schnittstelle von Arduino lesen
        erkennung_b = (str.encode("SendDigital"))
        #print (erkennung)
        if input_all_b == erkennung_b:   #Erkennung dass Integer Werte kommen
            digital_ok=0               #Kontrovariable für setzen der Werte nach erfolgreichem lesen
            #print("receve_digital")
            
            for counter in range(0,empfangsfach_b): #Schlaufe durchlaufen so lange bis Empfangsfachgrösse erreicht
                input_all_b = ser.read(2)                                 #read(2) für 2 Zeichen damit auch "," eingelesen wird
                input_filter_b = input_all_b.strip(str.encode(","))       #Koma aus String entfernen (Filter)
                #print (input_filter_b)
                if len(input_filter_b) >0 and ((input_filter_b == (b'1') or input_filter_b == (b'0'))):  #Neue Anpassung Raspi4 offenbar so schnell dass Puffer geleert wird da Arduino langsamer sendet
                                                                              #Deshalb hier jeweils nochmal prüfen ob Daten schon in Empfangsfach sind                            
                                                                              #und zulässig sind
                    input_b = int(input_filter_b)
                    #print (input_b)
                    input_b_array [count_array_b] = input_b
                    count_array_b = count_array_b+1
                    if (count_array_b == empfangsfach_b):
                        digital_ok=1
                
            #Daten auf Globale variabel schreiben   Werte werden nur geschrieben wenn alle sauber empfangen wurden    
            if (digital_ok):
                #print ("digital_ok")                
                #Daten auf Globale variabel schreiben
                input_b0 = input_b_array[0]  #Binärwert0
                input_b1 = input_b_array[1]  #Binärwert1
                input_b2 = input_b_array[2]  
                input_b3 = input_b_array[3]  
                input_b4 = input_b_array[4]  
                input_b5 = input_b_array[5]  
                input_b6 = input_b_array[6]  
                input_b7 = input_b_array[7]  
                input_b8 = input_b_array[8]  
                input_b9 = input_b_array[9]  
                input_b10 = input_b_array[10]  
                input_b11 = input_b_array[11]  
                input_b12 = input_b_array[12]  
                input_b13 = input_b_array[13]  
                input_b14 = input_b_array[14]
                input_b15 = input_b_array[15]
                input_b16 = input_b_array[16]
                input_b17 = input_b_array[17]
                input_b18 = input_b_array[18]
                input_b19 = input_b_array[19]
                input_b20 = input_b_array[20]
                input_b21 = input_b_array[21]
                input_b22 = input_b_array[22]
                input_b23 = input_b_array[23]
                input_b24 = input_b_array[24]
                input_b25 = input_b_array[25]
                input_b26 = input_b_array[26]
                input_b27 = input_b_array[27]
                input_b28 = input_b_array[28]
                input_b29 = input_b_array[29]
                input_b30 = input_b_array[30]
                input_b31 = input_b_array[31]
                

                #Input von Arduino in Serieller ausgabe Darstellen (für Diagnosezwecke) Macht alles langsam!
                diagnose = 0  # Diagnose ein oder ausschalten
                if diagnose ==1:
                    print ("Digital Inputs:")
                    print (input_b_array)
 
    root.after(200,empfangen) #aufrufintervall in xx ms (alle 200ms aufrufen)
    #Intervall schneller als Arduino machen damit neuste Daten immer vorhanden sind
    

#***************--------Methode für Dynamische Label im Hauptfenster---------***************************************
def ausgabe_label(label):
    def count():
        global counter
        counter += 1
        label.config(text="Counter: " + str(counter))
        label.after(UPDATE_INTERVALL, count)
    count()

def ausgabe_label1(lab0,lab1,lab2,lab3,lab4,lab5,lab6,lab7,lab8,lab9,lab10,lab11,lab12,lab13,lab14,lab15,): #Label wird 1x übergeben
    def ausgabe():                   #Untermethode ohne übergabewert die im Intervall aufgerufen wird
        lab0.config(text="Sekunden UV: " + str(input_i0))
        lab1.config(text="Max.Zyklusz./min UV: " +str(input_i1))
        lab2.config(text="Heizstufe: " + str(input_i2))
        lab3.config(text="Heizungsschieber Stellung: " + str(input_i3)+"%")
        lab4.config(text="Restzeit bis Regelanpassung: " + str(input_i4)+"min")
        lab5.config(text="Trendwert Heizung: " + str(input_i5/10)+"°C")
        lab6.config(text="h-Mittelwert Wohnzimmertemp: " + str(input_i6/10)+"°C")
        lab7.config(text="Wohnen Temp.: " + str(input_i7/10)+"°C")
        lab8.config(text="F: " + str(input_i8/10)+"%")
        lab9.config(text="Gartenkeller Temp.: " +str(input_i9/10)+"°C")
        lab10.config(text="Sekunden EG: " + str(input_i10))
        lab11.config(text="Max.Zyklusz./min EG: " + str(input_i11))
        lab12.config(text="Sekunden DG: " + str(input_i12))
        lab13.config(text="Max.Zyklusz./min DG: " + str(input_i13))
        lab14.config(text="DG Temp.: " + str(input_i14/10)+"°C")
        lab15.config(text="F: " + str(input_i15/10)+"%")
        root.after(UPDATE_INTERVALL, ausgabe)  #Ausgabe wird nach zeit "Update intervall" aktualisiert
    ausgabe()  

#Mehtoden ENDE---------------------------------------------------------------------------------------------------------------------


#****************************************-------Aktualisieren----------***********************************************
#********************************************************************************************************************

UPDATE_INTERVALL = 1000 #Aktualisierungsrate der Panel einstellen in ms



#***************************************-------Hauptprogramm----------***********************************************
#***********************************************************************************************************************

#Instanzen erzeugen---------------------------------------------------------
heiz_1 = Heizen()                              #Instanz der klasse Heizung erzeugen
sys_1 = System()                               #Instanz der klasse Heizung erzeugen
notb_1 = System()                              #Instanz der klasse Notbedienung erzeugen
storen_eg = Storen_EG(ser)                     #Instanz1 der klasse Storen erzeugen
licht_1 = Licht()                              #Instanz der klasse Licht erzeugen

#Global Variablen definieren---------------------------------------------------------
global counter
counter =0

global gelesen
gelesen =0

#Variablen für Empfang Integer Werte
global input_i0, input_i1, input_i2, input_i3, input_i4,  input_i5,  input_i6,  input_i7   
global input_i8, input_i9, input_i10, input_i11, input_i12, input_i13, input_i14, input_i15

input_i0=0
input_i1=0
input_i2=0
input_i3=0
input_i4=0
input_i5=0
input_i6=0
input_i7=0
input_i8=0
input_i9=0
input_i10=0
input_i11=0
input_i12=0
input_i13=0
input_i14=0
input_i15=0

#Variablen für Empfang Binär Werte
global input_b0, input_b1,  input_b2, input_b3, input_b4, input_b5, input_b6, input_b7                 
global input_b8, input_b9, input_b10, input_b11, input_b12, input_b13, input_b14, input_b15
global input_b16, input_b17, input_b18, input_b19, input_b20, input_b21, input_b22, input_b23
global input_b24, input_b25, input_b26, input_b27, input_b28, input_b29, input_b30, input_b31

input_b0=0
input_b1=0
input_b2=0
input_b3=0
input_b4=0
input_b5=0
input_b6=0
input_b7=0
input_b8=0
input_b9=0
input_b10=0
input_b11=0
input_b12=0
input_b13=0
input_b14=0
input_b15=0
input_b16=0
input_b17=0
input_b18=0
input_b19=0
input_b20=0
input_b21=0
input_b22=0
input_b23=0
input_b24=0
input_b25=0
input_b26=0
input_b27=0
input_b28=0
input_b29=0
input_b30=0
input_b31=0
input_b32=0

    
#***********************************************************************************************************************
#Hauptfenster (name root)-----------------------------------------------------------------
root = Tk()                                                             #Fenster erzeugen mit Namen xxx
root.title('KS-Automation')    #Titel des fensters definieren
root.geometry('1920x1080')
#root[bg] = "blue"

#Methode Daten empfangen aufrufen
empfangen()

#Fenster-Inhalt definieren
label1 = Label(root, text="Gebäudeleitsystem",
               fg="black",font = "Helvetica 25 bold")
label1.place(x=35,y=20)

label2 = Label(root, text="KS-Automation",
               fg="black",font = "Helvetica 15 bold")
label2.place(x=35,y=1000)

#Lables für Analog-Anzeigen 16 Stück-----------------------------------------
label10 = Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label10.place(x=35,y=60)

label11= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label11.place(x=35,y=100)

label12= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label12.place(x=35,y=140)

label13= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label13.place(x=35,y=180)

label14= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label14.place(x=35,y=220)

label15= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label15.place(x=35,y=260)

label16= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label16.place(x=35,y=300)

label17= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label17.place(x=35,y=340)

label18= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label18.place(x=350,y=340)

label19= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label19.place(x=35,y=380)

label20= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label20.place(x=35,y=420)

label21= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label21.place(x=35,y=460)

label22= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label22.place(x=35,y=500)

label23= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label23.place(x=35,y=540)

label24= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label24.place(x=35,y=580)

label25= Label(root, fg="black",font = "Helvetica 20 bold") #Label anlegen
label25.place(x=350,y=580)

#Labels an Zyklische Ausgabemethode übergeben
ausgabe_label1(label10,label11,label12,label13,label14,label15,label16,label17,label18,label19,label20,label21,label22,label23,label24,label25)  


#Unterfenster über Button aufrufen------------------------------------------
def h_button1():                                                      #Befehl für Küchenpanel aufrufen
    heiz_1.H_Fenster1()                                         #Instanz aufrufen  
h_button1 = Button(root, text='Heizung', font = "Helvetica 25 bold",
width=12,height=4,bg= "SteelBlue1",activebackground= "SteelBlue1",command = h_button1)
h_button1.place(x=35,y=625)

def h_button2():                                                #Befehl für Storen aufrufen
    storen_eg.Fenster1()                                         #Instanz aufrufen                                                  
h_button2 = Button(root, text='Storen', font = "Helvetica 25 bold",
width=12,height=4,bg= "SteelBlue1",activebackground= "SteelBlue1",command = h_button2)
h_button2.place(x=35,y=825)

def h_button3():                                                      #Befehl für Küchenpanel aufrufen
    licht_1.L_Fenster1()                                         #Instanz aufrufen                                                  
h_button3 = Button(root, text='Licht', font = "Helvetica 25 bold",
width=12,height=4,bg= "SteelBlue1",activebackground= "SteelBlue1",command = h_button3)
h_button3.place(x=315,y=625)

def h_button4():                                                    #Befehl für System aufrufen
    sys_1.S_Fenster1()                                         #Instanz aufrufen                                                  
h_button4 = Button(root, text='System', font = "Helvetica 25 bold",
width=12,height=4,bg= "SteelBlue1",activebackground= "SteelBlue1",command = h_button4)
h_button4.place(x=315,y=825)

 

#************************************************************************************************************   

#Mainloop damit Fenster geöffnet bleibt
mainloop()
#Hauptprogramm ENDE
#************************************************************************************************************

        



 
           







