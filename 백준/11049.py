'''
문제)
크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 입력으로 주어진 행렬의 순서를 바꾸면 안 된다.

입력)
첫째 줄에 행렬의 개수 N(1 ≤ N ≤ 500)이 주어진다.

둘째 줄부터 N개 줄에는 행렬의 크기 r과 c가 주어진다. (1 ≤ r, c ≤ 500)

항상 순서대로 곱셈을 할 수 있는 크기만 입력으로 주어진다.

출력)
첫째 줄에 입력으로 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값을 출력한다. 정답은 231-1 보다 작거나 같은 자연수이다. 또한, 최악의 순서로 연산해도 연산 횟수가 231-1보다 작거나 같다.
'''
#sol1: 127444kb	1032ms
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


#sol2: 129572kb	744ms
import sys
INF = sys.maxsize
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
memo= [[INF for j in range(N)] for i in range(N)]

for i in range(N-1):
    memo[i][i+1] = arr[i][0] * arr[i][1] * arr[i+1][1]

#재귀로 풀어보자
def solution(i,j):
    if i==j: return 0
    if memo[i][j]!=INF: return memo[i][j]
    for k in range(i,j):
        print(i,k,j)
        memo[i][j] = min(memo[i][j], solution(i,k)+solution(k+1,j)+arr[i][0]*arr[k][1]*arr[j][1])
    return memo[i][j]
solution(0,N-1)
print(memo[0][-1])