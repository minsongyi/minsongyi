while True:
    a= input()
    if a=='.':
        exit()
    an=[]
    b=[]
    for  i in range(0,len(a)):
        if a[i]== '[' :
            an.append('[')
        elif a[i]=='(':
            an.append('(')
            
        elif a[i]==']':
            if len(an)!=0:
                continue
            else:
                if an[len(an)-1]=='[':
                    an.pop(len(an)-1)
            
        elif a[i]==')':
            if len(an)!=0:
                continue
            elif an[len(an)-1]=='(':
                an.pop(len(an)-1)
    if len(an)!=0:
        print('no')
    else:
        print('yes')