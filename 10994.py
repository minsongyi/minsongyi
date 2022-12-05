import time
n= int(input())
side=1+(n-1)*4

L=[]
for i in range(0,side):
    L.append([' ']*side)
    
def draw(y,x,a):
    # print(f'draw{y},{x},{a}')
    for i in range(y,y+a):
        for j in range(x,x+a):
            L[i][j]='*'
            
    y2,x2,b=y+1,x+1,a-2
    for i in range(y2, y2+b):
        for j in range(x2, x2+b):
            L[i][j]=' '
            
    # for i in range(0, len(L)):
    #     c=''.join(L[i])
    #     print(c)   
        
    # time.sleep(2)
    if a-4>0:
        draw(y+2,x+2,a-4)
    

    
draw(0,0,side)   

for i in range(0, len(L)):
    a=''.join(L[i])
    print(a)