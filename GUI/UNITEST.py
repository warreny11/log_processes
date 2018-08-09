import serial
import SCRIPT



def Test_Connection():
    print "Testing Connection..."
    port = "/dev/tty.usbserial"
    baud = 9600
    my_SL1_connection = SCRIPT.Connection(port,baud)
    my_SL1_connection.connect(port,baud)
    print my_SL1_connection.ser.is_open()
    if my_SL1_connection.ser.is_open() == True:
        print "Pass"
    else :
        print "Fail"

Test_Connection()

