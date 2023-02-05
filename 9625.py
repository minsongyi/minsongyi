'''
A            10
B            01
BA           11
BA B         12 
BA B BA      23
BA B BA B AB 35
'''

k= int(input())
A=[0]*46
B=[0]*46
A[0]=1
A[1]=0
B[0]=0
B[1]=1

for i in range(2,k+1):
    A[i]= A[i-1]+A[i-2]
    B[i]=B[i-1]+B[i-2]
    
print(A[k],B[k])
    