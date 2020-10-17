from itertools import combinations
#122808kb	1112ms
def countBit(x):
    cnt = 0
    while x:
        if x&1:
            cnt+=1
        x >>= 1
    return cnt
ret = 987654321
N = int(input())
S = list(list(map(int, input().split())) for _ in range(N))
for n in range(1<<N):
    if countBit(n) == N//2:
        team1 = set()
        team2 = set()
        for i in range(N):
            if n&1<<i:
                team1.add(i)
            else:
                team2.add(i)
        t1 ,t2=0,0
        for c in combinations(team1,2):
            t1 += S[c[0]][c[1]]
            t1 += S[c[1]][c[0]]
        for c in combinations(team2,2):
            t2 += S[c[0]][c[1]]
            t2 += S[c[1]][c[0]]
        ret =min(ret,abs(t1-t2))
        if ret == 0: break
print(ret)

#sol2---------------------------------------
#122616kb	976ms
from itertools import combinations
N = int(input())
ret= 987654321
S = list(list(map(int, input().split())) for _ in range(N))
for c in combinations(list(range(N)), N//2):
    team1 = c
    team2 = []
    for i in range(N):
        if i not in team1:
            team2.append(i)
    t1, t2 = 0, 0
    for c in combinations(team1, 2):
        t1 += S[c[0]][c[1]]
        t1 += S[c[1]][c[0]]
    for c in combinations(team2, 2):
        t2 += S[c[0]][c[1]]
        t2 += S[c[1]][c[0]]
    ret = min(ret, abs(t1 - t2))
    if ret == 0: break
print(ret)