y= int(input())
x= int(input())
side= int(input())
L=[]
for k in range(0,10):
    L.append([' ']*100)

for i in range(y, y+ side):
    print('i',i)
    for t in range(x, (x + side)-(i-y)):
        print('t', t)
        L[i][t]='*'
for j in range(0, len(L)):
    print(*L[j])