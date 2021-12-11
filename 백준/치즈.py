#1 찾기 -> 해당 위치를 기준으로 사방에 0이 하나라도 있는지 체크 -> 진짜 완전 뚫린 구멍인지 확인

import sys
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())
time, cnt_arr = 0,[]
dy,dx= [0,0,1,-1], [1,-1,0,0]
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]


def is_whole(y,x,d):
    while True:
        y += dy[d]
        x += dx[d]
        if 0<=y<N and 0<=x<M:
            if arr[y][x] == 1:
                return False
        else:
            return True

def check(y,x):
    for d in range(4):
        ny,nx = y+dy[d], x+dx[d]
        if 0<=ny<N and 0<=nx<M and arr[ny][nx]==0:
            if is_whole(ny,nx,d):
                return True
        elif ny<0 or ny>=N or nx<0 or nx>=M:
            return True
        else: pass
    return False

def print_arr():
    for r in range(N):
        print(arr[r])


while True:
    flag=False
    cnt=0
    new_arr = [arr[i][:] for i in range(N)]
    print_arr()
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                flag=True
                cnt += 1
                if check(r,c):
                    new_arr[r][c] = 0


    if flag:
        time+=1
        arr = [new_arr[i][:] for i in range(N)]
        print("===after")
        print_arr()

        cnt_arr.append(cnt)
    else:
        break
print(cnt_arr)
print(time, cnt_arr[-1])