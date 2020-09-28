#126780kb	856ms
import sys
from collections import deque
from itertools import combinations
def get_safty_area(walls): #안전 영역 크기
    global board
    for w in walls:
        board[w[0]][w[1]] = 1
    done = set()
    que = deque(virus_space)
    while que:
        y,x = que.popleft()
        for d in range(4):
            ny = y+dy[d]
            nx = x+dx[d]
            if ny<0 or nx<0 or ny>=N or nx>=M or board[ny][nx] != 0 or (ny,nx) in done:
                continue
            que.append((ny,nx))
            done.add((ny,nx))
    for w in walls:
        board[w[0]][w[1]] = 0
    return len(empty_space)-3-len(done)

global board
N,M = map(int, input().split())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
dy,dx = [-1,1,0,0],[0,0,-1,1]
virus_space = set()
empty_space = set() #벽을 세울수 있는 공간
for e,b in enumerate(board):
    for i in range(len(b)):
        if b[i] == 0:
            empty_space.add((e,i))
        elif b[i] == 2:
            virus_space.add((e,i))

ret = 0
for c in list(combinations(empty_space, 3)):
    ret = max(ret, get_safty_area(c))
print(ret)

'''
#숏코딩(117420kb, 436ms)
o,b,a=[],[],0
N,M=map(int,input().split())
for r in range(N):o+=list(map(int,input().split()))
for i in range(N*M):
	if o[i]==0:b+=[i]
h=len(b)
for i in range(h-2):
    for j in range(i+1,h):
        for k in range(j+1,h):
            print(i,j,k)
            m,q=o[:],[]
            m[b[i]],m[b[j]],m[b[k]]=1,1,1
            for v in range(N*M):
                if m[v]==2:q+=[v]
            for v in q:
                if m[v] ==2:
                    U,R,D,L = v-M,v+1,v+M,v-1
                    if m[U] == 0 and U >= 0: m[U] = 2;q += [U]
                    if R < N * M and m[R] == 0 and R % M: m[R] = 2;q += [R]
                    if D < N * M and m[D] == 0: m[D] = 2;q += [D]
                    if m[L] == 0 and L % M != M - 1: m[L] = 2;q += [L]
            s=m.count(0)
            if a<s:a=s
print(a)
'''