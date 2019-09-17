from collections import deque
N = int(input())
m = {0: (0,1), 1:(-1,0), 2:(0,-1), 3:(1,0)}
#드래곤 커브의 일부면 (x,y)에 1로 표시
arr = [[0 for _ in range(101)] for _ in range(101)]
while N >0:
    N -= 1
    x,y,d,g = map(int, input().split())
    arr[y][x] = 1
    prev = deque()
    #끝 점
    end = (y + m[d][0], x + m[d][1])
    arr[end[0]][end[1]] = 1
    prev.append(d)
    for i in range(g):
        tmp = deque()
        for j in range(len(prev)):
            d = prev[j]+1
            if d > 3:
                d = 0
            if 0<=end[0]<= 100 and   0<=end[1]<=100:
                arr[end[0]+m[d][0]][end[1]+m[d][1]] = 1
            end = (end[0]+m[d][0], end[1]+m[d][1])
            tmp.append(d)
        for t in tmp:
            prev.appendleft(t)
cnt =0
res = set()
for r in range(len(arr)):
    for rr in range(len(arr[r])):
        if arr[r][rr] == 1:
            res.add((r,rr))
dx = [1,0,1]
dy = [0,1,1]
for y,x in res:
    temp = 0
    for i in range(3):
        ny = y+dy[i]
        nx = x+dx[i]
        if (ny,nx) in res:
            temp +=1
    if temp >=3:
        cnt += 1
print(cnt)