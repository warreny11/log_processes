import serial
import time

port = "/dev/tty.usbserial"
baud = 9600

try:
    serial_object = serial.Serial(port, baud)
    if serial_object.is_open:
        print("Connected to " + port)
        serial_object.write(b'Connected')

        usrcmd = raw_input
        serial_object.write(usrcmd)
        
except:
    print "Can't Open Specified Port"



