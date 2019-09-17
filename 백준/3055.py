#빈 곳 .  물이 찬 곳 *  돌 X   비버 굴 D  고슴도치 위치 S
#매분마다 고슴도치 이동 : 인접한 빈칸(.), 비버 굴(D)
#매분마다 물 확장: 인접한 빈칸(.), 물이 찬곳(*)
#물과 고슴토치는 돌을 통과못함
#고슴도치가 안전하게 비버 굴로 이동하기 위한 최소 시간은?
#고슴도치는 물이 찰 예정인 칸 즉, 물과 한변이라도 공유하는 빈칸에는 이동할 수 없다.

#----------중복방문 찾고 고치기---------------
from collections import deque
import sys
R,C = map(int, input().split())
arr = []
inW = deque()
i = 0
while len(arr)<R:
    li = list(sys.stdin.readline().strip())
    if len(li) >0:
        if 'S' in li:
            inS = (i, li.index('S'))
        if '*' in li:
            inW.append((i,li.index('*')))
        arr.append(li)
        i += 1

def bfs():
    global arr, inW, inS, R,C
    que = deque()
    que.append([inS,0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    #물확산 타이밍 맞추기
    time = -1
    while que:
        q = que.popleft()
        y,x = q[0]
        cnt = q[1]
        n = len(inW)
        if arr[y][x] == '*': continue
        # 고슴도치 move
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= R or nx < 0 or nx >= C: continue
            if arr[ny][nx] != 'X' and arr[ny][nx] != '*' and arr[ny][nx] != 'S':
                if arr[ny][nx] == 'D':
                    print(cnt + 1)
                    return
                else:
                    arr[ny][nx] = 'S'
                    que.append([(ny, nx), cnt + 1])
        #cnt값이 올라가면 물확산
        if time != cnt:
            #물확산
            for k in range(n):
                wy,wx = inW.popleft()
                for h in range(4):
                    wyy = wy+dy[h]
                    wxx = wx+dx[h]
                    if wyy <0 or wyy >= R or wxx <0 or wxx >=C: continue
                    if arr[wyy][wxx]=='.' or arr[wyy][wxx] =='S':
                        arr[wyy][wxx] = '*'
                        inW.append((wyy,wxx))
            time += 1


    print('KAKTUS')

bfs()