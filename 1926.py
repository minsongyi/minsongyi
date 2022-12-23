import sys
sys.setrecursionlimit(30000)

n,m = [*map(int, input().split())]
L=[]
for i in range(0,n):
    _= [*map(int, input().split())] 
    L.append(_)

dx=[0,0,1,-1]
dy=[1,-1,0,0]


def out_of_bound(y,x):
    global n,m
    if y<0 or y>=n:
        return True
    if x<0 or x>=m:
        return True
    return False
# out_of_bound() - type error
#out_of_bound('a','b') - type error
a=0
def rec(y,x):
    global a
    for d in range(0,4):
        ny=y+dy[d]
        nx=x+dx[d]
        if out_of_bound(ny,nx)==True:
            continue
        if L[ny][nx]==1:
            L[ny][nx]=0
            a+=1
            rec(ny,nx)
    return
d=0    
An=[]
for i in range(0,n):
    for j in range(0,m):
        if L[i][j]==1:
            a=0
            a+=1
            L[i][j]=0
            d+=1
            rec(i,j)
            An.append(a)
    
print(d)
if d==0:
    print(0)
else:
    print(max(An))
#print(max([])) ValueError: max() arg is an empty sequence 