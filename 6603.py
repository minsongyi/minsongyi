
start=True
while True:

    L= [*map(int, input().split())] 
    if L[0]==0:
        break
    
    if not start:
        print()
    
    start=False
    
        
    k,L=L[0],L[1:]
    L.sort()
    # H=[0]*k
    A=[]

    def lotto(nth,_to,S):# lotto는 to에서 끝까지 가능한 숫자를 표시했다 지웠다가
        global k
        if nth==k-6:
            ##############
            A=[]
            for i in range(0,len(S)):
                if S[i]==1:
                    continue
                else:
                    A.append(L[i])
            print(*A)

            #print(S)
            
            #############
            
        if _to>=len(L):
            return
        
        for i in range(len(L)-1,_to-1,-1):
            S[i]=1
            
            # S.append(i)
    
            lotto(nth+1,i+1,S)
            S[i]=0
            
            
    lotto(0,0,[0]*k)
    