#===Bottom-up
#참고: https://huiung.tistory.com/166 , https://blog.encrypted.gg/115
#232484kb	736ms
import sys
INF=-987654321
N,M=map(int, input().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
costs=[[[INF]*3 for _ in range(M)] for _ in range(N)]

for i in range(3):
    costs[0][0][i]=0

for y in range(N):
    for x in range(M):#===== 왼 -> 오 방향으로 보기

        if x+1<M:#==오른쪽으로 -> 오른쪽에서 온거는 X
            costs[y][x+1][0]=max(costs[y][x+1][0], costs[y][x][0]+board[y][x])#==왼쪽에서 온거
            costs[y][x+1][0]=max(costs[y][x+1][0], costs[y][x][2]+board[y][x])#==위에서 온거

        if y+1<N:#==아래로
            costs[y+1][x][2] = max(costs[y+1][x][2], costs[y][x][0] + board[y][x])  #==왼쪽에서 온거
            costs[y+1][x][2] = max(costs[y+1][x][2], costs[y][x][1] + board[y][x])  #==오른쪽에서 온거
            costs[y+1][x][2] = max(costs[y+1][x][2], costs[y][x][2] + board[y][x])  #==위에서 온거

        if x-1>=0:#==왼쪽으로 -> 왼쪽에서 온거는 X
            costs[y][x-1][1] = max(costs[y][x-1][1], costs[y][x][1] + board[y][x])  #==오른쪽에서 온거
            costs[y][x-1][1] = max(costs[y][x-1][1], costs[y][x][2] + board[y][x])  #==위에서 온거


    for x in range(M-1,-1,-1):#===== 오 -> 왼 방향으로 보기

        if x+1 < M:  # ==오른쪽으로 -> 오른쪽에서 온거는 X
            costs[y][x + 1][0] = max(costs[y][x + 1][0], costs[y][x][0] + board[y][x])  # ==왼쪽에서 온거
            costs[y][x + 1][0] = max(costs[y][x + 1][0], costs[y][x][2] + board[y][x])  # ==위에서 온거

        if y+1 < N:  #==아래로
            costs[y + 1][x][2] = max(costs[y + 1][x][2], costs[y][x][0] + board[y][x])  # ==왼쪽에서 온거
            costs[y + 1][x][2] = max(costs[y + 1][x][2], costs[y][x][1] + board[y][x])  # ==오른쪽에서 온거
            costs[y + 1][x][2] = max(costs[y + 1][x][2], costs[y][x][2] + board[y][x])  # ==위에서 온거

        if x-1 >= 0:  #==왼쪽으로 -> 왼쪽에서 온거는 X
            costs[y][x - 1][1] = max(costs[y][x - 1][1], costs[y][x][1] + board[y][x])  # ==오른쪽에서 온거
            costs[y][x - 1][1] = max(costs[y][x - 1][1], costs[y][x][2] + board[y][x])  # ==위에서 온거

print(max(costs[-1][-1])+board[-1][-1])



#===굉장히 빠르고 메모리도 절약한 코드(gbba1029님)
#140852kb	288ms

import sys
n, m = map(int, input().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

#==모든 행에 대해서 만들지 않고 딱 한 행에서 볼 것만 담을 예정인 듯
right = [0]*m
left = [0]*m


dp[0][0] = data[0][0]
for j in range(1, m): #===첫 행은 미리 채우고(왼 -> 오)
    dp[0][j] = dp[0][j-1] + data[0][j]


for i in range(1, n): #===이제 각 행을 보면서
    #=== 왼-> 오 방향으로
    right[0] = dp[i-1][0] + data[i][0] #==젤 왼쪽에 있는건 왼쪽에서 오는 걸 받지 못하니까 이렇게 예외 처리한 듯
    for j in range(1, m):
        right[j] = max(right[j-1] + data[i][j], dp[i-1][j] + data[i][j]) #==왼쪽이나 위에서 온 것 중 큰 것

    #=== 오 -> 왼 방향으로
    left[m-1] = dp[i-1][m-1] + data[i][m-1] #==젤 오른쪽에 있는건 오른쪽에서 오는 걸 받지 못하니까 이렇게 예외 처리한 듯
    for j in range(m-2, -1, -1):
        left[j] = max(left[j+1] + data[i][j], dp[i-1][j] + data[i][j]) #==오른쪽이나 위에서 온 것 중 큰 것

    for k in range(m):
        dp[i][k] = max(right[k], left[k]) #==두 방향 중 큰 것

print(dp[n-1][m-1])


#=======Top-down: 메모리 초과!!!!
'''
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
'''
