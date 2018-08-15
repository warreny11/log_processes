import serial
import time
from SCRIPT import Connection

<<<<<<< HEAD


my_SL1_connection = Connection()
port = raw_input("port: ")
baud = raw_input("baud: ")
Connect_status = my_SL1_connection.connect(port,baud)
=======
my_SL1_connection = Connection()
Connect_status = my_SL1_connection.connect()
>>>>>>> d149bafe5d550d49aaa801b4ffd57fae6e516b39

if Connect_status==0:
    print "Connected..."


my_SL1_connection.executecommand(raw_input())
    
            

    

    




        
        








