import serial
import sys 

port = "/dev/tty.usbserial"
baud = 9600

serial_object = serial.Serial(port, baud)

def disconnect(usrexit):
    if serial_object.isOpen():
        print(serial_object.name + ' is open...')
    
    while True:
        cmd = raw_input()
        if cmd == "e":    
            print("exiting program and disconnecting from serial")
            serial_object.close() 
            sys.exit()
        else:
            serial_object(cmd.encode('ascii')+'\r\n')
            out = serial_object()
            print('Recieving...' + out)

