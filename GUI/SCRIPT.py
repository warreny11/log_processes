import serial
import sys
from data_sort import convert
import serial

port = "/dev/tty.usbserial"
baud = 9600

class Connection():
    
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        self.rxstr = ""
        print "Initializing Connection..."

    def connect(self):
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1

    def commands(self,my_input): 
        
        if my_input == "a":
            commandstatus = "auto"
            print "Entering Auto-update Mode..."
            
        elif my_input == "e":
            commandstatus = "exit"
            print "Exiting program and Disconnecting from Serial"

        else:
            commandstatus = "free"

        return commandstatus
        
    def executecommand(self,my_input):
        self.my_input = my_input

        commandstatus = "start"
        commandstatus = self.commands(self.my_input)

        if commandstatus == "auto":
            out = ''
            out += self.ser.read()
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            self.ser.close() 
            sys.exit()

        if commandstatus == "free":
            self.ser.write(self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        
        if out == ';':
            print(convert(self.rxstr))
            self.rxstr = ''


