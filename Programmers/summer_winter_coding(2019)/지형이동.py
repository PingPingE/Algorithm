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


from collections import defaultdict
import heapq
def solution2(land, height):
    answer = 0
    N = len(land)
    links = defaultdict(lambda: defaultdict())
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(N):
        for j in range(N):
            n = land[i][j]
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < N and abs(land[ny][nx] - n) > height:
                    cost = abs(land[ny][nx] - n)
                    links[(i, j)][(ny, nx)] = cost
                    links[(ny, nx)][(i, j)] = cost

    #다익스트라로 풀어보기
    costs = [[10001] * N for _ in range(N)]
    costs[0][0] = 0
    que = [[costs[0][0], 0, 0]]
    heapq.heapify(que)
    while que:
        cost, y, x = heapq.heappop(que)
        if cost > costs[y][x]: continue

        for k, v in links[(y, x)].items():
            if v <= height:
                ncost = cost
            else:
                ncost = cost + v
            # print(f"from ({y},{x}) to {k}, ncost: {ncost}, cur_costs: {costs[]}")
            if ncost <= costs[k[0]][k[1]]:
                costs[k[0]][k[1]] = ncost
                heapq.heappush(que, [ncost, k[0], k[1]])
    print(costs)
    return answer

print(solution2([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)) #기댓값: 15
