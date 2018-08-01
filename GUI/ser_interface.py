import serial
import time
import sys

def connect(a,b): 
    global serial_object
    serial_object = serial.Serial(str(a), b)
    while serial_object.is_open:
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    

def commands():

    if serial_object.is_open:
        while True:
            cmd = raw_input()
            a = 0
            if cmd == " ":
                serial_object.write("RN")
                a = 2                                       #prints current data              
                

            elif cmd == "a":
                a = 3
                
            
            elif cmd == "s":
                a = 0
                

            elif cmd == "e":    
                print("exiting program and disconnecting from serial")    #e: exit hotkey
                serial_object.close() 
                sys.exit()

            else:                                                         #all other commands are sent to serial
                serial_object.write(cmd)





