
a= int(input())
for i in range(0,a):
    K,L,R =[*map(int,input().split(' '))]
    an=(R-L)//2
    if (R-L)%2==0 and K%2==0:
        an+=1
    if (R-L)%2!=0:
        an+=1
        if K%2==0 and R%2!=0 and L%2==0:
            an+=1
    print(an)