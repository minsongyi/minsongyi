a= int(input())
L=[]
for i in range(0,a):
    m,n= map(int, input().split())
    L.append((n,m))
L=set(L)
L=list(L)
L.sort()
for i in range(0, len(L)):
    print(L[i][1], L[i][0])

