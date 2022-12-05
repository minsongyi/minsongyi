n, k, i = map(int, input().split())
L=[]
L = [*map(int, input().split())]
A=['O']*n
right=i
left=i
X=L[i]
while 0<=right<n and X<=L[right]<=X+k:
    A[right]='X'
    right+=1
while 0<=left <n and X<=L[left]<=X+k:
    A[left]='X'
    left-=1
print(*A)
    