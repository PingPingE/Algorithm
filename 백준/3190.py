from collections import deque
def Move():
    global board,current
    if current[-1] == 'R':
        r,c = 0,1
    elif current[-1] == 'L':
        r,c = 0,-1
    elif current[-1] == 'U':
        r,c = -1,0
    else:#D
        r,c = 1,0
    nr = current[0]+r
    nc = current[1]+c
    #범위 이탈(벽) or 자기 벽과 부딪힘
    if nr<0 or nc<0 or nc>=N or nr>=N or board[nr][nc] == 1:
        return False
    #사과가 없으면
    if board[nr][nc] != -1:
        rr,cc = tail.popleft()
        board[rr][cc] = 0

    # 머리 이동
    board[nr][nc] = 1
    tail.append([nr, nc])
    current[0] = nr
    current[1] = nc
    return True

N = int(input())
K = int(input())
board= [[0]*N for _ in range(N)]
board[0][0] = 1#뱀몸은 1로 표시
for _ in range(K):
    r,c = map(int, input().split())
    board[r-1][c-1] = -1
L = int(input())
#뱀이 회전할 시간과 D or L
move = {}
for _ in range(L):
    l = list(input().split())
    x = int(l[0])
    C = l[1]
    move[x] = C
#머리위치와 방향
current = [0,0,'R']
tail = deque()
tail.append([0,0])
L = {'R':'U', 'L':'D', 'U':'L','D':'R'}
D = {'R':'D', 'L':'U','U':'R', 'D':'L'}
time = 0
while True:
    #뱀 이동
    if time in move:
        if move[time] == 'L':
            current[-1] = L[current[-1]]
        else:
            current[-1] = D[current[-1]]

    res = Move()
    time += 1
    if res is False:
        break

print(time)