while True:
    m,n = [*map(int, input().split())] 
    if m==0 and n==0:
        break
    L=[]
    for i in range(0,n):
        a= [*map(int, input().split())] 
        L.append(a)
    
    dx=[0,0,1,-1,1,-1,1,-1]
    dy=[1,-1,0,0,1,-1,-1,1]
    def out_of_bound(y,x):
        if y<0 or y>=n:
            return True
        if x<0 or x>=m:
            return True
        return False
    
    def rec(y,x):
        for d in range(0,8):
            ny=y+dy[d]
            nx=x+dx[d]
            if out_of_bound(ny,nx)==True:
                continue
            if L[ny][nx]==1:
                L[ny][nx]=0
                rec(ny,nx)
        return
    island=0    
    for i in range(0,n):
        for j in range(0,m):
            if L[i][j]==1:
                L[i][j]=0
                island+=1
                rec(i,j)
        
    print(island)