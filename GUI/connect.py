import serial

def connect(a,b): 

    global serial_object
    serial_object = serial.Serial(str(a), b)
    while serial_object.is_open:
        return 0
    else:
        return -1 



