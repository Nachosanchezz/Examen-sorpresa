def rgb(r, g, b):
    pass # your code here
#print(r, g, b)
    
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return "{:02X}{:02X}{:02X}".format(r, g, b)
    
    

