l= int(input())
L=[]
for  _ in range(0,l):
    a= input().split(' ')
    L.append([-int(a[1]), int(a[2]), -int(a[3]), a[0]])
L.sort()
for i in range(0,l):
    print(L[i][3])