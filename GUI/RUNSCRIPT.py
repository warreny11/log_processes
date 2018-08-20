import serial
import time
from SCRIPT import NonSerial
import sys




my_SL1_connection = NonSerial()
Connect_status = my_SL1_connection.connect(port,baud)

if Connect_status == 0:
    print "Connection Established...Serial Port Open..."

else :
    print "Unconnected...Please Try Again"
    sys.exit()

    

    




        
        








