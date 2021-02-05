
from serial import SerialException, Serial

class SerialConnection:
    def __init__(self):
        try: 
            self.connection = Serial('/dev/ttyACM0', 9600, timeout = 0)
        except  SerialException:
            self.connection = Serial()

    def write(self, code):
        self.connection.write(str.encode(code))