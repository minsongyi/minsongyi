n=int(input())
stick=[*map(int, input().split(' '))]
hash=[n*2+1]*(n+1)
an=0
#1 2 3 2 1 4 4 3
for i in range(0,n*2):
    if hash[stick[i]]!=n*2+1:
       # print(stick,an)
        for t in range(hash[stick[i]]+1,i):
            if stick[t]!=0:
                an+=1
         
        an+=1
             
        stick[hash[stick[i]]]=0
        stick[i]=0
        #print(stick,an)
        #print()

    else:        
        hash[stick[i]]=i


print(an+1)
