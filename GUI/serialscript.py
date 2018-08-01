from ser_interface import connect, commands, serial
import re
import time
debug = 1

if debug == 0:
    port = raw_input("Enter Port Name: ")
    baud = raw_input("Enter Baud Rate: ")

if debug == 1:
    port = "dev/tty.usbserial"
    baud = 9600

if connect(port,baud)==0:
    print "Connected..." 
    print "To print updated data, press spacebar\nTo switch to auto mode, press a\nTo disconnect and exit, press e"                                  #if connected
    serial_object = serial.Serial(port,baud)
    while connect(port,baud)==0:

        commands()
            
    else: 
        print "Connection Broken..."

elif connect(port,baud)==-1:
    print "Connection not established..."