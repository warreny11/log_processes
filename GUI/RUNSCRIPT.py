from data_sort import convert
import sys 
import serial

class Connection():
    def __init__(self,port,baud):
        self.port = port
        self.baud = baud
        print "Initializing Connection..."

    def connect(self):
        self.ser = serial.Serial(str(port), baud)
        while self.ser.is_open:
            return 0
        else:
            return -1

print "help"
port = "/dev/tty.usbserial"
baud = 9600

print "Hello"
my_SL1_connection = Connection(port,baud)
my_SL1_connection.connect()
print my_SL1_connection

if my_SL1_connection.connect()==0:
    print "Connected..."

def Autoprint():
    
    rxstr = ''
    while (1):
        
        out = ''
        out += my_SL1_connection.ser.read()
        rxstr += out
        #if out != '':
#            print (out)
        if out == ';':
            convert(rxstr)
            rxstr = ''

    
def commands(my_input):    
        if my_input == "a":
            print "Entering Auto-update Mode..."
            Autoprint()
                    
        if my_input == "e":
            print("Exiting program and disconnecting from Serial...")    #e: exit hotkey
            my_SL1_connection.ser.close() 
            sys.exit()

        else :
            my_SL1_connection.ser.write(my_input)
    
while my_SL1_connection.ser.is_open:
    commands(raw_input())
    








