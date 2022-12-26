n,d =[*map(int, input().split())] 
M=[0]*10
s=0
for i in range(1,n+1):
    s=0
    while True:
        if (i//(10**s))==0: # 여기가 문제인것같음
            break
        else:
            #print(i,(i//(10**s))%10)
            M[(i//(10**s))%10]+=1
            s+=1

print(M[d])
#print(M)
        
    
'''
(a//1000)%10
(a//100)%10
(a//10)%10
'''
