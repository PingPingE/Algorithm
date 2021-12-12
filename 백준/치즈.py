'''
문제
아래 <그림 1>과 같이 정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈(회색으로 표시된 부분)가 놓여 있다.
판의 가장자리(<그림 1>에서 네모 칸에 X친 부분)에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다. 치즈의 구멍 속에는 공기가 없지만
구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때, 
공기 중에서 치즈가 모두 녹아 없어지는 데 걸리는 시간과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고, 둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
'''

'''
풀이
- 0만 따라감
- 가면서 사방을 체크해서 1값을 가지는 위치가 가장자리
'''

#31780KB	140ms
import sys
from collections import deque
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())
time,cnt= 0,0
dy,dx= [0,0,1,-1], [1,-1,0,0]
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt+=1

def bfs():
    global cnt,arr
    #이전 위치의 ㅔ, y, x
    que = deque([[0,0,0]])
    new_arr = [arr[i][:] for i in range(N)]
    done=set([(0,0)])
    flag = False
    while que:
        prev, y,x = que.popleft()

        #이전에 0이었고, 이번값은 1이면 -> 가장자리
        if not prev and arr[y][x]:
            flag= True
            new_arr[y][x]=0
            cnt -=1
            continue

        for d in range(4):
            ny,nx = y+dy[d] , x+dx[d]
            if (ny,nx) not in done and 0<=ny<N and 0<=nx<M:
                done.add((ny,nx))
                que.append([arr[y][x], ny, nx])
    if flag:
        arr = [new_arr[i][:] for i in range(N)]


prev=cnt
while cnt > 0:
    prev = cnt
    time+=1
    bfs()

print(time)
print(prev)
