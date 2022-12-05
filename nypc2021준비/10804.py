'''
히니 씩 보먄서 for문 사용하면서 돌려서 집어넣기


card=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for _ in range(0,10):
    a= [*map(int, input().split(' '))]
    if (a[1]-a[0])%2==0:
        n = a[0]+(a[1]-a[0])//2
        #print(n)
    else:
        n= a[0]+((a[1]-a[0])+1)//2-1
        #print(n)
    for i in range(a[0], n+1 ): 
        mcard=card[i-1]

        card[i-1]=card[(sum(a)-i)-1]
        card[(sum(a)-i)-1]= mcard
        
        #print(mcard,i-1, (sum(a)-i)-1 )
    #print(*card)
    #print()
print(*card)
'''
a= [*map(int, input().split(' '))]
n = len(a)//2

for i in range(0, n):
    mcard=a[i]
    a[i]=a[(len(a)-1-i)]
    a[(len(a)-1-i)]=mcard
    #print(a)
print(a)