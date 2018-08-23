import serial
import time
from autoprint import NonSerial,SerialWrapper
import sys



sys.stdout.flush()
# port = raw_input()
port = "COM8"


sys.stdout.flush()
# baud = raw_input()
baud = 9600

my_SL1_connection = NonSerial()
con1 = my_SL1_connection.connect(port,baud)


def runtime(my_input):
    return my_SL1_connection.executecommand(my_input)

        
while con1 == 0:
    runtime("a")