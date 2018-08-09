import SCRIPT
from data_sort import convert

debug = 1

if debug == 0:
    port = raw_input("Enter full port name: ")
    baud = raw_input("Enter baud rate: ")

if debug == 1:
    port = "/dev/tty.usbserial"
    baud = 9600

my_SL1_connection = SCRIPT.Connection(port,baud)
my_SL1_connection.connect(port,baud)
print my_SL1_connection.ser

if my_SL1_connection.connect(port,baud)==0:
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

def serwrite(my_input):
    
    my_SL1_connection.ser.write(my_input)
    
while my_SL1_connection.connect(port,baud)==0:
    my_input = raw_input()
    my_SL1_whileconnect = SCRIPT.Commands(my_input)
    my_SL1_whileconnect.commands(my_input)








