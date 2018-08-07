import serial
import time
import sys
import os
import re
from data_sort import convert

class commandline(object):
    def __init__(self, my_input):
        self.my_input = raw_input


cmdstate = ""

def connect(a,b): 

    global serial_object
    serial_object = serial.Serial(str(a), b)
    while serial_object.is_open:
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    


def commands():
    global serial_object
    
    
    cmd = raw_input()


    if cmd == " ":
        print("updating data\n")
        serial_object.write("RN")
        if serial_object.in_waiting():
            livedata = serial_object.read()
            print convert(livedata)
        else:
            print("no data")
            cmd = raw_input()
                                                        
        
    elif cmd == "a":
        print("entering auto printout mode\n")
        cmdstate = "autoprint"
     
            
            
        
    elif cmd == "e":    
        print("exiting program and disconnecting from serial")    #e: exit hotkey
        serial_object.close() 
        sys.exit()

    else:                                                         #all other commands are sent to serial
        serial_object.write(cmd)

    return cmdstate



