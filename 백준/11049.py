import sys
INF = sys.maxsize
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
memo= [[INF for j in range(N)] for i in range(N)]

for i in range(N-1):
    memo[i][i] =0
    memo[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]
memo[-1][-1] = 0

for k in range(N-1):
    for i in range(k):
        for j in range(k+1,N):
            memo[i][j] = min(memo[i][k-1] + memo[k][j] + (arr[i][0] * arr[j][0] * arr[j][1]),memo[i][j])
print(memo)
print(memo[0][-1])

# def dfs(num,cur, left, right):
#     global mini
#     if num >= mini: return
#     if not left and not right:
#         mini=min(mini, num)
#         return
#
#     if left:
#         top = left[-1]
#         dfs(num+(top[0]*top[1]*cur[1]),(top[0],cur[1]), left[:-1], right[:])
#
#     if right:
#         top = right[0]
#         dfs(num + (cur[0] * cur[1] * top[1]), (cur[0], top[1]), left[:], right[1:])
#
# for n in range(N):
#     dfs(0,arr[n],arr[:n],arr[n+1:])
# print(mini)