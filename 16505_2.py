a= int(input())
L=[]
for k in range(0,2**10):
    L.append([' ']*2**10)
L[0][0]=='*'
if a==0:
    print('*')
    exit()
elif a==1:
    print('''**
*''')
    exit()
S=[]
for k in range(0,2**10):
    S.append([' ']*2**10)
L[0][0]='*'
L[0][1]='*'
L[1][0]='*'

S[0][0]='*'
S[0][1]='*'
S[1][0]='*'

for l in range(2, a + 1):
    side = (2**(l-1))
    # print(side, 0, 2**(l-1))
    # print(side, 2**(l-1), 0)
    for k in range(0, 0 + side):
        for i in range(2**(l-1), (2**(l-1)) + side):
            L[k][i]=S[k][i - (2**(l-1))]
            #print(i - (2**(l-1)), ',', k, i)
            #print(len(S[0]), len(L[0]), len(S), len(L))
    for s in range(2**(l-1), (2**(l-1)) + side ):
        for t in range(0, 0 + side):
            L[s][t]=S[s-(2**(l-1))][t]
       
    for k in range(0,2**10):  
        S[k]=L[k][:]
an=''
for i in range(0, 2**a):
    an=''
    for k in range(0, 2**a-i): # 
        an+=L[i][k]
    print(an)