import re
import time
import sys
import serial
from autoprint import Autoprint
from commandinput import commandline

debug = 1

if debug == 1:

    port = "/dev/tty.usbserial"
    baud = 9600

elif debug == 0:

    port = raw_input("Enter Port Name: ")
    baud = raw_input("Enter Baud Rate: ")

class SLconnect:
    def __init__(self,port,baud):

       self.port = port
       self.baud = baud

    def connect(self,port,baud): 
        
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1   

name = ""
i = 1

name = ("SL" + str(i))

name = SLconnect(port,baud)
name.connect = port,baud
bob = commandline(raw_input)

if name==0:
    print ("Connected to " + name)
    print "To switch to auto mode, press a and Enter\nTo type commands, type then enter\nTo disconnect and exit, press e and Enter"                                  #if connected

    if debug == 1:
        print port, baud
    
    while name==0:
        
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

elif name==-1:
    print "Connection not established..."
