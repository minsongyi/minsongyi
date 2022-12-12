#2447
n= int(input())
L=[]
for i in range(n):
    a= [*map(int, input().split())] 
    L.append(a)
    
white=0
blue=0

def is_not_same(y,x,side):
    global white,blue
    q=L[y][x]
    num=0
    for i in range(y,y+side):
        for j in range(x,x+side):#돌리는 범위를 생각하지 않음 같아야하는 개수를 잘못 생각함
            if L[i][j]==q:
                num+=1
    if num!=side*side:
        return True
    else:
        if q==1:
            blue +=1
        else:
            white +=1
        return False

def rec(y,x,side):
    global white, blue
    s= side//2
    if is_not_same(y,x,side):
        # print(y, x, side)
        # if y+x+side ==0:
        #     exit()
        rec(y,x,s)
        rec(y+s,x,s) 
        rec(y,x+s,s)
        rec(y+s,x+s,s)
    
if is_not_same(0,0,n)==True:
    rec(0,0,n)
    
else:
    if L[0][0]==1:
        white=0
        blue=1
    else:
        white=1
        blue=0
        
print(white)
print(blue)