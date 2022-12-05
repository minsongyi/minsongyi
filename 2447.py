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
    three=side//3
    
    draw_white(y+three,x+three,three)
    

rec(0,0,n)
for i in range(0,len(L)):
    print(*L[i])