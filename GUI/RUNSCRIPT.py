import serial
import time
from SCRIPT import Connection,port,baud

my_SL1_connection = Connection(port,baud)
Connect_status = my_SL1_connection.connect()

if Connect_status==0:
    print "Connected..."

while Connect_status==0:
    my_SL1_connection.executecommand(raw_input())

    




        
        








