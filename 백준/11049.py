#dp 문제인듯
import sys
sys.setrecursionlimit(10**9)
N = int(input())
mini = sys.maxsize
arr = [list(map(int,input().split())) for _ in range(N)]

def dfs(num,cur, left, right):
    global mini
    if num >= mini: return
    if not left and not right:
        mini=min(mini, num)
        return

    if left:
        top = left[-1]
        dfs(num+(top[0]*top[1]*cur[1]),(top[0],cur[1]), left[:-1], right[:])

    if right:
        top = right[0]
        dfs(num + (cur[0] * cur[1] * top[1]), (cur[0], top[1]), left[:], right[1:])

for n in range(N):
    dfs(0,arr[n],arr[:n],arr[n+1:])
print(mini)