k=int(input())
m,n= map(int, input().split())
m1,k1= m, k
h=0
f=0
if k<m:
    while True:
        m=m%k
        if m==0:
            h=k
            break
        k=k%m
        if k==0:
            h=m
            break
    f=(k1*m1)//h
elif m<k:
    while True:
        k=k%m
        if k==0:
            h=m
            break
        m=m%k
        if m==0:
            h=k
            break
    f=(k1*m1)//h
#print(h)
#print(f)

if (n-f)% n==0:
    a= f//k1+(n-f)//m1
elif (n-f)% n!=0:
    a= f//k1+((n-f)//m1) +1
elif m>n:
    a= n//k +1
print(a)