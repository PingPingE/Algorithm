import sys
from collections import defaultdict
#재시도1: set -> list: set의 삽입 연산때문에 시간초과가 나는건가 싶어서 바꿈 -> 이제 런타임에러가 뜸(pypy3)
#재시도2: 필요없는 연산 없앰 (for v2 in v) -> 여전히 런타임에러 ;; -> dfs말고 bfs로 풀어보자
#재시도3: bfs로 바꿈 -> 229568kb	15760ms
N,M = map(int, input().split())
links = defaultdict(list)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    links[b].append(a)#b를 해킹하면 a도 해킹할 수 있다.

max_target = [0,[]]
for k,v in links.items(): #v: k를 해킹했을 때 함께 해킹할 수 있는 컴퓨터들
    check = list(0 for _ in range(N+1))
    que = v[:]
    check[k] =1
    while que:
        q = que.pop()
        if check[q]:
            continue
        check[q] = 1
        if q in links:
            for q_v in links[q]:
                if check[q_v]: continue
                que.append(q_v)
    length = sum(check)
    if max_target[0] <length:
        max_target = [length, [k]]
    elif max_target[0] == length:
        max_target[1].append(k)

print(' '.join(map(str,sorted(max_target[1]))))