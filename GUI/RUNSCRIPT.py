import serial
import time
from SCRIPT import NonSerial,SerialWrapper
import sys


print "port: ",
sys.stdout.flush()
# port = raw_input()
port = "COM8"
print 
sys.stdout.flush()
print "baud: ",
sys.stdout.flush()
# baud = raw_input()
baud = 9600

my_SL1_connection = NonSerial()
con1 = my_SL1_connection.connect(port,baud)


def runtime(my_input):
    return my_SL1_connection.executecommand(my_input)

        
while con1 == 0:
    runtime(raw_input())

    # modset = "true"
    # while modset == "true":
    #     my_input = raw_input()
        
    #     while my_input == "a":
    #         my_input == "a"
    #         runtime(my_input)
    #         modset = "true"

    #     else:
    #         runtime(my_input)
    #         modset = "false"
    
