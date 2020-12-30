#T1,T2: 14분3초
#T3: 17분 19초(3분 16초)
import sys
from collections import defaultdict,deque
N,M,V = map(int, input().split())
links = defaultdict(set)
for _ in range(M):
    a,b = map(int ,sys.stdin.readline().split())
    links[a].add(b)
    links[b].add(a)

def dfs():
    stack = []
    stack.append(V)
    done = []
    while stack:
        st = stack.pop()
        if st in done: continue #모든 노드가 done에 들어간다는 보장이 없음 그래서 이 조건문 필요
        done.append(st)
        if len(done) == N: break
        for v in sorted(links[st], reverse=True):
            if v not in done:
                stack.append(v)
    return ' '.join(map(str, done))

def bfs():
    que = deque()
    que.append(V)
    done = [V]
    while que:
        q = que.popleft()
        if len(done) == N: break
        for v in sorted(links[q]):
            if v not in done:
                done.append(v)
                que.append(v)
            if len(done) == N: break
    return ' '.join(map(str,done))

print(dfs())
print(bfs())