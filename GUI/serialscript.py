import re
import time
import sys
import serial
from autoprint import Autoprint,serwrite
from commandinput import commandline

class SLconnect:
    
    def __init__(self,port,baud):
        debug = 0

        if debug == 1:

            self.port = "/dev/tty.usbserial"
            self.baud = 9600

        elif debug == 0:

            self.port = port
            self.baud = baud

    def connect(self,port,baud): 
        
        self.ser = serial.Serial(str(self.port), self.baud)
        while self.ser.is_open:
            print 0
            return 0
        else:
            print -1
            return -1   

name = ""
i = 1

name = ("SL" + str(i))
print name
name = SLconnect(raw_input("Enter Port Name: "),raw_input("Enter Baud Rate: "))

bob = commandline(raw_input)

if name.connect==0:
    print ("Connected to " + name)
    print "To switch to auto mode, press a and Enter\nTo type commands, type then enter\nTo disconnect and exit, press e and Enter"                                  #if connected

    
    
    while name.connect==0:
        
        cmdauto = commandline(raw_input)
        if cmdauto == "autoprint":
            Autoprint()
        if cmdauto == "commandin":
            bob.commandin(raw_input)

        if cmdauto == "exiting":
            print("exiting program and disconnecting from serial")    #e: exit hotkey
            name.ser.close() 
            sys.exit()
                
    else: 
        print "Connection Broken..."

elif name.connect==-1:
    print "Connection not established..."
