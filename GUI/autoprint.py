import serial
from data_sort import convert

def connect():
    port = "/dev/tty.usbserial"
    baud = 9600

    ser = serial.Serial(str(port), baud)
    if ser.is_open():
        print "Connected..."

    while ser.is_open:
            return 0
    else:
        return -1   
        
connect()

def Autoprint():
    rxstr = ''
    while (1):
        
        out = ''
        out += ser.read()
        rxstr += out
        #if out != '':
#            print (out)
        if out == ';':
            convert(rxstr)
            rxstr = ''

def serwrite(my_input):
    ser.write(my_input)

