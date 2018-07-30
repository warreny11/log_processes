import serial
import time
import sys 

#port = raw_input("Enter Port Name: ")
#baud = raw_input("Enter Baud Rate: ")
usrexit = raw_input()

def connect(): 
    global serial_object
    
    try:
        serial_object = serial.Serial("/dev/tty.usbserial", 9600)
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
            import serial

def disconnect(usrexit):
    if usrexit == "e": 
        try :   
            print("exiting program and disconnecting from serial")
            serial_object.close() 
            sys.exit()
        except :
            print("still connected")


print connect()



