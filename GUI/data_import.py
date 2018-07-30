def hex2ascii(hexnum):
    
    num = hexnum.decode("hex")
    return num

#data import apply conversion 


hexnum = "7061756c"
print hex2ascii(hexnum)