
L=[0,1]
def a(x):
    print(f'a{x}')
    if x<=1:
        return L[x]
    else:
        return a(x-1)+a(x-2)
    
n = int(input())
print( a(n) )