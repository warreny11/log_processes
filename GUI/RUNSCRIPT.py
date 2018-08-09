from SCRIPT import Connection,port,baud,Commands,Autoprint

my_SL1_connection = Connection(port,baud)
my_SL1_connection.connect()

if my_SL1_connection.connect()==0:
    print "Connected..."

while my_SL1_connection.connect()==0:
    print "bob"




        
        








