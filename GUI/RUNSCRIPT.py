import serial
import time
from SCRIPT import NonSerial

print "port: ",
port = raw_input()
print "baud: ",
baud = raw_input() 

my_SL1_connection = NonSerial()
Connect_status = my_SL1_connection.connect(port,baud)

if Connect_status==0:
    my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








