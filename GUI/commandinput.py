import serial
import time

port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(port, baud)

def commandin(my_input):
    ser.write(my_input + '\r\n')
                
       
                
#commandin()
