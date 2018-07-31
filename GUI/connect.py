import serial
import time
import sys

port = raw_input("Enter Port Name: ")
baud = raw_input("Enter Baud Rate: ")

def connect(): 
    global serial_object
    
    try:
        serial_object = serial.Serial(str(port), baud)
        if serial_object.is_open:
            print("Connected to " + port)
            serial_object.write(b'Connected')
    except:
        print "Cant Open Specified Port"

    if serial_object.is_open:
        while True:
            cmd = raw_input()
            if cmd == "print data":  
                size = serial_object.inWaiting()
                if size:
                    data = serial_object.read(size)
                    print data
                else:
                    print 'no data'
                time.sleep(1) 

            elif cmd == "e":    
                print("exiting program and disconnecting from serial")
                serial_object.close() 
                sys.exit()
            else:
                serial_object.write(cmd)

print connect()



