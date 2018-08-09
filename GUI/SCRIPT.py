import serial
from exiting import leave
from data_sort import convert

debug = 0

class Connection():
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        
        
        print "Initializing Connection..."

    def connect(self,port,baud):
        
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1   
    
class InsideCommands(Connection):
    def __init__(self,port,baud,ser,my_input):
        Connection.__init__(self,port,baud)
        self.ser = Connection.connect(self.port,baud)
    
    def Autoprint(self):
        rxstr = ''
        while (1):
        
            out = ''
            out += self.ser.read()
            rxstr += out
            #if out != '':
    #            print (out)
            if out == ';':
                convert(rxstr)
                rxstr = ''

    def serwrite(self,my_input):
        self.ser.write(my_input)

class Commands(InsideCommands):
    def __init__(self,my_input):
        self.my_input = my_input
        if debug==1:
            print "Initializing Commands"
        
        
    def commands(self,my_input):    
        if my_input == "a":
            print "Entering Auto-update Mode..."
            InsideCommands.Autoprint(self)
                    
        if my_input == "e":
            print "Exiting..."
            leave()

        else :
            InsideCommands.serwrite(self,my_input)



        


    




            
    

    
