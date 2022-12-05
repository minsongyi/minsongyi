a= int(input())
an=0
L=[]
while True:
    for i in range(a//5,-1,-1):
        if (a-5*i)%3==0:
            an=(i+(a-5*i)//3)
            print(an)
            break
            
    if an==0:
        print(-1)
    break
    
'''
if a%3==0:
    L.append(a%3)
elif a%5==0:
    L.append(a%5)
elif a%5!=0 and  a%3!=0:
    an+=(a//5)
    an+=((a%5)//3)
    if ((a%5)%3)!=0:
        L.append(-1)
    else: 
        L.append(an)
elif a%5!=0 and  a%3!=0:
    an+=(a//3)
    an+=((a%3)//5)
    if ((a%3)%5)!=0:
        L.append(-1)
    else: 
        L.append(an)

print(min(L))
'''