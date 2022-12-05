n= int(input())
a=[*map(int, input().split())]

AN=[]
for k in range(0,n):
    r=0
    t=0
    for i in range(0,n*2):
        if a[i]==k and t==0:
            t+=1
            print('y')

        elif a[i]!=k and t==1:
            r+=1
            print('o')

        elif a[i]==k and t==1:
            print('f')
            
    AN.append(r)
    
if sum(AN)*2==0:
    print(n+1)
else:
    print(AN)
    print(sum(AN)*2)