import serial
import sys
from data_sort import convert
import platform
import threading



class SerialWrapper:
    def __init__(self,port,baud):
        
        self.port = port
        self.baud = baud

    def serialconnect(self):

        # print self.port
        try: 
            self.ser = serial.Serial(str(self.port), int(self.baud))
            
            if self.ser.is_open:
                connect_status = 0
                print "Connected..."
                sys.stdout.flush()
                
            else:
                connect_status = -1
                print "Unconnected..."
                sys.stdout.flush()
                    
        except:
            connect_status = -1
            print "Connection Failed...Did you type the full name of the Port?"
            sys.stdout.flush()
            sys.exit()

        return connect_status

    def serialwrite(self, my_input):
        self.ser.write(my_input)

    def serialread(self):
        return self.ser.read()

    def serialclose(self):
        self.ser.close()
                

class NonSerial(SerialWrapper):
    
    def __init__(self):
        
        self.rxstr = ""
        

    def connect(self,port,baud):

        print 
        sys.stdout.flush()
        print "Initializing Connection..."
        sys.stdout.flush()

        self.port = port
        self.baud = baud
        

        connect_status = ""
        
        SerialWrapper(port,baud)
        connect_status = self.serialconnect()

        # print connect_status

        return connect_status
        
                    
    def commands(self,my_input): 
        
        if my_input == "a":
            commandstatus = "auto"
            print "Entering Auto-update Mode..."
            sys.stdout.flush()
            
            
        elif my_input == "e":
            commandstatus = "exit"
            print "Exiting program and Disconnecting from Serial"
            sys.stdout.flush()

        else:
            commandstatus = "free"

        return commandstatus
        
    def executecommand(self,my_input):
        self.my_input = my_input

        commandstatus = "start"
        commandstatus = self.commands(self.my_input)

        if commandstatus == "auto":
            out = ''
            out += str(SerialWrapper.serialread(self))
            print out
            print "sup"
            sys.stdout.flush()
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            SerialWrapper.serialclose(self)
            sys.exit()

        if commandstatus == "free":
            SerialWrapper.serialwrite(self,self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        print "hey"
        print "rxstr = " + self.rxstr
        sys.stdout.flush()
        if out == ';':
            print(convert(self.rxstr))
            sys.stdout.flush()
            self.rxstr = ''


