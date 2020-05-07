def rotate(board):
    tmp = [[0]*len(board) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            tmp[j][len(board)-1-i] = board[i][j]
    return tmp

def solution(key, lock):
    m = len(key)
    n = len(lock)
    #zero = 0  # 0의 개수를 먼저 셈
    # for i in range(n):
    #     for j in range(n):
    #         if lock[i][j] == 0:
    #             zero += 1
    zero = len(list(filter(lambda x: x == 0, sum(lock, []))))
    for _ in range(4):
        #열쇠 시작점(i,j)
        for i in range(-m,21):
            for j in range(-m, 21):
                cnt = 0
                stat = True
                #시작점으로부터 열쇠 대입
                for y in range(m):
                    for x in range(m):
                        ny = i+y
                        nx = j+x
                        if ny<0 or nx<0 or ny>=n or nx>=n:#범위 체크
                            continue
                        if lock[ny][nx] == 0 and  key[y][x] == 1:
                            cnt += 1
                        elif lock[ny][nx]==1 and key[y][x] == 1:
                            stat = False
                            break
                    if stat is False:
                        break
                if cnt == zero and stat is True:
                    return True
        key = rotate(key)
    return False

    # board = [[-1]*60 for _ in range(60)]
    # for i in range(len(lock)):
    #     for j in range(len(lock)):
    #         if lock[i][j] == 0:
    #             zero += 1
    #         board[(len(board)//2)+i][(len(board)//2)+j] = lock[i][j]
    # que = deque()
    # for i in range(len(board)):
    #     for j in range(len(board)- len(key)):
    #         que.append((i,j))
    # while que:
    #     y,x = que.popleft()
    #     c = 0
    #     zC = zero
    #     while c<=4:
    #         c += 1
    #         stat = False
    #         for i in range(y,len(key)+y):
    #             if i >= len(board):
    #                 break
    #             for j in range(x, len(key)+x):
    #                 if j >= len(board) or board[i][j] == -1:
    #                     continue
    #                 if board[i][j] == 1 and key[i-y][j-x]  == 1:
    #                     stat = True
    #                     break
    #                 if board[i][j] == 0:
    #                     if key[i-y][j-x] == 1:
    #                         zC -= 1
    #                     else:
    #                         stat = True
    #                         break
    #             if stat is True:
    #                 break
    #         if stat is False and zC == 0 :
    #             return True
    #         key = rotate(key)
    # return False
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))