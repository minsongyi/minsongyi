

def get_p(A,B):
    b=round(A[-1]**(1/2))
    c=round(B**(1/2))
    if b==1 or b<=c:
        return A
    else:
        A=A+[b]
        return get_p(A,B)
        
def comp(A,B):
    zero=abs(B-A)
    if B>A:
        b=int(B**(1/2))
        bb=b+1
        one=abs(A-b)+abs(B-b*b)+1
        two=abs(A-bb)+abs(B-bb*bb)+1

        res=min(zero,one,two)

    elif B<A:
        a=int(A**(1/2))
        aa=a+1
    
        one=abs(a-B)+abs(A-a*a)+1
        two=abs(aa-B)+abs(A-aa*aa)+1

        res=min(zero, one,two)
    else:
        res=zero
        

    return res

a= int(input())
for i in range(0,a):
    A,B=[*map(int,input().split(' '))]

    if A<B:
        temp=A
        A=B
        B=temp
        
    a=get_p([A],B)
    st=a[0]
    L=a[1:]+[B]
    n=0
    for i in L:
        n=n+comp(st,i)
        st=i
        
    print (n)
    
    
