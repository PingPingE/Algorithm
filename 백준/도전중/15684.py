import sys
sys.setrecursionlimit(10**9)
def check():#i -> i 체크
    for start in range(N):
       pos = start
       while True:
            r,c = pos//N, pos%N
            pos += arr[r][c]
            if pos+N >= N*H:
               break
            pos += N #내려가기
       if pos%N != start:return False
    return True

def solution(pos, cnt):
    global arr, res
    if check():
        res = min(res, cnt)
        return
    if cnt == 3 or pos >= N*H or cnt>=res:
        return
    for next_pos in range(pos, N*H):
        r,c = next_pos//N, next_pos%N
        if c+1<N and arr[r][c]==0 and arr[r][c+1] == 0:
            arr[r][c] = right
            arr[r][c+1] = left
            # print("before: ",arr)
            solution(pos+1, cnt+1)
            arr[r][c] = 0
            arr[r][c+1] = 0

left,right=-1,1
N,M,H = map(int, input().split())
arr =[[0]*N for _ in range(H)]
res = sys.maxsize
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = right
    arr[a-1][b] = left
# print(arr)
solution(0, 0)
if res == sys.maxsize: res = -1
print(res)
