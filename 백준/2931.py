#4시 52분 시작
R,C = map(int,input().split())
blank = []
block= {'|':0, '-':1,'+':2, '1':3,'2':4,'3':5,'4':6}
M = (0,0)
Z = (0,0)
board = []
for _ in range(R):
    li = list(input())
    for l in range(len(li)):
        if li[l] in  block:
            li[l] = block[li[l]]
        elif li[l] =='M':
            M = (_,l)
            li[l] = -1
        elif li[l] == 'Z':
            Z=(_,l)
            li[l] = -1
        else:
            blank.append((_,l))
    board.append(li)

def sol():
    global board,M,Z,R,C
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    r= M[0]
    c = M[1]
    #처음으로 가야할 곳 찾기
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if ny < 0 or nx < 0 or ny >= R or nx >= C or board[ny][nx] == '.' or (ny,nx) == Z:
            continue
        r,c = ny,nx
        break
    #M->Z갈 수 있는지 check하기
    while 0<=r<R and 0<=c<C :
        if (r,c) == Z:
            return True
        elif board[r][c] != '.' and 0<=board[r][c]:
            # 0~2번 블록까지는 그대로
            if board[r][c] in range(3):
                if board[r][c] == 0:
                    if i not in [0,1]:
                        return False
                elif board[r][c] == 1:
                    if i not in [2,3]:
                        return False
                r, c = r+dy[i], c+dx[i]
            elif board[r][c] == 3:
                if i == 0:  # 위로 가다가
                    c +=  1
                    i = 3
                elif i == 2:  # 왼쪽으로 가다가
                    r += 1
                    i = 1
                else:
                    return False

            elif board[r][c] == 4:
                if i == 1:  # 아래로 가다가
                    c += 1
                    i = 3
                elif i == 2:  # 왼쪽으로 가다가
                    r -= 1
                    i = 0
                else:
                    return False

            elif board[r][c] == 5:
                if i == 1:
                    c -= 1
                    i=2
                elif i == 3:
                    r -= 1
                    i=0
                else:
                    return False

            else:
                if i == 0:#위
                    c -= 1#왼
                    i = 2
                elif i == 3:
                    r += 1
                    i = 1
                else:
                    return False
        else:
            return False
    return False

#각빈칸마다 모든 블록 다 넣어보기
stat = False
for y,x in blank:
    for n in list(range(7)):
        board[y][x] = n
        if sol() is True:
            resR = y+1
            resC = x+1
            resN = n
            stat = True
            break
        board[y][x] = '.'
    if stat is True:
        break

for k in block:
    if block[k] == resN:
        resN = k
        break
strr = str(resR)+' '+str(resC) +' '+str(resN)
print(strr)