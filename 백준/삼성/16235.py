import sys
def cal(r,c):
    return [(r-1,c-1),(r-1,c+1),(r-1,c),(r,c-1),(r,c+1),(r+1,c),(r+1,c-1),(r+1,c+1)]
N,M,K = map(int,input().split())
A = []
board = [[5]*N for _ in range(N)]
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
#위치: 나이
B = {}
res = M
for _ in range(M):
    y,x,z= map(int,sys.stdin.readline().split())
    y-=1
    x-=1
    if (y,x) not in B:
        B[(y,x)] = [z]
    else:
        B[(y,x)].append(z)
dy =[-1,-1,-1,0,0,1,1,1]
dx =[1,0,-1,1,-1,1,-1,0]
while K:
    tmpB = {}
    for k in B.keys():
        #각 칸의 나무들 나이로 정렬(오름차순)
        sK = sorted(B[k])
        for s in range(len(sK)):
            if board[k[0]][k[1]] < sK[s]:
                #죽은 나무들은 바로 양분으로
                for ss in sK[s:]:
                    board[k[0]][k[1]] += ss//2
                    res -= 1
                sK = sK[:s]
                break
            else:
                board[k[0]][k[1]] -= sK[s]
                sK[s] += 1
        B[k] = sK
        tmpB[k] = sK

    #새나무 심기
    for k,v in tmpB.items():
        #심어야할 나무 개수
        cnt = 0
        for vv in v:
            if vv%5 == 0:
                cnt += 1
        if cnt >0:
            for ny,nx in cal(k[0],k[1]):
                if ny < 0 or nx < 0 or ny >= N or nx >= N:
                    continue
                res += cnt
                if (ny,nx) in B:
                    B[(ny,nx)].extend([1 for _ in range(cnt)])
                else:
                    B[(ny,nx)] = [1 for _ in range(cnt)]
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j]
    K -= 1

print(res)

#숏코딩, 400ms
# import sys
# input = sys.stdin.readline
# def adj(r, c):
#     return [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
#
# n, m, k = map(int, input().split())
#
# a = [list(map(int, input().split())) for _ in range(n)]
# nuts = [[5]*n for i in range(n)]
# trees = [[[] for __ in range(n)] for _ in range(n)]
#
# for i in range(m):
#     x, y, z = map(int, input().split())
#     trees[x-1][y-1].append(z)
#
# def spring_and_summer():
#     for i in range(n):
#         for j in range(n):
#             nut = nuts[i][j]
#             new, s = [], 0
#             for u in trees[i][j]:
#                 if u <= nut:
#                     nut -= u
#                     new.append(u+1)
#                 else:
#                     s += u//2
#             trees[i][j] = new
#             nuts[i][j] = nut + s
#
# def autumn_and_winter():
#     for r in range(n):
#         n1, a1 = nuts[r], a[r]
#         for c in range(n):
#             n1[c] += a1[c]
#             u = sum(1 for i in trees[r][c] if not i%5)
#             if u:
#                 for r1, c1 in adj(r,c):
#                     if 0 <= r1 < n and 0 <= c1 < n:
#                         trees[r1][c1] = [1]*u + trees[r1][c1]
#
# for _ in range(k):
#     spring_and_summer()
#     autumn_and_winter()
#
# print(sum(sum(len(i) for i in j) for j in trees))
