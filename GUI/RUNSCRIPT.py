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

my_SL1_connection = SerialWrapper(port,baud)
nonserial = NonSerial()


while my_SL1_connection==0:
    nonserial.executecommand(raw_input())
    
            

    

    




        
        








