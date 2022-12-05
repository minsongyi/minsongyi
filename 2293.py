n, k=[*map(int, input().split())] 
coins=[]
for i in range(0,n):
    c= int(input())
    coins.append(c)
no= 0
h=[no]*(k+1)#h[i]는 i를 만들 수 있는 경우의 수
h[min(coins)]=1
h[0]=0
for i in range(1,min(coins)):
    h[i]=no
    
    
for i in range(0,k+1):
    if h[i]!=no:
        for j in range(0,n):
            if i+coins[j]<k+1:
                
                # if h[i]+1 < h[i+coins[j]]:
                #     h[i+coins[j]]= h[i]+1
if h[k]==no:
    print(-1)
else:
    print(h[k])