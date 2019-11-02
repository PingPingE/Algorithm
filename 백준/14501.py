# from collections import deque
# N = int(input())
# sch = []
# for _ in range(N):
#     #걸리는 일수, 보상
#     sch.append(list(map(int, input().split())))
# #보상
# res = 0
# que = deque()
# #첫 상담: 모든 인덱스와 보상(처음 0) 넣기
# for n in range(N):
#     que.append((n,0))
# while que:
#     ind,curR = que.popleft()
#     days = sch[ind][0]
#     reward = sch[ind][1]
#     #가능여부 체크
#     if ind+days<=N:
#         curR += reward
#         #넣을 땐 가능여부 체크 안함
#         for i in range(ind+days, N):
#             que.append((i, curR))
#         res = max(res, curR)
#
# print(res)

#숏코딩
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [0]* (n+1)
for i in range(n):
    for j in range(i + board[i][0], n+1):
        dp[j] = max(dp[i] + board[i][1], dp[j])
print(dp[n])