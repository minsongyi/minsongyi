def half(a):
    L=[]
    h=int(len(a)/2)
    for i in a[:h]:
        if i==0:
            L.append(1)
        else:
            L.append(0)
    return (L+a[h:])        


def f(x):
    lenx=len(x)
    half_l=int(lenx/2)
    if lenx==1:
        L=x
    else:
        l=x[:half_l]
        r=x[half_l:]
        new_l=half(l)
        new_r=half(r)
        L=f(new_l)+f(new_r)
    return L


T=int(input())

for i in range(0,T):
    K,L,R =[*map(int,input().split(' '))]
    n=2**K
    k=[0]*n

    kk=half(k)
    L=f(kk)
    #print (L)


    f=L[L-1:R]
    an=sum(f)
    print (an)