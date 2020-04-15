from collections import deque
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
res = 0
que = deque()
for i in range(4):
    que.append([board[:][:], 1,i])
while que:
    #배열, 이동 횟수, 이동 할 방향
    arr, count, dir = que.popleft()
    tmp = [[0 for i in range(N)]for j in range(N)]

    if dir ==0:
        for x in range(N):
            top = 0#tmp에 넣을 순서
            cur = -1  # 현재 비교대상
            for r in range(N):
                if arr[r][x] == 0:
                    continue
                else:
                    #비교대상이 있는지
                    if cur == -1:
                        cur = r
                    #있으면 비교
                    else:
                        if arr[cur][x] == arr[r][x]:
                            tmp[top][x] = arr[r][x]*2
                            top +=1
                            cur = -1
                        else:
                            #다르면 그냥 cur값만 넣어주고 cur갱신
                            tmp[top][x] = arr[cur][x]
                            top += 1
                            cur = r
            # 마지막 비교대상이 있는데 맨뒤 or 0만 나와서 처리 못한경우
            if cur != -1:
                tmp[top][x] = arr[cur][x]

    elif dir ==1:
        for x in range(N):
            bottom = N - 1
            cur = -1  # 현재 비교대상
            for r in range(N-1, -1,-1):
                if arr[r][x] == 0:
                    continue
                else:
                    # 비교대상이 있는지
                    if cur == -1:
                        cur = r
                    # 있으면 비교
                    else:
                        if arr[cur][x] == arr[r][x]:
                            tmp[bottom][x] = arr[r][x] * 2
                            bottom -= 1
                            cur = -1
                        else:
                            # 다르면 그냥 cur값만 넣어주고 cur갱신
                            tmp[bottom][x] = arr[cur][x]
                            bottom -= 1
                            cur = r
            # 마지막 비교대상이 있는데 맨뒤 or 0만 나와서 처리 못한경우
            if cur != -1:
                tmp[bottom][x] = arr[cur][x]


    elif dir ==2:
        for y in range(N):
            #tmp에 놓을 인덱스
            left = 0
            cur = -1  # 현재 비교대상
            for x in range(N):
                if arr[y][x] == 0:
                    continue
                else:
                    if cur ==-1:
                        cur = x
                    else:
                        if arr[y][cur] == arr[y][x] :
                            tmp[y][left] = arr[y][x]*2
                            left += 1
                            cur = -1
                        else:
                            #다르면 그냥 cur값만 넣어주고 cur갱신
                            tmp[y][left] = arr[y][cur]
                            left += 1
                            cur = x
            # 마지막 비교대상이 있는데 맨뒤 or 0만 나와서 처리 못한경우
            if cur != -1:
                tmp[y][left] = arr[y][cur]

    else:
        for y in range(N):
            right = N-1
            cur = -1  # 현재 비교대상
            for x in range(N-1, -1,-1):
                if arr[y][x] == 0:
                    continue
                else:
                    if cur ==-1:
                        cur = x
                    else:
                        if arr[y][cur] == arr[y][x] :
                            tmp[y][right] = arr[y][x]*2
                            right -= 1
                            cur = -1
                        else:
                            #다르면 그냥 cur값만 넣어주고 cur갱신
                            tmp[y][right] = arr[y][cur]
                            right -= 1
                            cur = x
            #마지막 비교대상이 있는데 맨뒤 or 0만 나와서 처리 못한경우
            if cur != -1:
                tmp[y][right] = arr[y][cur]


    #최댓값
    for h in range(N):
        res = max(res, max(tmp[h]))

    if count <5:
        for i in range(4):
            que.append([tmp, count+1, i])

print(res)
