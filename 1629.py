## (A**B)%C

A,B,C= [*map(int, input().split())] 

def multiple(a,b):
    global C
    answer=1
    if b==1:
        answer=a
    elif b%2==0:

        answer=(multiple(a,b//2)**2)%C
    elif b%2==1:
        answer=(multiple(a,b//2)**2)%C
        b=b-1

        answer*=a
    return(answer)

print(multiple(A,B)%C)