import serial
import sys
from data_sort import convert
import platform

print "port:",
sys.stdout.flush()
port = raw_input()

print "baud:",
sys.stdout.flush()
baud = raw_input() 

class Serialstuff():
    def __init__(self,ser):
        self.ser = ser
        
    def serialconnect(self,port,baud):

        system = platform.system()
            # This determines the system running
        poss_systems =[
                ("Windows", "1"),
                ("Linux", "2"),
                ("Darwin", "3"),
            ]
        for text,modes in poss_systems:
            if system == text:
                # print system
                version_ = int(modes)
                # print self.version_

        sys_list = [("Windows","1","COM"),
                    ("Linux", "2","/dev/tty"),
                    ("Mac", "3","/dev/tty.")]

            
        for types, nums, ports in sys_list:
            if version_ == int(nums):
                try:
                    self.ser = serial.Serial(ports + str(port), baud)
                    if self.ser.is_open :
                        print "hey"
                        return 0
                    else :
                        print "no"
                        return -1 
                except:
                    print("Running " + types + ": Can't Open Specified Port, Try Again")
                    sys.exit()

    def serialwrite(self, my_input):
        self.ser.write(my_input)

    def serialread(self):
        self.ser.read()

    def serialclose(self):
        self.ser.close()

    #port = "/dev/tty.usbserial"
    #baud = 9600

class NonSerial():
    
    def __init__(self):
        
        self.rxstr = ""
        print "Initializing Connection..."

    def connect(self,port,baud): 
        try:
            Serialstuff.serialconnect(port,baud)
        except:
            print "sorry"
        
                    
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
            out += Serialstuff.serialread
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            Serialstuff.serialclose 
            sys.exit()

        if commandstatus == "free":
            Serialstuff.serialwrite(self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        
        if out == ';':
            print(convert(self.rxstr))
            self.rxstr = ''


