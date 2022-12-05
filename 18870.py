a= int(input())
e= [*map(int, input().split(' '))]
x=[]
An=[]
for i in range(0,a):
    x.append(e[i])
b={}
e=set(e)
e=list(e)
e.sort()
for i in range(0,len(e)):
    b[e[i]]=i
for k in range(0,a):
    if x[k] in b:
        An.append(b[x[k]])

print(*An)