#544ms
from copy import deepcopy
R,C,M = map(int, input().split())
shark = {}
board = [[0]*C for _ in range(R)]
c = 1
for _ in range(M):
    li = list(map(int, input().split()))
    board[li[0]-1][li[1]-1] = c
    shark[c] = li[2:]#위치빼고 속력, 방향, 크기만 저장
    c += 1

time = 0
res = 0
while time < C:
    tmp = [[0]*C for _ in range(R)]
    # 잡자
    for i in range(R):
        if board[i][time] > 0:
            res += shark[board[i][time]][-1]
            board[i][time] = 0
            break
    #상어이동
    #각 상어 이동 여부 체크
    done = set()
    for i in range(R):
        for j in range(C):
            if board[i][j] >0 and board[i][j] not in done:
                done.add(board[i][j])
                # 방향
                dir = shark[board[i][j]][1]
                # 속도
                speed = shark[board[i][j]][0]
                if dir == 1 : # 위
                    if speed <= i:
                        ny = i - speed
                        nx = j
                        if speed == i:
                            shark[board[i][j]][1] = 2
                    else:
                        t1 = speed - i
                        if (t1 // (R - 1)) % 2 == 0:
                            shark[board[i][j]][1] = 2
                            dir = 2
                        if dir == 1:
                            ny = R - 1 - (t1 % (R - 1))
                        else:
                            ny = t1 % (R - 1)
                        nx = j

                elif dir == 2:  # 아래
                    if speed <= (R - 1 - i):
                        ny = i + speed
                        nx = j
                        if speed == (R-1-i):
                            shark[board[i][j]][1] = 1
                    else:
                        t1 = speed - (R - 1 - i)
                        if (t1 // (R - 1)) % 2 == 0:
                            shark[board[i][j]][1] = 1
                            dir = 1
                        if dir == 1:
                            ny = R - 1 - (t1 % (R - 1))
                        else:
                            ny = t1 % (R - 1)
                        nx = j

                elif dir == 3:  # 오른쪽
                    if C - 1 - j >= speed:
                        ny = i
                        nx = j + speed
                        if speed == C-1-j:
                            shark[board[i][j]][1] = 4
                    else:
                        # 끝으로
                        t1 = speed - (C - 1 - j)
                        # 방향 바꾸기
                        if (t1 // (C - 1)) % 2 == 0:
                            shark[board[i][j]][1] = 4
                            dir = 4
                        if dir == 3:
                            nx = t1 % (C - 1)
                        else:
                            nx = C - 1 - (t1 % (C - 1))
                        ny = i

                else: #왼쪽
                    if speed <= j:
                        ny = i
                        nx = j - speed
                        if speed == j:
                            shark[board[i][j]][1] = 3
                    else:
                        # 원점으로
                        t1 = speed - j
                        if (t1 // (C - 1)) % 2 == 0:
                            shark[board[i][j]][1] = 3
                            dir = 3
                        if dir == 3:
                            nx = t1 % (C - 1)
                        else:
                            nx = C - 1 - (t1 % (C - 1))
                        ny = i
                if tmp[ny][nx] > 0:
                    if shark[tmp[ny][nx]][-1] < shark[board[i][j]][-1]:
                        tmp[ny][nx] = board[i][j]
                else:
                    tmp[ny][nx] = board[i][j]
    board ,tmp = tmp, board
    time += 1
print(res)

#360ms
# def move_shark(r, c, s, d, z):
#     if new_a[r][c]:
#         if new_a[r][c][-1] > z:
#             return
#     new_a[r][c] = [s, d, z]
#
#
# def catch():
#     global ans
#     caught = False
#     temp_sharks = []
#     for r in range(R):
#         for c in range(C):
#             if c == king_position and not caught and a[r][c]:
#                 caught = True
#                 ans += a[r][c][-1]
#                 a[r][c] = 0
#                 continue
#             if a[r][c]:
#                 s, d, z = a[r][c]
#                 nr = r + s * dr[d]
#                 nc = c + s * dc[d]
#                 if nr < 0:
#                     nr = -nr
#                     d = 1
#                 if nr > R - 1:
#                     q = nr // (R-1)
#                     b = nr % (R-1)
#                     if q % 2 == 0:
#                         nr = b
#                     else:
#                         nr = R - 1 - b
#                         d = 0
#                 if nc < 0:
#                     nc = -nc
#                     d = 2
#                 if nc > C-1:
#                     q = nc // (C-1)
#                     b = nc % (C-1)
#
#                     if q % 2 == 0:
#                         nc = b
#                     else:
#                         nc = C-1 - b
#                         d = 3
#                 a[r][c] = 0
#
#                 move_shark(nr, nc, s, d, z)
#
#
# R, C, M = map(int, input().split())
# # 주의1: 좌표가 1부터 시작함.
#
# a = [[0] * (C) for _ in range(R)]
# new_a = [[0] * (C) for _ in range(R)]
# dr = [-1, 1, 0, 0]
# dc = [0, 0, 1, -1]
# for _ in range(M):
#     r, c, s, d, z = map(int, input().split())
#     a[r-1][c-1] = [s, d-1, z]
#
# king_position = 0
# k = C
# ans = 0
# while k:
#     k -= 1
#     catch()
#     a, new_a = new_a, a
#     king_position += 1
#
# print(ans)

