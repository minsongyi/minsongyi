import sys
sys.setrecursionlimit(25000)

t= int(input())
for _ in range(t):
    L=[]
    m,n,k=[*map(int, input().split())] 

    for i in range(0,n):
        L.append([0]*m)
        
    for i in range(0,k):
        a,b = [*map(int, input().split())] 
        L[b][a]=1
        
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    def out_of_bound(y,x):
        if y<0 or y>=n:
            return True
        if x<0 or x>=m:
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
    worm=0    
    for i in range(0,n):
        for j in range(0,m):
            if L[i][j]==1:
                L[i][j]=0
                worm+=1
                rec(i,j)
        
    print(worm)