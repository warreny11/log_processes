import os, pty, serial

master, slave = pty.openpty()
s_name = os.ttyname(slave)

ser = serial.Serial(s_name)

# To Write to the device
ser.write('Your text')
print("hi")
if ser.is_open:
    print "hey"

# To read from the device
print os.read(master,1000)
