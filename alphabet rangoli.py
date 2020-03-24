def print_rangoli(size):
    
    letters = list('abcdefghijklmnopqrstuvwxyz')
    nlet = letters[0:size]
    nlet.reverse()    
    
    n = 4*size -3
    
    for i in range(0,size):
        s = '-'.join(nlet[:i]) + "-" + nlet[i] + "-" + '-'.join(nlet[:i][::-1])
        centered = s.center(n,"-")
        
        print(centered)
        
    for i in reversed(range(0,size-1)):
        s = '-'.join(nlet[:i]) + "-" + nlet[i] + "-" + '-'.join(nlet[:i][::-1])
        centered = s.center(n,"-")
        
        print(centered)
    
n = 10
print_rangoli(10)
