n, m =[*map(int, input().split(' '))]
M=[*map(int, input().split(' '))]
N=[*map(int, input().split(' '))]
L=[]
for i in range(0,n):
    L.append([M[i],i+1])
for k in range(0,m):
    h=''
    L.sort(reverse=True)
    while L and L[-1][0]==0:
            L.pop() 
    for t in range(0,(min(len(L),N[k]))):
        h+=str(L[t][1])+' '
        L[t][0]=L[t][0]-1
    print((min(len(L),N[k])), h)
    

