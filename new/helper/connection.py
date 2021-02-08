
from sys import modules
from tkinter import messagebox
from serial.tools import list_ports
from serial import Serial, SerialException

class Connection:
    def __init__(self):
        '''
        Open serial connection if not extist and add to main (root) application
        '''
        app = modules['__main__']
        
        if not hasattr(app, 'serialConnection'):
            try: 
                app.serialConnection = Serial(self.getPort(), baudrate = 19200, timeout=1)
            except  SerialException as err:
                print(err)
                messagebox.showwarning(title = 'Serial Connection', message = err)
        self.connection = app.serialConnection

    def getPort(self):
        portIndex = 0
        ports = list(list_ports.comports())
        for p in ports:
            while portIndex < 9:
                if 'CH340' in p[1]:
                    return p[0]
                portIndex += 1
        return None


    def write(self, code):
        if self.connection.is_open:
            self.connection.write(str.encode(code))
            return True
        return False