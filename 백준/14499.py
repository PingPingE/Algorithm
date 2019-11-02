from collections import deque
N,M,y,x,K = map(int,input().split())
#지도
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
#명령
d = deque()
d.extend(list(map(int, input().split())))
#주사위
dice = deque()
dice.extend([[-1]*3 for _ in range(4)])
for i in range(len(dice)):
    if i == 1:
        for j in range(3):
            dice[i][j] = 0
    else:
        dice[i][1] = 0
m = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
while d:
    dd = d.popleft()
    ny = y+m[dd][0]
    nx = x+m[dd][1]
    if ny<0 or nx<0 or ny>=N or nx>=M:
        continue
    y = ny
    x = nx
    #움직여서 현재 밑면 정보 갱신
    if dd == 1: #동
        tmp = dice[3][1]
        dice[3][1] = dice[1][2]
        for i in range(2,0,-1):
            dice[1][i] = dice[1][i-1]
        dice[1][0] = tmp

    elif dd==2: #서
        tmp = dice[3][1]
        dice[3][1] = dice[1][0]
        for i in range(2):
            dice[1][i] = dice[1][i+1]
        dice[1][2] = tmp

    elif dd==3: #북
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i+1][1]
        dice[3][1] = tmp

    else:#남
        tmp = dice[3][1]
        for i in range(3,0,-1):
            dice[i][1] = dice[i-1][1]
        dice[0][1] = tmp

    #새로 도착한 칸이 0인지 아닌지
    if board[y][x] == 0:
        board[y][x] = dice[3][1]
    else:
        dice[3][1] = board[y][x]
        board[y][x] = 0

    #출력
    print(dice[1][1])
