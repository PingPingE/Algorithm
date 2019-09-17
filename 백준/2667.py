import sys
from collections import deque
N=int(input())
arr = deque()
for _ in range(N):
    arr.append(list(map(str,sys.stdin.readline().rstrip())))

#방문여부 체크
done = []

def sol(y,x,cnt):
    global  arr,N
    dy = [-1, 1, 0, 0]#상하
    dx = [0, 0, -1, 1]#좌우
    #상하좌우 살피기
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        #범위 벗어났는지 체크
        if ((ny,nx) in done) or ny <0 or nx<0 or nx>=N or ny >=N:
            continue

        if int(arr[ny][nx]) == 1:
            done.append((ny,nx))
            cnt = sol(ny,nx,cnt+1)
    return cnt

#결과값 저장
res = []
#처음부터 모든 값 돌기
for a in range(N):
    for b in range(N):
        #done에 없고(방문 전이고), 값이 1인 곳 찾기
        if ((a,b) not in done) and int(arr[a][b]) == 1:
            done.append((a,b))
            res.append(sol(a,b,1))

print(len(res))
#정렬
res.sort()
for r in res:
    print(r)

