import sys
arr = []
N, L = map(int,input().split())
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

done = set()
cnt = 0
#가로 검사
for i in range(N):
    #직전 숫자, 연속 수
    m1= [arr[i][0],0]
    #조사여부
    stat1 = False
    #통과여부
    stat = True
    tmp = set()
    for j in range(N):
        if arr[i][j] != m1[0]:
            if abs(arr[i][j] - m1[0]) > 1:
                stat = False
                break
            #조사 중이었다면
            if stat1 is True:
                stat1 = False
                if m1[1] < L:
                    stat = False
                    break
                else:
                    for h in range(m1[1],m1[1]-L,-1):
                        if (i,j-h) in done or (i,j-h) in tmp:
                            stat =False
                            break
                        tmp.add((i,j-h))

            if m1[1] >= L and arr[i][j] - m1[0] == 1:
                for k in range(L,0,-1):
                    if (i,j-k) in done or (i,j-k) in tmp:
                        stat = False
                        break
                    tmp.add((i,j-k))
                #그냥 계속 진행
                m1[0] = arr[i][j]
                m1[1] = 0
            elif m1[0] - arr[i][j] == 1:
                stat1 = True
                m1[0] = arr[i][j]
                m1[1] = 0
            else:
                stat =False
                break
        m1[1] += 1
    if stat1 is True:
        if m1[1] < L:
            stat = False
        else:
            for h in range(m1[1]-1, m1[1]-L,-1):
                if (i, j - h) in done or (i, j - h) in tmp:
                    stat = False
                    break
                tmp.add((i, j - h))
    if stat is True:
        cnt += 1
        done.update(tmp)

done = set()
#세로검사
for b in range(N):
    #직전 숫자, 연속 수
    m2= [arr[0][b],0]
    #조사여부
    stat2 = False
    #통과여부
    stat = True
    tmp = set()
    for a in range(N):
        if arr[a][b] != m2[0]:
            if abs(arr[a][b] - m2[0]) > 1:
                stat = False
                break
            #조사 중이었다면
            if stat2 is True:
                stat2 = False
                if m2[1] < L:
                    stat = False
                    break
                else:
                    for h in range(m2[1],m2[1]-L,-1):
                        if (a-h,b) in done or (a-h,b) in tmp:
                            stat =False
                            break
                        tmp.add((a-h,b))

            if m2[1] >= L and arr[a][b] - m2[0] == 1:
                for k in range(L,0,-1):
                    if (a-k,b) in done or (a-k,b) in tmp:
                        stat =False
                        break
                    tmp.add((a-k,b))
                #그냥 계속 진행
                m2[0] = arr[a][b]
                m2[1] = 0
            elif m2[0] - arr[a][b] == 1:
                stat2 = True
                m2[0] = arr[a][b]
                m2[1] = 0
            else:
                stat =False
                break
        m2[1] += 1
    if stat2 is True:
        if m2[1] < L:
            stat = False
        else:
            for h in range(m2[1]-1,m2[1]-L,-1):
                if (a - h, b) in done or (a - h, b) in tmp:
                    stat = False
                    break
                tmp.add((a - h, b))
    if stat is True:
        cnt += 1
        done.update(tmp)
print(cnt)