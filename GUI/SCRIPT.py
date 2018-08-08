import serial
from autoprint import Autoprint,serwrite
from exiting import leave

debug = 0

class Connection():
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        print "Initializing Connection..."

    def connect(self,a,b):
        self.ser = serial.Serial(str(a), b)
        while self.ser.is_open:
            return 0
        else:
            return -1   


class Commands():
    def __init__(self,my_input):
        self.my_input = my_input
        if debug==1:
            print "Initializing Commands"
        
        
    def commands(self,my_input):    
        if my_input == "a":
            print "Entering Auto-update Mode..."
            Autoprint()
                    
        if my_input == "e":
            print "Exiting..."
            leave()

        else :
            serwrite(my_input)
        


    




            
    

    
