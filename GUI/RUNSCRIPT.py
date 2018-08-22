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


def runtime(my_input):
    return my_SL1_connection.executecommand(my_input)

        
while con1 == 0:
    a = False

    if raw_input() == "a":
        a = True
        while a :
            runtime("a")
    else:
        runtime(raw_input())
