from collections import deque
import sys
N,M= map(int, input().split())
board = []
red, blue ,goal= 0,0,0
for _ in range(N):
    li = list(sys.stdin.readline())
    for l in range(len(li)):
        if li[l] == 'R':
            red = [_,l]
        elif li[l] == 'B':
            blue = [_,l]
        elif li[l] == 'O':
            goal = [_,l]
    board.append(li)

que = deque()
#[red위치, blue위치, 현재cnt
que.append([red[:], blue[:], 0])
res = -1
dy = [-1,1,0,0]
dx = [0,0,-1,1]
done = set()
while que:
    r,b,cnt = que.popleft()
    done.add((r[0],r[1],b[0],b[1]))
    if cnt >= 10:
        break
    #red goal에 들어갔는지
    stat = False
    for i in range(4):
        rr, bb = r[:], b[:]
        #이전 값
        rb = [rr[:], bb[:]]
        while True:
            rny = rr[0]+dy[i]
            rnx = rr[1]+dx[i]
            if 0<=rny<N and 0<=rnx<M and board[rny][rnx] != '#':
                #현위치의 뒤
                rb[0] = rr[:]
                #현위치
                rr = [rny,rnx]
                if board[rny][rnx] == 'O':
                    break
            else:
                break

        while True:
            bny = bb[0]+dy[i]
            bnx = bb[1]+dx[i]
            if 0<=bny<N and 0<=bnx<M and board[bny][bnx] != '#':
                rb[1] = bb[:]
                bb = [bny,bnx]
                if board[bny][bnx] == 'O':
                    break
            else:
                break
        #파란구슬이 들어갔으면 그냥 continue
        if bb == goal:
            continue
        #둘이 만났을경우
        if rr==bb:
            #이동거리가 더 많은 구슬이 뒤로
            cR = abs(r[0]-rr[0])+ abs(r[1]-rr[1])
            cB = abs(b[0] -bb[0]) + abs(b[1]-bb[1])
            if cR > cB:
                #이전값 적용
                rr = rb[0]
            else:
                #이전값 적용
                bb = rb[1]
        #빨간구슬만 들어간경우 : 끝
        if rr == goal and bb != goal:
            res = cnt+1
            stat = True
            break
        else:
            if r != rr or b != bb:
                #done체크 (시간단축 엄청남)
                if (rr[0],rr[1],bb[0],bb[1]) not in done:
                    que.append([rr[:],bb[:], cnt+1])
            #두 구슬 모두 움직임이 없는 경우
            else:
                continue
    if stat is True:
        break
print(res)

