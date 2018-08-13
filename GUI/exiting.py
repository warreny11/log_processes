import serial
import sys 

port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(port, baud)

def leave():   
    print("exiting program and disconnecting from serial")    #e: exit hotkey
    ser.close() 
    sys.exit()
    
