import serial
from data_sort import convert

def Autoprint():
    ser = Connection.connect()
    rxstr = ''
    while (1):
        
        out = ''
        out += ser.read()
        rxstr += out
        #if out != '':
#            print (out)
        if out == ';':
            convert(rxstr)
            rxstr = ''

def serwrite(my_input):
    ser = connect()
    ser.write(my_input)

