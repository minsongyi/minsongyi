'''
a= int(input())
for i in range(0,a):
    x= int(input())
    num=[[0,0],[1,1],[2,2],[5,5],[6,9],[8,8],[9,6]]

'''
num=[0]*10
num[0]=0
num[1]=1
num[2]=2
num[5]=5
num[6]=9
num[8]=8
num[9]=6
def change(y):
    y=str(y)
    y=list(y)
    #print(y)
    for k in range(0,len(y)):
        y[k]= str(num[int(y[k])])
            #print(num[i][0], y[k])
    #print(y)
    an=''
    for o in range(len(y)-1,-1,-1):
        an+=y[o]
    an= int(an)
    return(an)
Xnum= [3,4,7]    

e= int(input())
for q in range(0,e):
    x= int(input())
    for v in range(0,100000):
        a=v
        Flag=False
        fl=False
        for i in range(0, len(Xnum)):
            if a==Xnum[i]:
                Flag=True
                break
        if Flag==True:
            continue
        elif Flag== False:
            b= change(a)
            if a-b==x:
                print(a)
                fl= True
                break
        if fl==True:
            break