import serial
import sys
from data_sort import convert
import platform

print "port:",
sys.stdout.flush()
port = raw_input()

print "baud:",
sys.stdout.flush()
baud = raw_input() 

class Serialstuff():
    def __init__(self,ser):
        self.ser = ser
        
    def serialconnect(self,port,baud):

        try:
            self.ser = serial.Serial(str(port), baud)
            while self.ser.is_open:
                print "Connected..."
                return 0
            else:
                return -1
        except :
            print "Unconnected..."
        

    def serialwrite(self, my_input):
        self.ser.write(my_input)

    def serialread(self):
        self.ser.read()

    def serialclose(self):
        self.ser.close()

    #port = "/dev/tty.usbserial"
    #baud = 9600

class NonSerial():
    
    def __init__(self):
        
        self.rxstr = ""
        print "Initializing Connection..."

    def connect(self,port,baud): 
        
        Connect_status = Serialstuff.serialconnect(port,baud)
        return Connect_status
                    
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
            out += Serialstuff.serialread
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            Serialstuff.serialclose 
            sys.exit()

        if commandstatus == "free":
            Serialstuff.serialwrite(self,self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        
        if out == ';':
            print(convert(self.rxstr))
            self.rxstr = ''


