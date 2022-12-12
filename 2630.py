#2447
n= int(input())
L=[]
for i in range(n):
    a= [*map(int, input().split())] 
    L.append(a)
    
white=0
blue=0

def is_same(y,x,side):
    global white,blue
    q=L[0][0]
    num=0
    for i in range(0,n):
        for j in range(0,n):
            if L[i][j]==q:
                num+=1
    if num!=n*n:
        return False
    else:
        if q==1:
            blue +=1
        else:
            white +=1
            

def rec(y,x,side):
    global white, blue
    s= side//2
    if is_same(y,x,side):
        rec(y,x,s)
        rec(y+s,x,s) 
        rec(y,x+s,s)
        rec(y+s,x+s,s)
    
if is_same(0,0,n)==False:
    rec(0,0,n)
    
# else:
#     if L[0][0]==1:
#         white=0
#         blue=1
#     else:
#         white=1
#         blue=0
        
print(white)
print(blue)