import time

n, k=[*map(int, input().split())] 
coin=[]
for i in range(0,n):
    c= int(input())
    coin.append(c)
no= 0
#dp[i] = i원을 만들수있는 경우의 수
dp=[0]*(k+1) 

dp[0]=1

for i in range(0,n):
    print(coin[i],'원')
    for  j in range(0,k+1):
        if dp[j]>0 and j+coin[i]<=k:
            dp[j+coin[i]]+=dp[j]
        time.sleep(1)
        print(f' dp[{j+coin[i]}] = {dp[j+coin[i]]}')
print(dp[k])