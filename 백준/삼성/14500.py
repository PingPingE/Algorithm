import sys
N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split() )))
tw = []
th =[]
for i in range(N):
    # 가로
    w = []
    # 세로
    h = []
    for j in range(M):
        if j+1 < M:
            tmp1 = arr[i][j] + arr[i][j+1]
            w.append(tmp1)

        if i+1 < N:
            tmp2 = arr[i][j] + arr[i+1][j]
            h.append(tmp2)
    tw.append(w)
    if len(h) > 0:
        th.append(h)
#tw
wx1 = [2,0,1,-1]
wy1 = [0,1,1,1]
hx1 = [0,1,0,1]
hy1 = [1,1,-2,-2]

#th
wx2 = [1,1,-2,-2]
wy2 = [0,1,0,1]
hx2 = [-1,1,0]
hy2 = [1,1,2]
max = 0
for i in range(N):
    for j in range(M):
        y = i
        x = j
        try:
            tmpW = tw[y][x]
            #tmpW-------------
            #w 탐색
            for k in range(4):
                ny = y+wy1[k]
                nx = x+wx1[k]
                if ny <0 or nx <0 or ny>=N or nx >=M-1:
                    continue
                if (tmpW + tw[ny][nx]) > max:
                    max = tmpW+tw[ny][nx]


            #h탐색
            for g in range(4):
                ny = y+hy1[g]
                nx = x+hx1[g]
                if ny< 0 or nx < 0 or ny >=N-1 or nx >= M:
                    continue
                if (tmpW + th[ny][nx]) > max:
                    max = tmpW+th[ny][nx]

            # ㅗ , ㅜ, ㅏ, ㅓ 탐색
            temp = 0
            if y - 1 >= 0 and y + 1 < N:
                # ㅏ
                if temp < (tmpW + arr[y + 1][x] + arr[y - 1][x]):
                    temp = tmpW + arr[y + 1][x] + arr[y - 1][x]

                if x + 1 < M - 1:
                    # ㅓ
                    if temp < (tmpW + arr[y + 1][x + 1] + arr[y - 1][x + 1]):
                        temp = tmpW + arr[y + 1][x + 1] + arr[y - 1][x + 1]
            if x + 2 < M - 1:
                if y - 1 >= 0:
                    # ㅗ
                    if temp < (tmpW + arr[y - 1][x + 1] + arr[y][x + 2]):
                        temp = tmpW + arr[y - 1][x + 1] + arr[y][x + 2]

                if y + 1 < N:
                    # ㅜ
                    if temp < (tmpW + arr[y][x + 2] + arr[y + 1][x + 1]):
                        temp = tmpW + arr[y][x + 2] + arr[y + 1][x + 1]
            if temp > max:
                max = temp
        except:
            pass

        # tmpH-------------
        try:
            tmpH = th[y][x]
            # w 탐색
            for a in range(4):
                ny = y + wy2[a]
                nx = x + wx2[a]
                if ny <0 or nx <0 or ny>=N or nx >=M-1:
                    continue

                if (tmpH + tw[ny][nx]) > max:
                    max = tmpH + tw[ny][nx]

                # h탐색
            for b in range(3):
                ny = y + hy2[b]
                nx = x + hx2[b]
                if ny < 0 or nx < 0 or ny >= N-1 or nx >= M:
                    continue
                if (tmpH + th[ny][nx]) > max:
                    max = tmpH + th[ny][nx]

            # ㅗ , ㅜ, ㅏ, ㅓ 탐색
            temp = 0
            if y + 2 < N - 1:
                if x + 1 < M:
                    # ㅏ
                    if temp < (tmpH + arr[y + 2][x] + arr[y + 1][x + 1]):
                        temp = tmpH + arr[y + 2][x] + arr[y + 1][x + 1]

                if x - 1 >= 0:
                    # ㅓ
                    if temp < (tmpH + arr[y + 2][x] + arr[y + 1][x - 1]):
                        temp = tmpH + arr[y + 2][x] + arr[y + 1][x - 1]
            if x + 1 < M and x - 1 >= 0:
                if y + 1 < N - 1:
                    # ㅗ
                    if temp < (tmpH + arr[y + 1][x - 1] + arr[y + 1][x + 1]):
                        temp = tmpH + arr[y + 1][x - 1] + arr[y + 1][x + 1]
                # ㅜ
                if temp < (tmpH + arr[y][x - 1] + arr[y][x + 1]):
                    temp = tmpH + arr[y][x - 1] + arr[y][x + 1]

            if temp > max:
                max = temp
        except:
            continue

print(max)














