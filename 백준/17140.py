def solC():
    global A, maxR, maxC
    tmpR = 0
    for i in range(maxC):
        # 배열의 인덱스 : 수, 해당 인덱스의 값: 등장횟수
        num = [101 for _ in range(101)]
        for j in range(maxR):
            if A[j][i] == 0:
                continue
            if num[A[j][i]] == 101:
                num[A[j][i]] = 1
            else:
                num[A[j][i]] += 1

        # 한 열 끝나면
        minn = 0
        jj = 0
        cnt = 0
        # 100넘었는지
        stat = False
        while min(num) < 101:
            minn = min(num)
            for k in range(len(num)):
                if num[k] == minn:
                    if jj < 100:
                        A[jj][i] = k
                        jj += 1
                        A[jj][i] = num[k]
                        jj += 1
                        cnt += 2
                    else:
                        stat = True
                        break

                    num[k] = 101
            if stat is True:
                break
        if cnt > tmpR:
            tmpR = cnt

        for cc in range(cnt, max(maxR, tmpR)):
            A[cc][i] = 0
    maxR = tmpR

def solR():
    global A, maxR, maxC
    tmpC = 0
    for i in range(maxR):
        # 배열의 인덱스 : 수, 해당 인덱스의 값: 등장횟수
        num = [101 for _ in range(101)]
        for j in range(maxC):
            if A[i][j] == 0:
                continue
            if num[A[i][j]] == 101:
                num[A[i][j]] = 1
            else:
                num[A[i][j]] += 1
        # 한 행 끝나면
        minn = 0
        jj = 0
        stat = False
        # 컬럼 수 세기
        cnt = 0
        while min(num) < 101:
            minn = min(num)
            for k in range(len(num)):
                if num[k] == minn:
                    if jj < 100:
                        A[i][jj] = k
                        jj += 1
                        A[i][jj] = num[k]
                        cnt += 2
                        jj += 1
                    else:
                        stat = True
                        break
                    # 넣은건 101로 초기화
                    num[k] = 101
            if stat is True:
                break
        # 나머지 0으로 채움
        if cnt > tmpC:
            tmpC = cnt
        for cc in range(cnt, max(maxC, tmpC)):
            A[i][cc] = 0
    maxC = tmpC

r,c,K = map(int,input().split())
r -= 1
c -= 1
A = [[0]*100 for _ in range(100)]
for _ in range(3):
    li  = list(map(int, input().split()))
    j = 0
    for l in li:
        A[_][j] = l
        j+= 1

time = 0
#최대 행과 열 개수(인덱스X)
maxR = 3
maxC = 3
while time <= 100:
    if A[r][c] == K:
        break
    time += 1
    if maxR >= maxC:#R연산
        solR()
    else:#C연산
        solC()

if time> 100:
    print(-1)
else:
    print(time)
