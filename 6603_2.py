# for i in range(9):
#     for j in range(1,i):
#         print(j,i)
        
# for i in range(8,0,-1):
#     for j in range(i-1,0,-1):
#         print(j,i)
        
# for i in range(10):
#     for j in range(i):
#         for k in range(1,j):
#             print(k,j,i)
# print()
for i in range(9,0,-1):
    for j in range(i-1,0,-1):
        for k in range(j-1,0,-1):
            print(k,j,i)
            
# for i in range(11):
#     for j in range(i):
#         for k in range(j):
#             for l in range(1,k):
#                 print(l,k,j,i)