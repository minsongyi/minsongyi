n, m= map(int, input().split())
L=[*map(int, input().split())]
AL=[]
an=(max(L))
for k in range(0,n):
    AL.append([L[k], k+1])
if m==1:
    A=[]
    if L.count(an)==1:
        print(L.index(an)+1)
        exit(0)
    elif L.count(an)!=1:
        for k in range(0,n):
            if L[k]==an:
                A.append(k+1)
        print(max(A))
        exit(0)
here=-1
for i in range(0, sum(L)):
    here= (here+m)%n
    #print(here)
    AL[here][0]=AL[here][0]-1
    if AL[here][0]==0:
        AL.pop(here)
        n=n-1
        here-=1
    if len(AL)==1:
        print(AL[0][1])
        break
    #print(AL)
