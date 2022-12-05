dic = {}


# dp = [-1] 

# dp[i] = i + !?? # 오른쪽에 해당되는 정보만 저장한다.
# dp[i + 1] = ASDF


# [ [i, ids] , [i, dsfs]]
# dp : 모든 가계가 존재하는 좌표별로, 
# 바운더리 (left, right) 만들건데, left가 그 가계의 위치로 고정이 돼 있고,
# right는 언제까지 탐색할까 모든 가계가 다 들어갈 때가지

# hash = [False]

# hash[store] = True
# n -= 1
print(300000000//500000)
n, k, m = map(int, input().split()) # 가게 수, 가게 종류, 원룸 수

for _ in range(n):
    location, name = map(int, input().split())

    if location not in dic:
        dic[location] = []
    dic[location].append(name)

store = list(dic.items())
store.sort()
# print(store)

dp = []

storeLen = len(store)
for i in range(storeLen):
    hash = [False] * (k + 1)
    remain = k
    left = store[i][0]
    right = store[i][0]

    for j in range(i, storeLen):
        loc = store[j][0] # 현 위치
        for st in store[j][1]: # 현 위치에 있는 가게들
            if hash[st] == False:
                right = loc
                hash[st] = True
                remain -= 1
        if remain == 0:
            break
    if remain == 0:
        dp.append((left, right))

#print(dp)
for i in range(0,m):
    h=int(input())
    low=h
    high=h
    an=2000000000
    for left,right in dp:
        le = min(left,low)
        ri = max(high, right)
        
        distance = ri-le

        if distance<an:
            an=distance
    print(an)






'''
4 2 3 
7 1
1 1
5 2
2 2
9 
4
3


4 3 1
1 1
2 2
8 3
9 1
5


3 3 1
5 1
5 2
5 3
5


4 2 1
1 1
2 2
4 1
5 2
3


4 2 1
-999999999 1
-999999998 2
-999999996 1
-999999995 2
-999999997
'''





# print(-1000000000 + 1)


'''

home: loc

left, right = loc, loc

ans = 1e10
for i in range(n):
    if dp[i] >=0:
        low = i
        
        ans = min(ans, max(right, high) - min(left, low))
        high = dp[i]
        
'''