a= int(input())
b=[*map(int, input().split(' '))]
b.sort()
AN=[]
for i in range(0,a):
    an=0
    for t in range(0,i+1):
        an+=b[t]
    AN.append(an)

print(sum(AN))