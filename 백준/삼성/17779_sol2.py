#125788kb	524ms
import sys
from itertools import product
N = int(input())
A = [[0]*(N+1)]
for _ in range(N):
    tmp = [0]+list(map(int, sys.stdin.readline().split()))
    A.append(tmp)
ret = 987654321
tmp = [list(range(1,N+1))]
tmp.append(list(range(1,N+1)))
for p in product(*tmp):#기준점
    x,y=p
    #경계 길이
    for d1 in range(1,N+1):
        for d2 in range(1,N+1):
            if 1<=x<x+d1+d2 and x+d1+d2<=N and 1<=y-d1<y and y<y+d2<=N:
                board = [[0] * (N + 1) for _ in range(N + 1)]
                count = [0 for _ in range(6)]
                for i in range(d1+1):
                    board[x+i][y-i] = 5

                for j in range(d2+1):
                    board[x+j][y+j] = 5

                for k in range(d2+1):
                    board[x+d1+k][y-d1+k] = 5

                for m in range(d1+1):
                    board[x+d2+m][y+d2-m] = 5

                for r in range(1,N+1):
                    s,e = 1,1
                    stat = False
                    while e<N+1:
                        if board[r][e]== 5:
                            if stat^1:
                                if 5 in board[r][e+1:]:
                                    stat = True
                                    s=e
                                    e+=1
                                else:
                                    count[5] += A[r][e]
                                    break
                            else:
                                e+=1
                                break
                        else:
                            e+=1
                    if stat:
                        for j in range(s,e):
                            board[r][j] =5
                            count[5] += A[r][j]
                #1번
                for r in range(1,x+d1):
                    for c in range(1,y+1):
                        if board[r][c]!=0:continue
                        board[r][c] = 1
                        count[1]+=A[r][c]

                #2번
                for r in range(1,x+d2+1):
                    for c in range(y+1,N+1):
                        if board[r][c] != 0: continue
                        board[r][c] = 2
                        count[2]+=A[r][c]

                #3번
                for r in range(x+d1,N+1):
                    for c in range(1,y-d1+d2):
                        if board[r][c] != 0: continue
                        board[r][c] = 3
                        count[3]+=A[r][c]

                #4번
                for r in range(x+d2+1, N+1):
                    for c in range(y-d1+d2, N+1):
                        if board[r][c] != 0: continue
                        board[r][c] =4
                        count[4]+=A[r][c]
                if min(count[1:]) == 0: continue
                ret = min(ret, max(count[1:])- min(count[1:]))

print(ret)