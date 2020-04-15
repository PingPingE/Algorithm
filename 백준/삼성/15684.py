def check():
    global res, N, H, board
    for start in range(N):
        current  = start
        for j in range(H):
            if current <0 or current>=N:
                break
            if board[j][current] >0:
                current += 1
            elif current-1 >=0 and board[j][current-1] >0:
                current -= 1
        if start != current:
            return False
    return True
def sol(y,x,n):
    global res, board, N, H
    if res >= 0 and res<=n:
        return
    if check() is True:
        res = n
    if n >= 3:
        return
    for i in range(y,H):
        for j in range(x,N-1):
            if board[i][j] >0:
                continue
            if j+1 <N and board[i][j+1] >0:
                continue
            if j-1>=0 and board[i][j-1] >0:
                continue
            board[i][j] = 1
            sol(i,j,n+1)
            board[i][j] = 0
        x = 0

N,M,H = map(int,input().split())
res = -1
board = [[0]*N for _ in range(H)]
for _ in range(M):
    a,b = map(int, input().split())
    board[a-1][b-1]=1
sol(0,0,0)
print(res)