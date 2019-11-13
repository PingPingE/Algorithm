from collections import deque
def solution(m, n, board):
    answer = 0
    global done
    # 왼 아래 대각선(왼쪽 밑)
    dy = [0, 1, 1]
    dx = [1, 0, 1]
    arr = []
    for b in board:
        arr.append(list(b))
    que = deque()

    for i in range(m - 1):
        for j in range(n - 1):
            # y,x
            que.append([i, j])
    # 한번 돌 때 없어질 블럭(길이 0이면 break)
    done = set()
    while que:
        y, x = que.popleft()
        if arr[y][x] == 0:
            continue
        Tdone = set()
        prev = arr[y][x]
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= m or nx >= n:
                break
            if prev == arr[ny][nx]:
                Tdone.add((ny, nx))
            else:
                break
        # 4개 블럭 완성?
        if len(Tdone) == 3:
            Tdone.add((y, x))
            done |= Tdone

        if len(que) == 0:
            if len(done) == 0:
                return answer
            else:
                answer += len(done)
                # 판 갱신(done에 있는거 지워주고 위에꺼 끌어내림)
                for y, x in done:
                    arr[y][x] = 0
                # 밑에서부터
                for y in range(m - 1, -1, -1):
                    for x in range(n):
                        # 0이면 위에 0아닌거랑 바꾸기
                        if arr[y][x] == 0:
                            for i in range(y - 1, -1, -1):
                                if arr[i][x] != 0:
                                    arr[y][x], arr[i][x] = arr[i][x], arr[y][x]
                                    break

                for i in range(m - 1):
                    for j in range(n - 1):
                        # y,x
                        if arr[i][j] == 0:
                            continue
                        que.append([i, j])
                done = set()

    return answer
#print(solution(4,5,['CCBDE', 'AAADE', 'AAABF', 'CCBBF']))
print(solution(6,6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))