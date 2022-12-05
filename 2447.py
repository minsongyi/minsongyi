n= int(input())
L=[]
for i in range(0,n):
    L.append(['*']*n)
    
def draw_white(y,x,side):
    for  i in range(y,y+side):
        for j in range(x,x+side):
            L[i][j]=' '
            
def rec(y,x,side):
    if side<3:
        return
    T=side//3
    
    draw_white(y+T,x+T,T)
    rec(y,x,T)
    rec(y+T,x,T)
    rec(y+2*T,x,T)
    
    rec(y,x+T,T)
    rec(y+ 2*T,x+T,T)
    
    rec(y,x+2*T,T)
    rec(y+T,x+2*T,T)
    rec(y+2*T,x+2*T,T) 
    
rec(0,0,n)
for i in range(0,len(L)):
    print(''.join(L[i]))