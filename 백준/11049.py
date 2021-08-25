#127444kb	1032ms
import sys
INF = sys.maxsize
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
memo= [[INF for j in range(N)] for i in range(N)]

for i in range(N-1):
    memo[i][i] =0
    memo[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]
memo[-1][-1] = 0

#아 k를 가장 바깥에 두면 안됐음(이건 [i,j]구간 내에 계속 돌려야하니)
for diff in range(1,N):#ABCD가 있을 때 AB 먼저 보고 ABC 보고 그다음 ABCD 보고 (그 안에서 k로 쪼개서 최소 비용 계산하고) 
    for i in range(N-diff):
        j = i+diff
        for k in range(i,j):
            # print(i,k,j)
            memo[i][j] = min(memo[i][k] + memo[k+1][j] + (arr[i][0] * arr[k][1] * arr[j][1]),memo[i][j])
# print(memo)
print(memo[0][-1])