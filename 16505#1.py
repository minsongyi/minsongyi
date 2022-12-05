# y,x, s= [*map(int, input().split(' '))]
  
import time  
def triangle( y, x, s):
    for i in range(y, y+s):
        for t  in range(x,x+s-(i-y)):
            L[i][t]='*'
    for j in range(y+1, y+s-1):
        for h in range(x+1, x+s-(j-y)-1):
            L[j][h]=' '
         
    half = s // 2
    
    for i in range(0, len(L)):
        print(*L[i])    
        
    time.sleep(1)
    triangle( y, x , half)
    triangle(y+ half, x, half)
    triangle(y, x+half, half)
  
  
  
s = int(input())
L=[]
for k in range(0, 2**s):
    L.append([' ']*2**s)
    
              
triangle(0,0,2**s)
for i in range(0, len(L)):
    print(*L[i])    
            