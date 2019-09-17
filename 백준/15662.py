#14891번도 비슷
import time
from collections import deque
start= time.time()
T = 4
arr = {}
for _ in range(T):
    arr[_+1] = deque()
    arr[_+1].extend(list(map(int,input())))
K = int(input())
#n번째 톱니바퀴 w로 돌리기(-1 : 반시계, 1: 시계)
def move(n,w):
    global arr
    if w==-1:
        tmp = arr[n].popleft()
        arr[n].append(tmp)
    else:
        tmp = arr[n].pop()
        arr[n].appendleft(tmp)
for _ in range(K):
    stat = [0]*(T + 1)
    n,w = map(int, input().split())
    r, l = arr[n][2], arr[n][6]
    stat[n] = w
    for a in range(n,0,-1):
        if stat[a] == 0:
            break
        if a-1 in arr:
            if arr[a-1][2] != l:
                #돌려야하면 표시
                stat[a-1] = -w
                w= -w
                l = arr[a - 1][6]
    #초기화
    w = stat[n]
    for b in range(n, T+1):
        if stat[b] == 0:
            break
        if b + 1 in arr:
            if arr[b+1][6] != r:
                stat[b+1] =-w
                w= -w
                r = arr[b + 1][2]
    #돌리기
    for k in range(1,T+1):
        if stat[k] != 0:
            move(k,stat[k])

cnt = 0
for i in range(1,T+1):
    cnt += arr[i][0]*(2**(i-1))

print(cnt)
print(time.time()-start)

#시간 별로 안걸리는 코드
# def needRotate(leftGear, rightGear):
#     if leftGear[2] != rightGear[-2]:
#         return True
#     return False
#
# def rotate(gears, index, direction, rotated):
#     if index in rotated:
#         # Already rotated
#         return
#     rotated.append(index)
#     if index + 1 < len(gears):
#         if needRotate(gears[index], gears[index + 1]):
#             rotate(gears, index + 1, -direction, rotated)
#     if index - 1 >= 0:
#         if needRotate(gears[index - 1], gears[index]):
#             rotate(gears, index - 1, -direction, rotated)
#     if direction == 1:
#         gears[index] = gears[index][-1:] + gears[index][:-1]
#     else:
#         gears[index] = gears[index][1:] + gears[index][:1]
#
# def score(gears):
#     ans = 0
#     for i, gear in enumerate(gears):
#         if gear[0] == '1':
#             ans += 2 ** i
#     return ans
#
# gears = []
# for _ in range(4):
#     gears.append(list(input()))
#
# for _ in range(int(input())):
#     i, d = map(int, input().split())
#     rotate(gears, i - 1, d, [])
# print(score(gears))