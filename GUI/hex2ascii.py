def hex2ascii(hexnum):
    
    num = hexnum.decode("hex")
    return num



hexnum = "7061756c"
print hex2ascii(hexnum)