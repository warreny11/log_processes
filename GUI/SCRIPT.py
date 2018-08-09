import serial



class Connection():
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        print "Initializing Connection..."

    def connect(self,port,baud):
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1
