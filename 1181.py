a= int(input())
L=[]
for i in range(0,a):
    b= input()
    L.append((len(b),b))
L=set(L)
L=list(L)
L.sort()
for j in range(0, len(L)):
    print(L[j][1])
