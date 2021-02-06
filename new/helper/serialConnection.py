
from serial import SerialException, Serial
from serial.tools import list_ports

class SerialConnection:
    def __init__(self):
        self.connection = Serial()

        try: 
            self.connection.baudrate = 19200
            #self.connection.port = '/dev/ttyACM0'
            self.connection.port = self.getPort()
            self.connection.timeout = 0
        except  SerialException:
            self.connection = Serial()

    def getPort(self):
        ports = list(list_ports.comports())
        for p in ports:
            while setPortIndex < 9:
                if 'CH340' in p[1]:
                    return 'COM' + str(setPortIndex)
                setPortIndex += 1
        return None


    def write(self, code):
        self.connection.open()
        if self.connection.is_open:
            self.connection.write(str.encode(code))
            self.connection.close()
            return True
        return False