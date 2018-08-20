import serial
import sys
from data_sort import convert
import platform


#port = "/dev/tty.usbserial"
#baud = 9600

class Connection():
    
    def __init__(self):
        
        self.rxstr = ""
        print "Initializing Connection..."

    def connect(self,port,baud): 

        # port = self.port
        # baud = self.baud

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
                self.version_ = int(modes)
                # print self.version_
  
        # this is the version setter that takes system and sets the port and baud defaults
        sys_list = [("Windows","1","COM"),
                    ("Linux", "2","/dev/tty"),
                    ("Mac", "3","/dev/tty.")]

        
        for types, nums, ports in sys_list:
            if self.version_ == int(nums):
                try:
                    self.ser = serial.Serial(ports + str(port), baud)
                    if self.ser.is_open :
                        print("Running " + types + ": Connected... Please click Next")
                        
                        return 0
                    else :
                        print "Unable to connect..."
                        
                        return -1 
                except:
                    print("Running " + types + ": Can't Open Specified Port, Try Again")
                    sys.exit()
                    
        

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
            out += self.ser.read()
            self.Autoprint(out)
                  
        if commandstatus == "exit":
            self.ser.close() 
            sys.exit()

        if commandstatus == "free":
            self.ser.write(self.my_input)
        
        commandstatus = "start"
        return commandstatus 

    def Autoprint(self,out):
        self.rxstr += out
        
        if out == ';':
            print(convert(self.rxstr))
            self.rxstr = ''


