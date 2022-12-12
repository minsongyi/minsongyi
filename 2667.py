import sys
sys.setrecursionlimit(25000)

n= int(input())
L=[]
for i in range(0,n):
    a= [*map(int, input().split())] 
    L.append(a)
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def out_of_bound(y,x):
    if y<0 or y>=n:
        return True
    if x<0 or x>=n:
        return True
    return False

def rec(y,x):
    for d in range(0,4):
        ny=y+dy[d]
        nx=x+dx[d]
        if out_of_bound(ny,nx)==True:
            continue
        if L[ny][nx]==1:
            L[ny][nx]=0
            rec(ny,nx)
    return
building=0    
for i in range(0,n):
    for j in range(0,n):
        if L[i][j]==1:
            L[i][j]=0
            building+=1
            rec(i,j)
    
print(building)