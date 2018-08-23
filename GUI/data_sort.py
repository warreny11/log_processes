import os
import sys
import re
import time
debug = 1

def convert(liveline):
    
    pattern = re.compile(r'\:([^;]*)\;')
    split_line = pattern.findall(liveline)
    data = []
    key = []
    strdata = []

    for i in range(len(split_line)):
        
        brokendata = split_line[i].split('=')
        data.append(brokendata[1])
        key.append(brokendata[0])
        
        try:
            data[i] = int(data[i],16)
            err = ""
            strdata = str(key[i]) + " = " + str(data[i])
            # return strdata
            
        except:
            data[i] = 0
            err = "NaN"
            strdata = str(key[i]) + " = " + str(err)
            # return strdata
        

        if debug == 0:
            if key[i] == "VB" :    
                print '{0}\r'.format("Voltage : " + str(data[i]*0.001+0) + err + " Volts")
                
            if key[i] == "PR" :
                print '{0}\r'.format("Pressure : " + str(data[i]*1+0) + err + " Pascals")

            if key[i] == "IP" :
                print '{0}\r'.format("Internal Pressure : " + str((data[i]*.25+0)*0.00750062) + err + " mm of mercury")
    
        if debug == 1:
                time.sleep(.1)
                print "\033[7A\033[1;35m HELLO \033[7B\033[6D"
                
                
# # # #wish list: db connection to data_sort for pulling the 

# # convert(":EV=01;:PR=0000;:PM=0000;:IP=0006130A;:RN=0000;:VB=0000;:VG=0000;:VC1=0000;:VC2=0000;:VC3=0000;:VC4=0000;:VC5=0000;:VC6=0000;:CB=0000;:CH=0000;:CG=0000;:SCD=0000;:ST=00000000;:RT=0000;:RS=00;:TS=00003BB4;:T16=0039;:TN=FFFE;:TH=FFFE;:TG=FFFE;:TB2=0000;:TB1=0000;:TC=0198;:ML=0000;:EC=0000;:ET=0000;:EI=0000;:FF=000558C0;:QC=FFFFFFFF;:CVB=00;:UB=0012;:QG=0000;:QB=0000;:EE=01;:HE=00;:BT=00152509;:BD=00180518;:FR=0101;:CVT=FFFFFFFF;:RE=0000;:SE=0000;:TIM=0000;:DE=07;:DEC=0050;:HEC=0057;:IO=0010;:SU=94;:EV=02;:PR=0000;:RN=0000;:SCD=0000;:ST=00000000;:RT=0000;:TS=00008640;:TC=0198;:EC=0000;:ET=0000;:EI=0000;:FF=00055AC6;:QC=FFFFFFFF;:CVB=00;:EE=03;:CVT=FFFFFFFF;:DEC=00A2;:HEC=00A9;:SU=90;download complete; checksum = 0x0000A035")
