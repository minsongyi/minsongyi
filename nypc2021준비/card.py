import sys; input = lambda: sys.stdin.readline().rstrip()
a= int(input())
p=[]
An=[]
L=[]
for i in range(0,a):
    b= int(input())
    L.append(b)
A={}
for i in range(0, a):
    if L[i]-1 in A:
        A[L[i]-1]+=1
    else:
        A[L[i]-1]=1
for i in A.values():
    An.append(i)
    #print(An)
ma=max(An)
for k,v in A.items():
    if v== ma:
        p.append(k+1)
print(min(p))
    