n,k=[*map(int, input().split())] 
L=[*map(int, input().split())] 
L.sort()
Max=int(str(L[-1])*len(str(n)))
answer=0
def number(num):
    global answer,n,k
    if  num<=n :
        answer=max(answer,num)
    if num>=Max and num>=10**k:
        return
    
    for i in range(0,k):
        num=num*10+L[i]
        #print(num)
        number(num)
        num= (num-L[i])//10
    

num=0
number(num)
print(answer)
    
'''
100000000 1
1

111 3
2 3 4
'''