import serial
from autoprint import Autoprint,serwrite
from exiting import leave

class Connection:
    def __init__(self,port,baud):
        self.port = "/dev/tty.usbserial"
        self.baud = 9600

    def connect(self,a,b):
        self.ser = serial.Serial(str(a), b)
        while self.ser.is_open:
            return 0
        else:
            return -1   


class Commands(Connection):
    def __init__(self,my_input):
        self.my_input = raw_input
        
        
        
    def commands(self,my_input):    
        if my_input == "a":
            commandstate = "auto"
            print "Entering Auto-update Mode..."
        if my_input == "e":
            commandstate = "exit"
            print "Exiting..."
        else :
            commandstate = "free"
    
    def commandinterpreter(self,commandstate):
        if commandstate == "auto":
            Autoprint()
        if commandstate == "exit":
            leave()
        if commandstate == "free":
            serwrite(self.my_input)

    while connect==0:
        self.commands(self.my_input)
    

    
