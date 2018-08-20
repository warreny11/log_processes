import serial
import time
from SCRIPT import Connection

print "port: ",
port = raw_input()
print "baud: ",
baud = raw_input() 

my_SL1_connection = Connection()
Connect_status = my_SL1_connection.connect(port,baud)

if Connect_status==0:
    my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








