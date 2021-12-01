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