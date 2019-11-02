from collections import deque
from copy import deepcopy
R,C,T = map(int, input().split())
arr = []
cleaner = []
for _ in range(R):
    li = list(map(int, input().split()))
    for l in range(len(li)):
        if li[l] == -1:
            #공기청정기 위치
            cleaner.append([_,l])
    arr.append(li)
dy = [-1,1,0,0]
dx = [0,0,-1,1]
while T>0:
    #달라질 부분 담을 배열
    tmp= deepcopy(arr)
    target = deque()
    #미세먼지확산
    for i in range(R):
        for j in range(C):
            #미세먼지 있으면
            if arr[i][j]>0:
                target.append([i,j])
    for i,j in target:
        #확산량
        num = arr[i][j]//5
        if num == 0:
            continue
        for k in range(4):
            ny = i+dy[k]
            nx = j+dx[k]
            if ny<0 or ny>=R or nx<0 or nx>=C or tmp[ny][nx] == -1:
                continue
            #조건 만족 시 확산(tmp에)
            tmp[ny][nx] += num
            #원래 미세먼지 자리 빼주기
            tmp[i][j] -= num

    arr[:] =tmp[:]
    #tmp 초기화
    tmp = [[-3] * C for _ in range(R)]
    for i, j in cleaner:
        tmp[i][j] = -1
    #공기청정기 작동
    stat = False #False면 위쪽(반시계)
    for a,b in cleaner:
        if stat is False:#반시계일때
            tmp[a][1] = 0
            #아래쪽
            for c in range(1,C-1):
                tmp[a][c+1] = arr[a][c]
            #오른쪽
            for c in range(a-1,-1,-1):
                tmp[c][C-1] = arr[c+1][C-1]
            #위쪽
            for c in range(C-2, -1,-1):
                tmp[0][c] = arr[0][c+1]
            #왼쪽
            for c in range(1,a):
                tmp[c][0] = arr[c-1][0]

            stat = True
        else:#시계일때
            tmp[a][1] = 0
            #위쪽
            for c in range(1, C - 1):
                tmp[a][c + 1] = arr[a][c]
            #오른쪽
            for c in range(a+1, R):
                tmp[c][C-1] = arr[c-1][C-1]
            #아래쪽
            for c in range(C-2, -1,-1):
                tmp[R-1][c] = arr[R-1][c+1]
            #왼쪽
            for c in range(R-2,a,-1):
                tmp[c][0] = arr[c+1][0]

            stat = False

    #arr와 비교해서 다른부분만 교체
    for i in range(R):
        for j in range(C):
            #변경 부분있으면 바꿔주기
            if tmp[i][j] != -3 and tmp[i][j] != -1:
                arr[i][j] = tmp[i][j]
    T -= 1

#미세먼지 합
res = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]>0:
            res += arr[i][j]
print(res)