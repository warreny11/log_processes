import serial
import time

def connect(): 
    global serial_object
    port = raw_input("Enter Port Name: ")
    baud = raw_input("Enter Baud Rate: ") 

    serial_object = serial.Serial(str(port), baud)

if serial_object.is_open:
    while True:
        size = serial_object.inWaiting()
        if size:
            data = serial_object.read(size)
            print data
        else:
            print 'no data'
        time.sleep(1)