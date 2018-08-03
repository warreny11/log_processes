import serial
from data_sort import convert

port = "/dev/tty.usbserial"
baud = 9600

serial_object = serial.Serial(port, baud)



def autoprint():
    


        
        
        size = serial_object.inWaiting()
        if size:
            
            livedata = serial_object.read(size)
            print convert(livedata)

        else : 
            print("no data")