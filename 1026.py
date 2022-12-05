n= int(input())
A=[*map(int, input().split(' '))]
B=[*map(int, input().split(' '))]

A.sort()
B.sort()
a=0
for i in range(0,n):
    a= a + A[i]*B[n-(i+1)]
print(a)