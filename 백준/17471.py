from itertools import combinations
def dfs(B):
    global m
    #출발지점
    stack = []
    stack.append([list(B)[0], set()])
    done = set()
    while stack:
        s, foot = stack.pop()
        done.add(s)
        foot.add(s)
        if len(done) == len(B):
            return True
        for v in m[s]:
            if v in B and v not in foot:
                stack.append([v, foot])

    return False

def check(arr):
    global N,m
    arr2 = set(range(1,N+1))
    #선거구2
    arr2 -= arr
    if len(arr) > 1 :
        if dfs(arr) is False:
            return False

    if len(arr2) > 1 :
        if dfs(arr2) is False:
            return False
    return True

def population(A):
    global N,pnum,res
    p1 = 0
    p2 = 0
    for n in range(1,N+1):
        if n in A:
            p1+= pnum[n]
        else:
            p2+= pnum[n]
    res = min(res, abs(p1-p2))

N= int(input())
#인덱스: 구역 번호(1~N), 각값: 인구수
pnum = [0]
pnum.extend(list(map(int, input().split())))
m = {}
res = 10000
#키: 구역번호(1~N), 값: 인접구역 번호
for _ in range(1,N+1):
    m[_] = list(map(int,input().split()))
    m[_].pop(0)

for i in range(1,(N//2)+1):
    #선거구1 조합
    for s in set(combinations(list(range(1,N+1)), i)):
        if check(set(s)) is True:
            population(s)
    if res == 0:
        break

if res == 10000:
    print(-1)
else:
    print(res)
