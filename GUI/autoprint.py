import serial
from data_sort import convert

port = "/dev/tty.usbserial"
baud = 9600

serial_object = serial.Serial(port, baud)

cmd = raw_input()


def autoprint(cmd):
    
    if cmd=="a":

        print("entering auto printout mode\n")
        
        size = serial_object.inWaiting()
        if size:
            livedata = serial_object.read(size)
            print convert(livedata)

        else : 
            print("no data")