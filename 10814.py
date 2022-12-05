a= int(input())
L=[]
for i in range(0,a):
    n, pl =input().split()
    L.append((int(n) , i ,pl ))
L.sort()

for i in range(0,a):
    print(L[i][0], L[i][2])