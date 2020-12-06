import sys
from collections import defaultdict
# set -> list: set의 삽입 연산때문에 시간초과가 나는건가 싶어서 바꿈 -> 이제 런타임에러가 뜸(pypy3)
#필요없는 연산 없앰 (for v2 in v) -> 여전히 런타임에러 ;; -> dfs말고 bfs로 풀어보자
def find(x):
    global check
    check[x] = 1
    if x not in links:
        return
    for xx in links[x]:
        if check[xx]: continue
        find(xx)
    return

N,M = map(int, input().split())
links = defaultdict(list)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    links[b].append(a)#b를 해킹하면 a도 해킹할 수 있다.

max_target = [0,[]]
for k,v in links.items(): #v: k를 해킹했을 때 함께 해킹할 수 있는 컴퓨터들
    check = list(0 for _ in range(N+1))
    find(k)
    length = sum(check)
    print(check)
    if max_target[0] <length:
        max_target = [length, [k]]
    elif max_target[0] == length:
        max_target[1].append(k)

print(' '.join(map(str,sorted(max_target[1]))))