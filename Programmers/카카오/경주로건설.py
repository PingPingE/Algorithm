#마지막 TC에서 걸림
import heapq
def solution(board):
    N = len(board)
    INF = 600*N*N

    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

    # cost, prev, cur
    que = [[0, (0, 0), (0, 0)]]
    heapq.heapify(que)
    costs = [[INF] * N for _ in range(N)]
    costs[0][0] = 0

    while que:
        cost, prev, cur = heapq.heappop(que)
        if costs[cur[0]][cur[1]] < cost: continue

        for d in range(4):
            ny, nx = cur[0] + dy[d], cur[1] + dx[d]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                if ny == prev[0] or nx == prev[1]:
                    ncost = cost + 100
                else:
                    ncost = cost + 600

                if ncost <= costs[ny][nx]:
                    que.append([ncost, cur, (ny, nx)])
                    costs[ny][nx] = ncost

    return costs[-1][-1]
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.35ms, 10.3MB)
테스트 7 〉	통과 (0.20ms, 10.3MB)
테스트 8 〉	통과 (0.20ms, 10.3MB)
테스트 9 〉	통과 (0.19ms, 10.3MB)
테스트 10 〉	통과 (0.38ms, 10.3MB)
테스트 11 〉	통과 (0.90ms, 10.3MB)
테스트 12 〉	통과 (2.72ms, 10.3MB)
테스트 13 〉	통과 (0.11ms, 10.3MB)
테스트 14 〉	통과 (0.14ms, 10.3MB)
테스트 15 〉	통과 (0.37ms, 10.3MB)
테스트 16 〉	통과 (0.66ms, 10.3MB)
테스트 17 〉	통과 (0.86ms, 10.3MB)
테스트 18 〉	통과 (1.06ms, 10.3MB)
테스트 19 〉	통과 (0.93ms, 10.3MB)
테스트 20 〉	통과 (0.65ms, 10.3MB)
테스트 21 〉	통과 (0.69ms, 10.3MB)
테스트 22 〉	통과 (0.06ms, 10.3MB)
테스트 23 〉	통과 (0.08ms, 10.3MB)
테스트 24 〉	통과 (0.06ms, 10.4MB)
테스트 25 〉	실패 (0.04ms, 10.4MB)
'''

'''
from collections import deque
def solution(board):
    N = len(board)
    answer = 600 * N * N
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]

    def bfs(start):
        nonlocal answer
        que = deque([[(0, 0), start, 100]])
        done = set()
        done.update([(0,0),start])

        while que:
            prev, cur, cost = que.popleft()
            print(prev, cur, cost)
            if cost >= answer:
                continue

            if cur == (N - 1, N - 1):
                answer = min(answer, cost)
                continue

            for d in range(4):
                ny, nx = cur[0] + dy[d], cur[1] + dx[d]
                if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in done and board[ny][nx] == 0:
                    if ny == prev[0] or nx == prev[1]:
                        que.append([cur, (ny, nx), cost + 100])
                    else:
                        que.append([cur, (ny, nx), cost + 600])
                    done.add((ny, nx))

    # prev, cur, cur_cost
    bfs((0,1))
    bfs((1,0))

    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
'''
