#===메모리 초과
import sys, heapq
sys.setrecursionlimit(10**8)
dy,dx=[0,0,-1],[-1,1,0]
N,M=map(int, input().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
costs=[[0]*M for _ in range(N)]
done =[[0]*M for _ in range(N)]

def check(y,x):
    return 0<=y<N and 0<=x<M

def sol(cost,y,x):
    if (y,x) == (N-1,M-1):
        return cost+board[y][x]

    if not check(y,x) or done[y][x]:
        return -1000

    done[y][x]=1
    costs[y][x]=max(sol(cost+board[y][x],y,x+1),
                    sol(cost+board[y][x],y,x-1),
                    sol(cost+board[y][x],y+1,x))
    done[y][x]=0

    return costs[y][x]

print(sol(0,0,0))