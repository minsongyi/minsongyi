
n= int(input())
side= 2**n

L=[]
for i in range(0,side):
    L.append([' ']*side)
L[0][0]='*'

# M=[['*','*'],['*',' ']]
# # for i in range(0,len(M)):
# #     print(*M[i])
    
# y,x=2,2
# for i in range(y,y+len(M)):
#     for j in range(x,x+len(M[0])):
#         L[i][j]=M[i-y][j-x]

# for i in range(0,len(L)):
#     print(*L[i])
    
C=['*']
# for i in range(0,len(L)):
#     C.append(L[i][:])
    
# for i in range(0,len(C)):
#     print(*C[i])
    
def draw(y,x,move):
        
    #print(f'draw{y},{x},{move}')
    for i in range(y,y+len(C)):
        for j in range(x,x+len(C[0])):
            L[i][j]=C[i-y][j-x]
            
    y2,x2=y+move,x
    
    for i in range(y2,y2+len(C)):
        for j in range(x2,x2+len(C[0])):
            L[i][j]=C[i-y2][j-x2]

    y3,x3 = y, x+move
    for i in range(y3,y3+len(C)):
        for j in range(x3,x3+len(C[0])):
            L[i][j]=C[i-y3][j-x3]
            
for i in range(0,n):
    C=[]
    for k in range(0,2**(i)):
        C.append(L[k][:2**(i)])
        
    draw(0,0,2**i)
           
    
for i in range(0,len(L)):
    for j in range(len(L)-i,len(L)):
        L[i][j]=''
        
for i in range(0,len(L)):
    a=''.join(L[i])
    print(a)