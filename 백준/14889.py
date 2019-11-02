from itertools import combinations
from itertools import permutations
from collections import deque
#두팀의 능력치 차이가 최소가 되도록 -> 0이면 STOP
N = int(input())
S = [list(map(int,input().split())) for _ in range(N)]
res = -1
que = deque()
#0~N-1번의 사람들 조합 (N//2개씩)
que.extend(list(combinations(list(range(N)), N//2)))
while que:
    q = que.popleft()
    point1 = 0
    point2 = 0
    for i,j in list(permutations(q,2)):
        point1 += S[i][j]
    q2 = set([i for i in range(N)])-set(q)
    for i,j in list(permutations(q2,2)):
        point2 += S[i][j]
    tmp = abs(point1 - point2)
    if res == -1 or tmp<res:
        res = tmp
    if res == 0:
        break
print(res)


