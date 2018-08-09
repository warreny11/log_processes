import serial

port = "/dev/tty.usbserial"
baud = 9600

ser = serial.Serial(str(port), baud)

while ser.is_open:
    ser.write(raw_input())