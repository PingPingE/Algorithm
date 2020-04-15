from collections import deque
from copy import deepcopy
from copy import copy
#시작위치, 가야할 방향, 임시 보드
def cal(y,x,dir,tmp):
    global N,M
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    tcnt = 0
    for i in dir:
        ny = y
        nx = x
        while True:
            ny += dy[i]
            nx += dx[i]
            if ny<0 or nx<0 or ny>=N or nx>=M or tmp[ny][nx] ==6:
                break
            if tmp[ny][nx] != 0:
                continue
            tmp[ny][nx] = -1
            tcnt += 1
    return [tcnt, tmp]

N, M = map(int, input().split())
que =deque()
cctv = set()
office = []
total = 0
#0: 빈칸, 6: 벽(통과X),1~5: CCTV종류)
for _ in range(N):
    li = list(map(int, input().split()))
    for l in range(len(li)):
        if li[l] == 6:
            continue
        total += 1
        if 1<=li[l]<=5:
            cctv.add((_,l))

    office.append(li)
#사각지대 개수
res = -1

que.append([copy(cctv), 0, [office[t][:] for t in range(len(office))]])

while que:
    ctv, cnt, tmp = que.popleft()
    if len(ctv) == 0:
        if res == -1 or res > total-cnt:
            res = total-cnt
        continue
    y,x = ctv.pop()
    #cctv자리도 세어줌
    cnt += 1
    cnum = tmp[y][x]
    ttmp = [tmp[t][:] for t in range(len(tmp))]
    if cnum == 1:
        ttmp[y][x] = -1
        for i in range(4):
            tres = cal(y,x,[i], [ttmp[t][:] for t in range(len(ttmp))])
            que.append([copy(ctv), cnt+tres[0],tres[1]])
    elif cnum == 2:
        ttmp[y][x] = -1
        for i in [(0,1),(2,3)]:
            tres = cal(y,x, i, [ttmp[t][:] for t in range(len(ttmp))])
            que.append([copy(ctv), cnt + tres[0], tres[1]])
    elif cnum == 3:
        ttmp[y][x] = -1
        for i in [(0,2),(0,3),(1,2),(1,3)]:
            tres = cal(y,x, i, [ttmp[t][:] for t in range(len(ttmp))])
            que.append([copy(ctv), cnt + tres[0], tres[1]])
    elif cnum == 4:
        ttmp[y][x] = -1
        for i in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]:
            tres = cal(y, x, i, [ttmp[t][:] for t in range(len(ttmp))])
            que.append([copy(ctv), cnt + tres[0], tres[1]])
    else:
        ttmp[y][x] = -1
        tres = cal(y, x, (0,1,2,3),[ttmp[t][:] for t in range(len(ttmp))])
        que.append([copy(ctv), cnt + tres[0], tres[1]])

print(res)


#개빠름
# def dfs(pos):
#     global N, M, res, map, dx, dy, seeDelta, cameraCount, camera, seeXY
#     if pos == cameraCount :
#         if len(seeXY) > res :
#             res = len(seeXY)
#         return
#     y,x,d = camera[pos]
#     for go in seeDelta[d] :
#         cnt = 0
#         for w in go :
#             ty = y + dy[w]
#             tx = x + dx[w]
#             for i in range(30) :
#                 if 0 > tx or tx >= M or 0 > ty or ty >= N or map[ty][tx] == 6 :
#                     break
#                 if not (tx,ty) in seeXY and map[ty][tx] == 0:
#                     cnt += 1
#                     seeXY.append((tx,ty))
#                 tx += dx[w]
#                 ty += dy[w]
#         dfs(pos+1)
#         for i in range(cnt) :
#             seeXY.pop(len(seeXY)-1)
# N, M = list(map(int,input().split()))
# map = [list(map(int,input().split())) for i in range(N)]
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]
# seeDelta = [
#     [],
#     [[0],[1],[2],[3]],
#     [(0,2),(1,3)],
#     [(0,1),(1,2),(2,3),(3,0)],
#     [(0,1,3),(0,1,2),(1,2,3),(0,2,3)],
#     [(0,1,2,3)]
# ]
# camera = []
# wallCount = 0
# for i in range(N) :
#     for j in range(M) :
#         if 0 < map[i][j] < 6 :
#             camera.append([i,j,map[i][j]])
#         elif map[i][j] == 6 :
#             wallCount += 1
# cameraCount = len(camera)
# seeXY = []
# res =  -1
# dfs(0)
# print(N*M - res - cameraCount - wallCount)
