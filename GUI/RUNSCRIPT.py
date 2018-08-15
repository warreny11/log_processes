import serial
import time
from SCRIPT import Connection



my_SL1_connection = Connection()
port = raw_input("port: ")
baud = raw_input("baud: ")
Connect_status = my_SL1_connection.connect(port,baud)

if Connect_status==0:
    print "Connected..."


my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








