a= []
for j in range(1,21):
    a.append(j)
for _ in range(10):
    b= [*map(int, input().split(' '))]
    n= ((b[1]+b[0])//2)
    print(n)
    for i in range(b[0]-1,n+1-1):# n까지 돌리고 싶으면 n+1깢 for문을 돌려야한
        mycard= a[i]
        print(i, sum(b)-2-i, a[i], a[sum(b)-2-i])
        a[i]= a[sum(b)-2-i]
        a[sum(b)-2-i]=mycard
        print(i, sum(b)-2-i, a[i], a[sum(b)-2-i])
        
    print(a)
print(*a)

'''
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

1 20
2 19
3 18
4 17
5 16
6 15
7 14
8 13
9 12
10 11
'''