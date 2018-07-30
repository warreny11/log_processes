import serial
import sys 

serial_object = serial.Serial("/dev/tty.usbserial", 9600)

usrexit = raw_input()

def disconnect(usrexit):
    if usrexit == "e": 
        try :   
            print("exiting program and disconnecting from serial")
            serial_object.close() 
            sys.exit()
        except :
            print("still connected")

