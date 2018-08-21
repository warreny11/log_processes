import serial
import time
from SCRIPT import NonSerial,SerialWrapper
import sys

print "port: ",
sys.stdout.flush()
port = raw_input()
print 
sys.stdout.flush()
print "baud: ",
sys.stdout.flush()
baud = raw_input()

my_SL1_connection = NonSerial()
my_SL1_connection.connect(port,baud)


while my_SL1_connection==0:
    my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








