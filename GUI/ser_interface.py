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

    while serial_object.is_open:
            cmd = raw_input()
            
            if cmd == " ":
                serial_object.write("RN")                                       #prints current data              
                
            elif cmd == "a":
                while True:
                    size = serial_object.inWaiting()
                    if size:
                        data = serial_object.read(size)
                        print data
                    if cmd == "s":
                        break
                
            elif cmd == "e":    
                print("exiting program and disconnecting from serial")    #e: exit hotkey
                serial_object.close() 
                sys.exit()

            else:                                                         #all other commands are sent to serial
                serial_object.write(cmd)





