#미로탐색
#1: 이동 가능 0: 불가능
#브루트포스 + BFS
import sys
arr = []
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    tmp = input()
    arr.append(list(tmp))

def bfs(arr):
    global N,M
    #y,x,count
    que = [(0,0,1)]
    done = [(0,0)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    result = -1
    cnt = 0
    while que:
        q = que.pop(0)
        cnt =q[2]
        y = int(q[0])
        x = int(q[1])

        if y==N-1 and x == M-1:
            if result == -1 or cnt<result:
                result = cnt
                continue

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or ny>=N or  nx<0 or nx>=M:
                continue
            if arr[ny][nx] == '1' and (ny,nx) not in done:
                done.append((ny,nx))
                que.append((ny,nx,cnt+1))
    return result

print(bfs(arr))