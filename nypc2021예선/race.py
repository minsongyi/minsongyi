a= int(input())
n, pl =map(int, input().split())
L= [*map(int, input().split())]
P=[]
An=[]

for i in range(0,a):
    P.append([abs(L[i]-n),-(L[i]-n),i+1])
P.sort()
for g in range(0,pl):
    An.append(P[g][2])
    
print(*An)

