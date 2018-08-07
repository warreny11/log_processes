import re
import time
import sys
import serial
from autoprint import Autoprint
from commandinput import commandline

debug = 1

class SLconnect(commandline):
    def __init__(self):

        if debug == 1:

            self.port = "/dev/tty.usbserial"
            self.baud = 9600

        elif debug == 0:
            self.port = raw_input("Enter Port Name: ")
            self.baud = raw_input("Enter Baud Rate: ")

    def connect(self,a,b): 
        
        ser = serial.Serial(str(a), b)
        while ser.is_open:
            return 0
        else:
            return -1   
    
    if connect(self.port, self.baud)==0:
        print ("Connected to " + name)
        print "To switch to auto mode, press a and Enter\nTo type commands, type then enter\nTo disconnect and exit, press e and Enter"                                  #if connected
        if debug == 1:
            print port, baud
    
        while connect(port,baud)==0:
        
            cmdauto = commands()
            if cmdauto == "autoprint":
                Autoprint()
            if cmdauto == "commandin":
                commandin(my_input)
            if cmdauto == "exiting":
                leave()
                
        else: 
            print "Connection Broken..."

    elif connect(port,baud)==-1:
        print "Connection not established..."
