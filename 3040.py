L=[]
for i in range(9):
    a= int(input())
    L.append(a)
an=sum(L)
n= an-100
for i in range(0,9):
    for j in range(0,9):
        if i!=j and L[i]+L[j]==n:
            L[i]=''
            L[j]=''
            for o in range(0, len(L)):
                if L[o]!='':
                    print(L[o])
            exit()
