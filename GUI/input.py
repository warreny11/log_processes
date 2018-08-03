import serial
import time

port = "/dev/tty.usbserial"
baud = 9600

serial_object = serial.Serial(port, baud)
if serial_object.is_open:
    print("Connected to " + port)
    serial_object.write(b'Connected')

else:
    print "Can't Open Specified Port"

def command():
    while serial_object.is_open:
        cmd = raw_input()
        serial_object.write(cmd)

