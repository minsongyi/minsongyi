a= input()
a=a.split(' ')
n=int(a[0])
k=int(a[1])

L = [*map(int, input().split())]

def burst(i): # i 번째 물풍선 터트리면 왼쪽 오른쪽으로 얼마나 터지는지 알려준다
    global k
    lower, upper = L[i], L[i] + k
    left, right = i, i

    while 0 <= left - 1 and lower <= L[left - 1] <= upper:
        left -= 1

    while right + 1 < n and lower <= L[right + 1] <= upper:
        right += 1

    return (left, right)

dp = [0] * n




dic = {}

def rec(lo, hi):
    if lo == hi:
        return 1
    elif hi < lo:
        return 0
    if (lo, hi) in dic:
        return dic[(lo, hi)]
    ans = 1e9
    for i in range(lo, hi):
        left, right = dp[i]
        ans = min(ans, rec(lo, left -1) + rec(right + 1, hi) + 1)
    dic[(lo, hi)] = ans
    return ans

an, ans = 1e9, 1e9

o=-1
if k==0:
    an = 0
    for i in range(0, n):
        if o!=L[i]:
            an+=1
            o=L[i]
    print(an)
    exit(0)
            
elif n <= 100:
    for i in range(n):
        dp[i] = burst(i)
    ans = rec(0, n-1)
    
print(min(an, ans))