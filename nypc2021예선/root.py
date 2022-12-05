
# # a -> b 일 때 b는 루트가 될 수 없다.
# # b가 루트가 될 수 없음이 확인 됐다면,
# # a가 아닌, b와 연결된 모든 정점은 루트가 되지 못한다.
# n= 정점
# 간선 개수= n-1
# 방향이 있다=1
# 방향이 없다 =0


# 1일 경우인 정점은
# 5->6 일 경우 6은 루트가 아니고
# 5이 아닌 6와 연결 된 모든 정점ㅇ,ㄴ 루트가 될수 없다 

# 8-1-1

n = int(input())

edge = []

for _ in range(n + 1):
    edge.append([])

tst = []

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    # a = 5 b = 2 c = 0
    if c == 0:#방향이 없다
        #조거을 안 봐도 됨
        edge[a].append( (b, c) )
        edge[b].append( (a, c) )
    elif c == 1:#방향이 잇다
        #조건을 봐야한다.
        tst.append( (a, b) )
        edge[a].append( (b, c) )
        edge[b].append( (a, 2) )


vis = [False] * (n + 1)

def dfs(v, v1):
    # print(v, v1)
    res = True
    for v2, d in edge[v]:
        # print(v2, d)
        if v1 == v2:
            continue
        if vis[v2]:
            continue
        if d > 1:
            return False
        vis[v2] = True
        res &= dfs(v2, v)
    return res

 # a -> b 일 때 b는 루트가 될 수 없다.(#1)
 # b가 루트가 될 수 없음이 확인 됐다면,(#2)
 # a가 아닌, b와 연결된 모든 정점은 루트가 되지 못한다.(#3)
def judge():
    ans = 0
    for v, v2 in tst:#검사할게 다 들어가 있다. v=3 (->) v2=1   (#1)
        vis[v2] = True#2
        # 열심히 연락 한다.
        # print(v, v2)
        if not dfs(v2, v):#3
            return 0#답이 없을때(연락을 돌리는데 자기가 루트를 하겠다고 할때)
    for i in range(1, n + 1):#루트가 될 수 있는 경우 세기
        if not vis[i]:#가위표 안 칠한 얘들
            ans += 1
    return ans

ans = judge()

print(ans)