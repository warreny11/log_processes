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
        print "Initializing Connection..."

    def connect(self):
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1



class Commands(Connection):
    def __init__(self,my_input):
        self.my_input = raw_input

    def commands(self):    

        if self.my_input == "a":
            commandstatus = "auto"
                    
        if self.my_input == "e":
            commandstatus = "exit"
            
        else :
            commandstatus = "free"
            
        return commandstatus

    def Autoprint(self):
    
        rxstr = ''
        out = ''
        out += self.ser.read()
        rxstr += out
        #if out != '':
    #            print (out)
        if out == ';':
            print(convert(rxstr))
            rxstr = ''

    def executecommand(self,status): 
    
        if status == "auto":
            print "Entering Auto-update Mode..."
            Autoprint()
                    
        if status == "exit":
            print("Exiting program and disconnecting from Serial...")    #e: exit hotkey
            self.ser.close() 
            sys.exit()

        if status == "free":
            self.ser.write(raw_input())

   