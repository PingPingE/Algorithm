#=======메모리 초과!!!!!!
import sys
sys.setrecursionlimit(10**8)
INF=-987654321
dy,dx=[0,0,1],[-1,1,0]
N,M=map(int, input().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
costs=[[[INF]*3 for _ in range(M)] for _ in range(N)]
done =[[0]*M for _ in range(N)]


def check(y,x):
    return 0<=y<N and 0<=x<M

def sol(y,x,d):
    if (y,x) == (N-1,M-1):
        return board[y][x]

    if costs[y][x][d] == INF:
        done[y][x] = 1
        for nd in range(3):
            ny, nx = y + dy[nd], x + dx[nd]
            if not check(ny, nx) or done[ny][nx]: continue
            costs[y][x][d] = max(costs[y][x][d], sol(ny,nx,nd) + board[y][x])
        done[y][x]=0

    return costs[y][x][d]

print(sol(0,0,0))