import liveline
import data_
import data_import
import re
import time
import data_sort


def connect(): 
    global serial_object
    port = raw_input("Enter Port Name: ")
    baud = raw_input("Enter Baud Rate: ") 

    serial_object = serial.Serial(str(port), baud)

if serial_object.is_open:
    while True:
        size = serial_object.inWaiting()
        if size:
            data = serial_object.read(size)
            print data
        else:
            print 'no data'
        time.sleep(1)

def data_sort(liveline):
    
    pattern = re.compile(r'\:([^;]*)\;')
    split_line = pattern.findall(liveline)
    data = []
    key = []

    for i in range(len(split_line)):
        
        brokendata = split_line[i].split('=')
        data.append(brokendata[1])
        key.append(brokendata[0])
        
        if key[i] == "VB" :
            print("Voltage :" + str(data[i]))

        if key[i] == "PR" :
            print("Presure :" + str(data[i]))
        


def hex2ascii(hexnum):
    
    num = hexnum.decode("hex")
    return num


def leave(userinput):
    asdf = 1

while(1): 
    """forever loop until exit function is called"""
    liveline = serial.readline
    data_sort(liveline)
    leave(userinput)
    

