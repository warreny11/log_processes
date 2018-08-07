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

class commandline(object):
    def __init__(self, my_input):
        commandline.my_input = raw_input()


def connect(a,b): 
    
    
    ser = serial.Serial(str(a), b)
    while ser.is_open:
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    
def commands():
    
                                                                
    if commandline.my_input== "a":
        print("entering auto printout mode\n")
        cmdstate = "autoprint"
     
    if commandline.my_input== "e":    
        cmdstate = "exiting"

    else :
        cmdstate = "commandin"

    return cmdstate



