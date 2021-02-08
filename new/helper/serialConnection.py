
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
            for port in self.getPorts():
                mainApp.serialConnection = Serial(port, baudrate = 19200, timeout=1)
                break
            
        self.connection = mainApp.serialConnection

    def getPorts(self):
        """ 
        Lists serial port names
        :raises EnvironmentError: On unsupported or unknown platforms
        :returns: A list of the serial ports available on the system
        """
        if platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif platform.startswith('linux') or platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = Serial(port)
                s.close()
                result.append(port)
            except (OSError, SerialException):
                pass
        return result


    def write(self, code):
        if self.connection.is_open:
            self.connection.write(str.encode(code))
            return True
        return False