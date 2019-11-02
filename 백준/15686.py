from itertools import combinations
import sys
import copy
def sol(s):
    global chicken, home, res
    tmp = copy.copy(chicken)
    tmp -= set(s)
    total = 0
    for y1,x1 in home:
        dist=sys.maxsize
        for y2,x2 in tmp:
            dist=min(dist, abs(y1-y2)+abs(x1-x2))
        total += dist
    res = min(res, total)

N,M = map(int,input().split())
chicken = set()
home = set()
res = sys.maxsize
for _ in range(N):
    li = list(map(int, sys.stdin.readline().split()))
    for l in range(len(li)):
        if li[l] == 2:
            chicken.add((_,l))
        elif li[l] == 1:
            home.add((_,l))
# 없애야할 치킨집 개수
goal= len(chicken) - M
#없앨 가게 조합
for s in set(combinations(chicken, goal)):
    sol(s)
print(res)