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