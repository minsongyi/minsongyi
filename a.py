# L=[1,2]
# a=0

# a=3
# print(id(L))
# L[0]=3
# print(id(L))
# L[1]=4
# print(id(L))
# L.append(4)
# print(id(L))

# r, c = 3, 4
# L = []
# for _ in range(r):
#     L.append( [0] * c )
# print('L') 
# for i in range(0,r):
#     print(*L[i])    

# L[1][2]= 1
    
# print('L2') 
# for i in range(0,r):
#     print(*L[i])    

# M = []
# C = [0] * c
# for _ in range(r):
#     M.append( C )
    
# print('M')   
# for i in range(0,r):
#     print(*M[i]) 
    
# M[1][2]=1

# print('M2') 
# for i in range(0,r):
#     print(*M[i])    
    
# print(id(M[0][2]))
# print(id(M[1][2]))
# print(id(M[2][2]))
# print(id(C[2]))

L=[1,2,3]
M=L[:]
print(M)
print(L)
L[0]=2
print(M)
print(L)