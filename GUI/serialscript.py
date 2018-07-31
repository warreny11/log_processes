from ser_interface import connect, commands, serial
import re
import time

port = raw_input("Enter Port Name: ")
baud = raw_input("Enter Baud Rate: ")

if connect(port,baud)==0:
    print "Connected..."                                   #if connected
    serial_object = serial.Serial(port,baud)

    commands()
    if commands()==2:
        size = serial_object.inWaiting()
        if size:
            data = serial_object.read(size)
            print data
        else:
            print 'no data'                                       #no data, prints no data
            time.sleep(1)

elif connect(port,baud)==-1:
    print "Connection not established..."


    




    

