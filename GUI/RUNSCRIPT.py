import serial
import time
from SCRIPT import NonSerial,SerialWrapper
import sys
import threading
from Queue import Queue
import time

print_lock = threading.Lock()

print "port: ",
sys.stdout.flush()
port = raw_input()
print 
sys.stdout.flush()
print "baud: ",
sys.stdout.flush()
baud = raw_input()


my_SL1_connection = NonSerial()
con1 = my_SL1_connection.connect(port,baud)

def runtime(my_input):
    my_SL1_connection.executecommand(my_input)
        # t1 = threading.Thread(target = my_SL1_connection.executecommand(raw_input())

def threader():
    while True:
        # gets an worker from the queue
        # Run the example job with the avail worker in queue (thread)
        runtime(raw_input())
        # completed with the job
        q.task_done()


q = Queue()

# wait until the thread terminates.
q.join()


t = threading.Thread(target=threader)
# classifying as a daemon, so they will die when the main dies
t.daemon = True
# begins, must come after daemon definition
t.start()








# while con1 == 0:
#     listener = threading.Thread(target=runtime)
#     listener.start()