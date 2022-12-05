'''
중요! 
6개 이상은 이긴걸로 표시되지않는다

검은색이 이겼을 경우에는 1을, 
흰색이 이겼을 경우에는 0를, 
아직 승부가 결정되지 않았을 경우에는 0을 출력한다. 

그 중 가장 위에 있는 것)의 가로줄 번호와, 세로줄 번호를 순서대로 출력한다.


'''
# 입력받기
board=[]
for w in range(19):
    a= [*map(int, input().split(' '))]
    board.append(a)
Answer=[]
dir = [[1, 0], [0, 1], [1, -1], [1, 1]]
#     [1, 0], [0, 1],] [1, 1], [-1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1]
# 하나씩 돌려보면서 1인지 2인지 변수안에 넣기
for i in range(19):
    for j in range(19):
        number=0
        if board[i][j]!=0:
            if board[i][j]==1:
                number=1
            elif board[i][j]==2:
                number=2
            y,x=i,j
            for q in range(0,4):
                flag= False
                an=1
                y,x= i,j
                opy, opx= i,j
                #print(i,j, dir[q])
                for _ in range(19):
                    y= y + dir[q][0]# 안바뀐다
                    x= x + dir[q][1]
                    if 0<=y<=18 and 0<=x<= 18:
                        if board[y][x]==number:
                            an+=1
                            #print(y+1,x+1, an, i+1, j+1, dir[q])
                        else:
                            break
                    
                for u in range(19):
                    opy= opy-(dir[q][0])
                    opx= opx-(dir[q][1])
                    if 0<=opx<=18 and 0<=opy<=18:
                        if board[opy][opx]==number:
                            #print('.')
                            an+=1
                            #print(opy+1,opx+1, an, i+1, j+1, -dir[q][0], -dir[q][1])
                        else:
                            break
                if an==5:
                    flag=True
                    #print(i+1, j+1)
                    Answer.append([number, j+1, i+1])
                elif an>5:
                    continue
                    #print() 
if len(Answer)==0:           
    print(0)
else:
    #print(Answer)
    print(min(Answer)[0])
    print(min(Answer)[2], min(Answer)[1])



                    
                        

#만약 1이고 다음번이 1일경우에 된다고 친다.
# 만약 2 이괴 다음번이 2일경우에는 가능하다고 친다
# 변수 안에 하나씩 더해가면서 
# 가능한 숫자 묶음(?) 을 다 돈후에 5 일경우에는 1 인지 2인지 프린트하고 처음 좌표 찍기.
# 만약 이긴사람이 없다면 0을 출력. 
'''
0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
'''