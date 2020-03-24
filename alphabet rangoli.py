def print_rangoli(size):
    
    letters = list('abcdefghijklmnopqrstuvwxyz')
    nlet = letters[0:size]
    nlet.reverse()    
    
    n = 4*size -3
    
    for i in range(size):
        s =  nlet[:i+1] + nlet[:i][::-1]
        centered = ('-'.join(filter(None,s))).center(n,"-")
        
        print(centered)
        
    for i in reversed(range(0,size-1)):
        s =  nlet[:i+1] + nlet[:i][::-1]
        centered = ('-'.join(filter(None,s))).center(n,"-")
        
        print(centered)
    

print_rangoli(10)
