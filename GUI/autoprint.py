import serial
from data_sort import convert

port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(port,baud)

 

def Autoprint():
    rxstr = ''
    while(1):
        out = ''
        out += ser.read()
        rxstr += out
        if out == ';':
            print(convert(rxstr))
            rxstr = ''

Autoprint()