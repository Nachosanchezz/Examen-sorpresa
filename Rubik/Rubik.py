def cube(n):
    fu = '/\\' 
    fl = '\\/' 
    t = '_\\'  
    r = '_/'  
    
    ret = ''
    for row in range(n):
        ret += (n-row-1)*' ' + (row+1)*fu + n*t + '\n'
    for row in reversed(range(n)):
        ret += (n-row-1)*' ' + (row+1)*fl + n*r + '\n'
        
    return ret[:-1]