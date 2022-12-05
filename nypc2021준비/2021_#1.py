'''
A에다가 받고
An은 0으로 체워진 똑같은 크기의 리스트
만약 0이면 에서 걸리게 하고

위- x,y+1
아래 - x, y-1
오른쪽 - x+1, y
왼쪽- x, y+1

A=[]
An=[]
for i in range(0,8):
    a=[*map(int, input().split(' '))]
    A.append(a) 
for i in range(0,8):
    An.append([0]*8)
for i in range(0,8):
    for k in range(0,8):
        if A[i][k]== 0:
            an=0
            for g in range(1,8):#0이 가운데에 있으면 바로 나가기
                if 0<=i-g-1 <=7:

                    if A[i-g][k]!=2:
                        break
                    if A[i-g][k]==2 and A[i-g-1][k]==1:
                        an+=1 
                        print(an,1)
                        break
                else:
                    break
            for p in range(1,8):
                if 0<=i+p+1 <=7:
                        
                    if A[i+p][k]!=2:#가운데에 1이나 0이있을때 
                        break
                    if A[i+p][k]==2 and A[i+p+1][k]==1:
                        an+=1
                        print(an,2)
                        break
                else:
                    break
            for j in range(1,8):
                if 0<=k+j+1<=7:

                    if A[i][k+j]!=2:
                        break

                    if A[i][k+j]==2 and A[i][k+j+1]==1:
                        an+=1
                        print(an,3)
                        break
                else:
                    break
            for n in range(1,8):
                if 0<=k-n-1<=7:

                    if A[i][k-n]!=2:
                        break
                    if  A[i][k-n]==2 and A[i][k-n-1]==1:
                        an+=1
                        print(an,4)
                        break
                else:
                    break
            for h in range(1,8):
                if 0<= k+h+1 <=7 and  0<=i+h+1 <=7:
                    if A[i+h][k+h]!=2:
                        break
                    if A[i+h][k+h]==2 and A[i+h+1][k+h+1]==1:
                        an+=1
                        print(a,5)
                        break
            for q in range(1,8):
                if 0<= k-q-1 <=7 and 0<=i-q-1<=7:
                    if A[k-q][i-q]!=2:
                        break
                    if A[k-q][i-q]==2 and A[k-q-1][i-q-1]==1:
                        an+=1
                        print(an,6)
                        break
            for f in range(1,8):
                if 0<= k-f-1 <=7 and 0<=i+f+1<=7:
                    if A[k-f][i+f]!=2:
                        break
                    if A[k-f][i+f]==2 and A[k-f-1][i+f-1]==1:
                        an+=1
                        print(an,7)
                        break
            for w in range(1,8):
                if 0<= k+w+1 <=7 and 0<=i-w-1<=7:
                    if A[k+w][i-w]!=2:
                        break
                    if A[k+w][i-w]==2 and A[k+w+1][i-w-1]==1:
                        an+=1
                        print(an,8)
                        break
            if an!=0:
                An[i][k]=1
for k in range(0,8):
    print(*An[k])
            

'''




answer=[]
for  i in range(8):
    answer.append( [0] *8)#정답을 넣을 리스트 만들기
dir= [[-1,-1], [-1,0], [-1,1], [0,1], [0,-1], [1,1], [1,0], [1,-1]]# 갈수 있는 방향 적어놓기

board = []
for k in range(0,8):
    a= [*map(int, input().split(' '))]#입력 받기
    board.append(a)#b에 input

for  i in range(8):
    for k in range(8):
        if board[i][k] !=0:#board를 보면서 2,1 일경우 패스 
            continue
        y,x = i,k
        flag = False#만약 된다면 flag를 true로 바꿀것이다

        for d in range(8):
            y, x = i, k#초기화 제데로 하기
            for _ in range(1,8):
                y= y + dir[d][0]#y안에 그 자리의 y좌표를 넣는다 
                x= x + dir[d][1]#x안에 그 자리의 x좌표를 넣는다 
                ny = y + dir[d][0]# nx 안에 그 자리의 x좌표에 다음 값를 넣는다
                nx = x + dir[d][1]# ny 안에 그 자리의 y좌표에 다음 값를 넣는다

                if 0 <= y <= 7 and 0<= x <= 7 and  0 <= nx <= 7 and  0 <= ny <= 7:#만약 판 안에 있다면...
                    if board[y][x] != 2:#만약 0,1 이 중간에 있으면 그만하기
                        break
                    if board[y][x] == 2 and board[ny][nx] == 1:#만약 다음거가 2 이고 다다음거가 1일경우...
                        flag = True #flag를 true로 바꾸어 가능하다는걸 표시
                else:#만약 판 안에 없다면...
                    break#그만하기
        if flag == True:# 다 돈 이후 flag가 true일경우..
            answer[i][k] = 1# 정답에 가능하다고 표시한다

for k in range(0,8):# 모든 자리를 본 이후 정답 프린트!
    print(*answer[k])
