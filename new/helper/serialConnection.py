
from sys import modules
from tkinter import messagebox
from sys import platform
from serial.tools import list_ports
from serial import Serial, SerialException

class SerialConnection:
    def __init__(self):
        '''
        Open serial connection if not extist and add to main (root) application
        '''
        
        # Main app
        mainApp = modules['__main__']
        
        # Set serial connection
        if not hasattr(mainApp, 'serialConnection'):        
            ports = self.getPorts()
            if ports:
                for port in self.getPorts():
                    try:
                        mainApp.serialConnection = Serial(port, baudrate = 19200, timeout = .5)
                        break
                    except (OSError, SerialException):
                        pass
                
                # Port already in use or connection error
                if not hasattr(mainApp, 'serialConnection') or not mainApp.serialConnection.is_open:
                    messagebox.showerror(title = 'Serial Connection', message = 'Serial connection error or port already in use')
                    mainApp.serialConnection = Serial()
            else:
                messagebox.showerror(title = 'Serial Connection', message = 'No Serial Port found')
                mainApp.serialConnection = Serial()
        
        self.connection = mainApp.serialConnection

    def getPorts(self):
        """ 
        Lists serial port names
        :returns: A list of the serial ports available on the system
        """
        if platform.startswith('win'):
            return ['COM%s' % (i + 1) for i in range(256)]
        elif platform.startswith('linux') or platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            return glob.glob('/dev/tty[A-Za-z]*')
        elif startswith('darwin'):
            return glob.glob('/dev/tty.*')
        return None


    def write(self, code):
        if self.connection.is_open:
            self.connection.write(code.encode())
            return True
        return False