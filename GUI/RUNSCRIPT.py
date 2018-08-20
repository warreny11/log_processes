import serial
import time
from SCRIPT import Connection
import sys


print "port:",
sys.stdout.flush()
port = raw_input()

print "baud:",
sys.stdout.flush()
baud = raw_input() 

my_SL1_connection = Connection()
Connect_status = my_SL1_connection.connect(port,baud)

if Connect_status==0:
    my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








