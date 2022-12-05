board=[]
for i in range(0,5):
    a=[*map(int, input().split())]
    board.append(a)
numbers=[]
for k in range(0,5):
    b= [*map(int, input().split())]
    numbers.append(b)
an = 0


def delete(num):
    for o in range(0,5):
        for g in range(0,5):
            if num==board[o][g]:
                board[o][g]='X'
                return [o, g]
                
def updown(y,x):
    flag=True
    for k in range(y,5):
        if board[k][x]!='X':
            flag=False
            break
    for n in range(y,-1,-1):
        if board[n][x]!='X':
            flag=False
            break
    if flag==True: 
       return True
    return False

def leftright(y,x):
    flag=True
    for k in range(x,5):
        if board[y][k]!='X':
            flag=False
            break
    for n in range(x,-1,-1):
        if board[y][n]!='X':
            flag=False
            break
   
    if flag==True:
        return True
    return False

def cross():
    count = 0
    flag=True
    for i in range(0,5):
        if board[i][i]!='X':
            flag=False
            break
    if flag==True:
        count += 1
    return count

def cross2():
    flag=True
    count = 0
    for h in range(4,-1,-1):
        if board[4-h][h]!='X':
            flag=False
            break
    if flag==True:
        count += 1
    return count
    
an=0
for q in range(0,5):
    for w in range(0,5):
        Y, X = delete(numbers[q][w])
        
        if updown(Y,X) == True:
            an += 1
            
        if leftright(Y,X) == True:
            an += 1
        if Y==X:
            an += cross()
        if Y + X == 4:
            an += cross2()
        if an>=3:
            print(q*5+(w+1))
            exit()