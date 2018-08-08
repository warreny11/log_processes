import SCRIPT



baud = 9600
port = "/dev/tty.usbserial"

my_SL1_connection = SCRIPT.Connection(port,baud)
my_SL1_connection.connect(port,baud)

if my_SL1_connection.connect(port,baud)==0:
    print "Connected..."
    
while my_SL1_connection.connect(port,baud)==0:
    my_input = raw_input()
    my_SL1_whileconnect = SCRIPT.Commands(my_input)
    my_SL1_whileconnect.commands(my_input)








