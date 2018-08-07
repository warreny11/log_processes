import serial
import time
import sys
import os
import re
from data_sort import convert

port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(port, baud)

cmdstate = ""

def connect(a,b): 
    
    
    ser = serial.Serial(str(a), b)
    while ser.is_open:
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    
class commandline(object):
    def __init__(self):
        self.my_input = raw_input()

def commands():

    test = commandline()
                                                                
    if test.my_input== "a":
        print("entering auto printout mode\n")
        cmdstate = "autoprint"
     
    if test.my_input== "e":    
        cmdstate = "exiting"

    else :
        cmdstate = "commandin"

    return cmdstate



