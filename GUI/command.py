import serial
import time

port = "/dev/tty.usbserial"
baud = 9600

try:
    serial_object = serial.Serial(port, baud)
    if serial_object.is_open:
        print("Connected to " + port)
        serial_object.write(b'Connected')
except:
    print "Cant Open Specified Port"

usrcmd = raw_input
serial_object.write(usrcmd)

