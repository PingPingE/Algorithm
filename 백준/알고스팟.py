'''
문제
알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다.
즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.

출력
첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.
'''
#126924kb	204ms
import sys,heapq
M,N= map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
INF = 987654321
dy,dx = [0,0,-1,1], [-1,1,0,0]

def dijkstra(r,c):
    costs = [[INF for _ in range(M)] for __ in range(N)]
    heap = []
    costs[r][c] = 0
    heapq.heappush(heap,[r,c, costs[r][c]])

    while heap:
        y,x,cost = heapq.heappop(heap)

        for d in range(4):
            ny,nx = y+dy[d], x+dx[d]
            if (0<=ny<N and 0<=nx<M) and costs[ny][nx] > cost+board[ny][nx]:
                costs[ny][nx] = cost+board[ny][nx]
                heapq.heappush(heap, [ny,nx, costs[ny][nx]])

    return costs[-1][-1]

print(dijkstra(0,0))

