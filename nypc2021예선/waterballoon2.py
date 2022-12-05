n, k=map(int,input().split())
L=[]

P=[]
L=[*map(int, input().split())]
for y in range(0,n):
    P.append((L[y],y))
P.sort()
#print(P)
#print(L)

A=['O']*n
an=0
i=0
for  g in range(0,n):
    if A[P[g][1]]=='O':
        #print(g)
        i=P[g][1]
        r=i
        l=i
        X=P[i][0]
        #print(X)
        #print(X+k)
        #print(k)
        A[P[g][1]]='X'
        print(i)
        while 0<= l-1 <n and X<=L[l-1]<=X+k:
            l-=1
            A[l]='X'
        while 0<=r+1<n and X<=L[r+1]<=X+k:
            r+=1
            A[r]='X'
        an+=1
        print(A)
print(an)


