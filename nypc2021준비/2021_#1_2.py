'''
전략: 하나씩 보면서 만약 다음거가2이고 다다음번이 1 일 경우만 정답
가운데에 0,1 이 끼워져있으면 안됨

리스트안에 각각 방향마다 움직이는 방향을 넣어놓기

다음번 이랑 다다음번 변수 만들어서 넣기

만약 가능하면 true 로 바꾸기


조심: 초기화 제데로 하기

'''
#정답넣을 리스트 만들기
answer = []
for i in range(8):
    answer.append([0] * 8)
# 입력받기
#방향 받기
dir= [[1, 0], [0, 1], [1, 1], [-1, 1], [-1, 0], [0, -1], [-1, -1], [1, -1]]
board = []
for i in range(0,8):
    a = [*map(int, input().split(' '))]
    board.append(a)
# 하나씩 돌려보기
for i in range(0, 8):
    for j in range(0, 8):
        if board[i][j] != 0:
            continue
# 만약 0 이면....
        elif board[i][j] == 0:
            y, x = i, j
# flag만들기
            flag = False
# 방향마다 보기
            for q in range(8):
                y, x = i, j
                for _ in range(8):
# 다음 거랑 다다음거 초기화해놓기
                    y = y + dir[q][0]
                    x = x + dir[q][1]
                    ny = y + dir[q][0]
                    nx = x + dir[q][1]

                    if 0 <= y <=7 and  0 <= x <=7 and  0 <= nx <=7 and  0 <= ny <=7:
# 만약 2가 아니면 X
                        if board[y][x] != 2:
                            break
# 만약 2고 다음이 1이면 O
                        if board[y][x] == 2 and board[ny][nx] == 1:
                            flag = True
# flag가 true 면 되는거다
        if flag == True:
            answer[i][j] = 1
# 정답 프린트
for h in range(8):
    print(*answer[h]) 
