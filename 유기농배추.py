t= int(input())
for _ in range(t):
    L=[]
    m,n,k=[*map(int, input().split())] 

    for i in range(0,n):
        L.append([0]*m)
        
    for i in range(0,k):
        a,b = [*map(int, input().split())] 
        L[b][a]=1
        
    def rec(y,x):
        return
    worm=0    
    for i in range(0,n):
        for j in range(0,m):
            if L[i][j]==1:
                worm+=1
                rec(i,j)
        
    print(worm)