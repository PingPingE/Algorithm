import sys
sys.setrecursionlimit(10**8)
N,M = map(int, input().split())
board = []
#-1로 초기화해야함 (0으로 하면 무한루프)
res = [[-1]*M for _ in range(N)]
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))
res[0][0] = board[0][0]
def sol(y,x):
    if y<0 or x<0 or x>=M or y>=N:
        return 0
    if res[y][x] == -1:
        res[y][x]  = board[y][x]+max(sol(y-1, x-1), sol(y-1,x), sol(y,x-1))
    return res[y][x]
print(sol(N-1,M-1))

#숏코딩
#젤 위에 0으로 채워진 행과 젤 왼쪽에 0으로 채워진 열을 만들어서 왼쪽, 위 검사
# m,n=map(int,input().split())
# l=[[0]*(n+1)]+[[0]+list(map(int,input().split())) for i in range(m)]
# for j in range(1,m+1):
#     for k in range(1,n+1):
#         l[j][k]+=max(l[j-1][k],l[j][k-1])
# print(max(l[-1]))