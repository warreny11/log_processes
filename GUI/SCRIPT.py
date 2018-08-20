import serial
import sys
from data_sort import convert
import platform



class SerialWrapper:
    def __init__(self, port, baud):
        print "Initializing Connection..."

        try: 
            self.ser = serial.Serial(str(port), int(baud))
            while self.ser.is_open:
                connect_status = 0
                print "Connected..."
                
            else:
                connect_status = -1
                print "Unconnected..."
                    
        except:
            connect_status = -1
            print "Connection Failed...Did you type the full name of the Port?"
            

    def serialwrite(self, my_input):
        self.ser.write(my_input)

    def serialread(self):
        self.ser.read()

    def serialclose(self):
        self.ser.close()
                
    def sendData(self, data):
        data += "\r\n"
        self.ser.write(data.encode())


class NonSerial():
    
    def __init__(self):
        
        self.rxstr = ""
        

    def connect(self,port,baud): 
        print "hey"
        SerialWrapper(port,baud)

        Connect_status = 1
        return Connect_status
                    
    def commands(self,my_input): 
        
        if my_input == "a":
            commandstatus = "auto"
            print "Entering Auto-update Mode..."
            
        elif my_input == "e":
            commandstatus = "exit"
            print "Exiting program and Disconnecting from Serial"

        else:
            commandstatus = "free"

        return commandstatus
        
    def executecommand(self,my_input):
        self.my_input = my_input

        commandstatus = "start"
        commandstatus = self.commands(self.my_input)

        if commandstatus == "auto":
            out = ''
            out += SerialWrapper.serialread
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            SerialWrapper.serialclose 
            sys.exit()

        if commandstatus == "free":
            SerialWrapper.serialwrite(self,self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        
        if out == ';':
            print(convert(self.rxstr))
            self.rxstr = ''


