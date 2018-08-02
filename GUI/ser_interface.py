import serial
import time
import sys
import os
import re
from data_sort import convert


def connect(a,b): 

    global serial_object
    serial_object = serial.Serial(str(a), b)
    while serial_object.is_open:
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    

def commands():
    global serial_object
    while serial_object.is_open:
            cmd = raw_input()
            
            if cmd == " ":
                print("updating data\n")
                serial_object.write("RN")
                if serial_object.in_waiting:
                    livedata = serial_object.read()
                    print convert(livedata)
                else:
                    print("no data")
                    cmd = raw_input()
                                                                 
                
            elif cmd == "a":
                print("entering auto printout\n")
                size = serial_object.inWaiting()
                if size:
                    while True:
                        livedata = serial_object.read(size)
                        print convert(livedata)
            
                        cmd = raw_input()
                    if cmd == "s":
                        break
                    
                
            elif cmd == "e":    
                print("exiting program and disconnecting from serial")    #e: exit hotkey
                serial_object.close() 
                sys.exit()

            else:                                                         #all other commands are sent to serial
                serial_object.write(cmd)





