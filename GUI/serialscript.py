from serialcom import connect, commands, serial, commandline
import re
import time
import sys
from autoprint import autoprintser
from commandinput import commandin
from exiting import leave

debug = 1



if debug == 1:
    port = "/dev/tty.usbserial"
    baud = 9600

elif debug == 0:
    port = raw_input("Enter Port Name: ")
    baud = raw_input("Enter Baud Rate: ")

if connect(port,baud)==0:
    print "Connected..." 
    print "To switch to auto mode, press a and Enter\nTo type commands, type then enter\nTo disconnect and exit, press e and Enter"                                  #if connected
    if debug == 1:
        print port, baud
    
    while connect(port,baud)==0:
        
        cmdauto = commands()
        if cmdauto == "autoprint":
            autoprintser()
        if cmdauto == "commandin":
            commandin(my_input)
        if cmdauto == "exiting":
            leave()
            
    else: 
        print "Connection Broken..."

elif connect(port,baud)==-1:
    print "Connection not established..."
