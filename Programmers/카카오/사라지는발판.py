import sys

def solution(board, aloc, bloc):
    INF = sys.maxsize
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    answer = INF
    N_y, N_x = len(board), len(board[0])

    def dfs(cur_yx, cnt, turn):
        nonlocal answer
        if cnt >= answer: return
        y, x = cur_yx[turn]
        if board[y][x]:
            flag=False
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < N_y and 0 <= nx < N_x and board[ny][nx]:
                    cur_yx[turn] = [ny, nx]
                    board[y][x] = 0
                    print("Turn:", turn, "move from :", (y, x), " to: ", (ny, nx))
                    dfs(list(cur_yx[i][:] for i in range(2)), cnt + 1, not turn)
                    board[y][x] = 1
                    cur_yx[turn] = [y, x]
                    flag = True
            print("======"*10, cnt, "answer: ", answer)
            if not flag:
                answer = min(answer, cnt)

        else:
            answer = min(answer, cnt)

    dfs([aloc, bloc], 0, 0)
    return answer