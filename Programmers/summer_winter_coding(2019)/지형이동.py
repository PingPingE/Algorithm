#https://yeeybook.tistory.com/18
#시도중
import sys
sys.setrecursionlimit(10 ** 8)

def solution(land, height):
    N = len(land)
    answer = 10001 * N * N
    dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]

    def dfs(y, x, cost, cnt):
        nonlocal answer, done
        if cost >= answer:
            return
        if cnt == N * N:
            answer = min(cost, answer)
            return

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not done[ny][nx]:
                diff = abs(land[y][x] - land[ny][nx])
                done[ny][nx] = 1
                dfs(ny, nx, cost + (diff if diff > height else 0), cnt + 1)
                done[ny][nx] = 0

    for i in range(N):
        for j in range(N):
            done = [[0] * N for _ in range(N)]
            done[i][j] = 1
            dfs(i, j, 0, 1)
    return answer


import heapq
def solution2(land, height):
    answer = 0
    N = len(land)
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    costs = [[10001] * N for _ in range(N)]
    costs[0][0] = 0
    que = [[costs[0][0], 0, 0]]
    heapq.heapify(que)
    while que:
        cost, y, x = heapq.heappop(que)
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            add = 0
            if 0 <= ny < N and 0 <= nx < N:
                if abs(land[ny][nx] - land[y][x]) > height:
                    add = abs(land[ny][nx] - land[y][x])
                ncost = cost + add
                if ncost < costs[ny][nx]:
                    costs[ny][nx] = ncost
                    heapq.heappush(que, [ncost, ny, nx])
    print(costs)
    return costs[-1][-1]

print(solution2([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)) #기댓값: 15
