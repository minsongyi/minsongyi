L=[]
AN=[]
n=0
a= int(input())
for  i in range(0,a):
    b= input()
    L.append(b)
for k in range(0, len(L)):
    for j in range(0, len(L[k])):
        AN.append((0,L[k][j]))
AN=set(AN)
AN=list(AN)
##print(AN)
for k in range(0, len(L)):
    for j in range(0, len(L[k])):
        for  h in range(len(AN)):
            if L[k][j]==AN[h][1]:
                AN[h]=list(AN[h])
                AN[h][0]-=10**(len(L[k])-j-1)
                AN[h]=tuple(AN[h])
                #print(AN[h])
an=0
AN.sort()
#print(AN)
for i in range(len(AN)):
    an-=(9-i)*AN[i][0]
    #print(an)
print(an)
