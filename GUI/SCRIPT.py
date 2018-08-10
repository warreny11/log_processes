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

    def commands(self,my_input): 
        
        if my_input == "a":
            commandstatus = "auto"
            
        elif my_input == "e":
            commandstatus = "exit"

        else:
            commandstatus = "free"

        return commandstatus
        
    def executecommand(self,my_input):
        self.my_input = my_input
    
        commandstatus = self.commands(self.my_input)

        if commandstatus == "auto":
            print "Entering Auto-update Mode..."
            while commandstatus == "auto":
                self.Autoprint()

        if commandstatus == "exit":
            print "Exiting program and Disconnecting from Serial"   #e: exit hotkey
            self.ser.close() 
            sys.exit()

        if commandstatus == "free":
            self.ser.write(my_input)

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


