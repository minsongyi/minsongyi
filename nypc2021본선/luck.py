amount= int(input())
num= [*map(int, input().split(' '))]
M= max(num)
m= min(num)
distance= M-m
A=[num[0]+distance]
for i in range(1, amount):
    A.append(A[i-1]+distance)
B=[]
for k in range(0, amount):
    B.append(num[k]-A[k])
start= -10**14
if start + amount*distance <= 10**14:
    print('YES')
    print(*A)
    print(*B)
else: 
    print('NO')
    