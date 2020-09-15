'''
문제)
이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 블록은 적어도 하나 주어진다.

출력)
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''
#132708kb	412ms
import sys
from collections import deque
N = int(input())
board = list( list(map(int, sys.stdin.readline().split() ))for _ in range(N))
que = deque()
que.append((list(b[:] for b in board),0)) #현재 보드, 움직인 횟수
res = 0
for o in board:
    tmp = max(o)
    res = max(res, tmp)
while que:
    cur, cnt = que.popleft()
    if cnt == 5:
        continue
    for d in range(4):
        tboard = [[0] * N for _ in range(N)]
        if d==0: #상
            for i in range(N):#열 시작
                count = 0 #행 시작
                y,x = 0,i
                while y<N and cur[y][x] ==0:
                    y += 1
                while 0<=y<N and 0<=x<N and cur[y][x]!=0:
                    ny = y+1
                    while ny<N and cur[ny][x] == 0:
                        ny += 1
                    if ny>=N or cur[ny][x] == 0:
                        tboard[count][i] = cur[y][x]
                        break
                    if cur[ny][x] == cur[y][x]:
                        tboard[count][i] = cur[ny][x]*2
                        y =ny+1
                        while y < N and cur[y][x] == 0:
                            y += 1
                    else:
                        tboard[count][i] = cur[y][x]
                        y = ny
                    res = max(res, tboard[count][i])
                    count += 1
        elif d==1:#하
            for i in range(N):#열 시작
                count = N-1 #행 시작
                y,x = N-1,i
                while y>=0 and cur[y][x] ==0:
                    y -= 1
                if cur[y][x] == 0: continue
                while 0<=y<N and 0<=x<N and cur[y][x]!=0:
                    ny = y-1
                    while ny>=0 and cur[ny][x] == 0:
                        ny -= 1
                    if ny<0 or cur[ny][x] == 0:
                        tboard[count][i] = cur[y][x]
                        break
                    if cur[ny][x] == cur[y][x]:
                        tboard[count][i] = cur[ny][x]*2
                        y = ny-1
                        while y >= 0 and cur[y][x] == 0:
                            y -= 1
                    else:
                        tboard[count][i] = cur[y][x]
                        y = ny
                    res = max(res, tboard[count][i])
                    count -= 1
        elif d==2: #좌
            for i in range(N):#행 시작
                count = 0 #열 시작
                y,x = i,0
                while x<N and cur[y][x] ==0:
                    x += 1
                while 0<=y<N and 0<=x<N and cur[y][x]!=0:
                    nx = x+1
                    while nx<N and cur[y][nx] == 0:
                        nx += 1
                    if nx>=N or cur[y][nx] == 0:
                        tboard[i][count] = cur[y][x]
                        break
                    if cur[y][nx] == cur[y][x]:
                        tboard[i][count] = cur[y][nx]*2
                        x = nx+1
                        while x < N and cur[y][x] == 0:
                            x += 1
                    else:
                        tboard[i][count] = cur[y][x]
                        x = nx
                    res = max(res, tboard[i][count])
                    count += 1
        else:#우
            for i in range(N):  # 행 시작
                count = N-1  # 열 시작
                y, x = i, N-1
                while x>0 and cur[y][x] ==0:
                    x -= 1
                while 0 <= y < N and 0 <= x < N and cur[y][x]!=0:
                    nx = x-1
                    while nx>=0 and cur[y][nx] == 0:
                        nx -= 1
                    if nx<0 or cur[y][nx] == 0:
                        tboard[i][count] = cur[y][x]
                        break
                    if cur[y][nx] == cur[y][x]:
                        tboard[i][count] = cur[y][nx] * 2
                        x = nx-1
                        while x >= 0 and cur[y][x] == 0:
                            x -= 1
                    else:
                        tboard[i][count] = cur[y][x]
                        x = nx
                    res = max(res, tboard[i][count])
                    count -= 1
        que.append((list(t[:] for t in tboard),cnt+1))
print(res)