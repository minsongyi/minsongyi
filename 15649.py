n,m = [*map(int, input().split())] 
L=[]
def recursion(start,num):
    if num==0:
        print(*L)
        return
    #start = 자기부터 n까지숫자 하나 선택함
    #num = 골라야하는 남은 숫자 
    for i in range(start, n+1):
        L.append(i)
        recursion(i+1,num-1)
        L.pop()
    
    
    
    
    
recursion(1,m)