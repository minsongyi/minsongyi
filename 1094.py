x= int(input())
def f(x,long,many,a):
    L=[64,32,16,8,4,2,1]
    
    if long + L[a]==x:
        print(many)
        
    elif long + L[a] <x:
        long+= L[a]
        f(x,long, many+1, a+1)
    else:
        f(x, long, many, a+1)

f(x,0,1,0)        