import sys
sys.setrecursionlimit(10**9)
def check():#i -> i 체크
    for start in range(N):
        cur = start
        for i in range(H):
            cur += arr[i][cur]
        if  cur != start:
            return False
    return True

def solution(y,cnt):
    global arr, res
    if check():
        res = min(res, cnt)
        return
    for i in range(y,H):
        for j in range(N):
            if arr[i][j] ==0 and arr[i+1][j] == 0 and arr[-1][j] == 0:
                arr[i][j] =  1
                solution(i,cnt+1)
                arr[i][j] = 0

N,M,H = map(int, input().split())
arr =[[0]*N for _ in range(H)]
res = sys.maxsize
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1
# print(arr)
solution(0, 0)
if res == sys.maxsize: res = -1
print(res)
