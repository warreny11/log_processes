import serial
import time

port = raw_input("Enter Port Name: ")
baud = raw_input("Enter Baud Rate: ")

def connect(): 
    global serial_object
    
    try:
        serial_object = serial.Serial(str(port), baud)
        serial_object.write(b'this is me')
    except:
        print "Cant Open Specified Port"

    if serial_object.is_open:
        while True:
            size = serial_object.inWaiting()
            if size:
                data = serial_object.read(size)
                print data
            else:
                print 'no data'
            time.sleep(1) 
            



