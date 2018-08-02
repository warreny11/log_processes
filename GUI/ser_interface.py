import serial
import time
import sys


def connect(p,b): 
    global serial_object

    if p=="/dev/tty.usbserial" and b==9600:
        serial_object = "connected"
    while serial_object=="connected":
        return 0
    else:
        return -1                                                      #0 is connected, -1 is not connected            
    

def commands():
    global serial_object
    while serial_object=="connected":
            cmd = raw_input()
            
            if cmd == " ":
                print("RN")   
                                                    #prints current data              
            elif cmd == "a":
            
                while True:
                    data = ":EV=01;:PR=0000;:PM=0000;:IP=0006130A;:RN=0000;:VB=0000;:VG=0000;:VC1=0000;:VC2=0000;:VC3=0000;:VC4=0000;:VC5=0000;:VC6=0000;:CB=0000;:CH=0000;:CG=0000;:SCD=0000;:ST=00000000;:RT=0000;:RS=00;:TS=00003BB4;:T16=0039;:TN=FFFE;:TH=FFFE;:TG=FFFE;:TB2=0000;:TB1=0000;:TC=0198;:ML=0000;:EC=0000;:ET=0000;:EI=0000;:FF=000558C0;:QC=FFFFFFFF;:CVB=00;:UB=0012;:QG=0000;:QB=0000;:EE=01;:HE=00;:BT=00152509;:BD=00180518;:FR=0101;:CVT=FFFFFFFF;:RE=0000;:SE=0000;:TIM=0000;:DE=07;:DEC=0050;:HEC=0057;:IO=0010;:SU=94;:EV=02;:PR=0000;:RN=0000;:SCD=0000;:ST=00000000;:RT=0000;:TS=00008640;:TC=0198;:EC=0000;:ET=0000;:EI=0000;:FF=00055AC6;:QC=FFFFFFFF;:CVB=00;:EE=03;:CVT=FFFFFFFF;:DEC=00A2;:HEC=00A9;:SU=90;download complete; checksum = 0x0000A035"
                    print data

                    if cmd == "s": 
                        break

            elif cmd == "e":    
                print("exiting program and disconnecting from serial")    #e: exit hotkey
                serial_object=="disconnected" 
                sys.exit()

            else:                                                         #all other commands are sent to serial
                print(cmd)





