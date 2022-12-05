n, m =[*map(int, input().split(' '))]
L=[]
A=[*map(int, input().split(' '))]
B=[*map(int, input().split(' '))]
e=0
r=0
while True:
    if n==e:
        for i in range(r, m):
            L.append(B[i])
        break
    elif m==r:
        for k in range(e,n):
            L.append(A[k])
        break
    if A[e] < B[r]:
        L.append(A[e])
        e+=1
    elif A[e]>B[r]:
        L.append(B[r])
        r+=1
    else:
        L.append(B[r])
        L.append(A[e])
        e+=1
        r+=1
    
print(*L)