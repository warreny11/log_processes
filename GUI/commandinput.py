import serial
import time
from data_sort import convert


port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(port, baud)

class commandline:
    def __init__(self, my_input):
        self.my_input = my_input
    
    def commandin(self, my_input):
        my_input = raw_input()
        ser.write(my_input)

    def commands(self, my_input):
                                                    
        if self.my_input== "a":
            print("entering auto printout mode\n")
            cmdstate = "autoprint"
        
        if self.my_input== "e":    
            cmdstate = "exiting"

        else :
            cmdstate = "commandin"

        return cmdstate
    
    def Autoprint(self):
        rxstr = ''
        while (1):
        
            out = ''
            out += ser.read()
            rxstr += out
            #if out != '':
    #            print (out)
            if out == ';':
                convert(rxstr)
                rxstr = ''
       
                
#commandin()
