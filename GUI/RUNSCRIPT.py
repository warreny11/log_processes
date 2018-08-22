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
con1 = my_SL1_connection.connect(port,baud)


# def runtime():
#     my_SL1_connection.executecommand(raw_input())
    # t1 = threading.Thread(target = my_SL1_connection.executecommand(raw_input())
        
while con1 == 0:
    my_SL1_connection.executecommand(raw_input())