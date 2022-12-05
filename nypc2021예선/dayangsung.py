a, b = map(int, input().split())
A = [*map(int, input().split())]

an = -1
AL=[]
r = 0
AN=[]
dp=[]
for i in range(a - b + 1):
    T = [] 
    for t in range(i, i + b):
        T.append( A[t] )
    


    for y in range(b):
        for h in range(y + 1, b):
            # print(abs(T[y]- T[h]))
            AL.append(abs(T[y]- T[h]))
        
    #print(AL,i)
    if r<sum(AL):
        r= sum(AL)
    AL=[]

print(r)