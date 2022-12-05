n,m =[*map(int, input().split())]
L=[]
for _ in range(0,n):
    a= [*map(int, input().split())]
    L.append(a)
#print(L)
times=int(input())
for q in range(0,times):
    an=0
    b= [*map(int, input().split())]
    for k in range(b[0]-1, b[2]):
        for i in range(b[1]-1, b[3]):
            print(L[k][i])
            an+= L[k][i]
    print(an)