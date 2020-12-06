#pypy3: 메모리초과, python3:시간초과

import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)
def find(x,targets): #함께 해킹 가능한 컴퓨터들 set에 담기
    targets.add(x)
    if x not in links:
        return
    for xx in links[x]:
        if xx in targets: continue
        find(xx, targets)
    return targets

N,M = map(int, input().split())
links = defaultdict(list)
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    links[b].append(a)#b를 해킹하면 a도 해킹할 수 있다.

max_target = [0,[]]
for k,v in links.items(): #v: k를 해킹했을 때 함께 해킹할 수 있는 컴퓨터들
    child = set()
    child.update(v)
    for v2 in v: #v를 해킹했을 때 함께 해킹할 수 있는 컴퓨터들
        if v2 in links:
            tmp=find(v2,set())
            child.update(tmp)
    child |= {k}
    length = len(child)
    if max_target[0] <length:
        max_target = [length, [k]]
    elif max_target[0] == length:
        max_target[1].append(k)

print(' '.join(map(str,sorted(max_target[1]))))