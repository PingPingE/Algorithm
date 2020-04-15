import sys
from copy import deepcopy
from itertools import product, combinations
def spread(w,cnt):
    global res
    #tmp = deepcopy(arr) -> 시간 진짜 오래 걸림
    tmp = [arr[l][:] for l in range(N)] #이렇게만 해줘도 300ms 절약
    d22= deepcopy(d2)
    #벽 표시
    for ww in range(3):
        tmp[w[ww][0]][w[ww][1]] = 1
    #확산
    while len(d22)>0:
        y,x = d22.pop()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M and tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                d22.add((ny,nx))
                cnt -= 1
    res = max(res, cnt)

dy = [-1,1,0,0]
dx = [0,0,-1,1]
N,M = map(int,input().split())
res = 0
arr = []
d2 = set()
wall = set()
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        #원래 벽 위치 저장
        if li[i] == 1:
            wall.add((_,i))
        #원래 바이러스 위치 저장
        if li[i] == 2:
            d2.add((_,i))
    arr.append(li)

comb = list(product([i for i in range(N)],[j for j in range(M)]))
ccomb = []
for y,x in comb:
    if (y, x) not in d2 and (y, x) not in wall:
        ccomb.append((y,x))
comb2 = list(combinations(ccomb, 3))#3개의 벽설치 후보위치 comb
for c in comb2:
    spread(c, N*M -(len(wall) + len(d2)+3))
print(res)


# dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
#
#
# def check(grp, res, s): #임시로 3개 벽 세운 보드, 빈칸 현 개수, 확산되기 전 2의 위치
#     global maximum
#     while len(s) != 0:
#         vr, vc = s.pop()
#         for t in range(4):
#             tr, tc = vr + dr[t], vc + dc[t]
#             if 0 <= tr < n and 0 <= tc < m:
#                 if grp[tr][tc] == 0:
#                     grp[tr][tc] = 2
#                     s.append((tr, tc))
#                     res -= 1
#     if res > maximum:
#         maximum = res
#
#
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# result = 0
# maximum = 0
# vir = []
# #벽 후보
# wall = []
# for r in range(n):
#     for c in range(m):
#         if board[r][c] == 0:
#             result += 1
#             wall.append((r, c))
#         elif board[r][c] == 2:
#             vir.append((r, c))
# for i in range(result-2):
#     for j in range(i + 1, result-1):
#         for k in range(j + 1, result):
#             temp = [board[l][:] for l in range(n)] #임시보드 초기화
#             for l in i, j, k: #벽 3개 세우기
#                 temp[wall[l][0]][wall[l][1]] = 1
#             check(temp, result - 3, vir[:])
# print(maximum)