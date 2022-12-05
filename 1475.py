n= [*map(int,input())]
L=[0]*11
for i in range(0,len(n)):
    L[n[i]]+=1

L[10]=((L[9]+L[6])//2+(L[9]+L[6])%2)
L[6]=0
L[9]=0

print(max(L))