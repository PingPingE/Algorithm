'''
문제)
N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

입력)
첫째 줄에 노드의 개수 N이 주어지고, 다음 N-1개 줄에는 트리 상에서 연결된 두 정점이 주어진다.
그 다음 줄에는 가장 가까운 공통 조상을 알고싶은 쌍의 개수 M이 주어지고, 다음 M개 줄에는 정점 쌍이 주어진다.

출력)
M개의 줄에 차례대로 입력받은 두 정점의 가장 가까운 공통 조상을 출력한다.
'''
#134076kb	1024ms
import sys
from collections import deque,defaultdict

N = int(input())
links = defaultdict(list)
for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    links[a].append(b)
    links[b].append(a)

levels= [0 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
que = deque([1])
done =set([1])
while que:
    prev = que.popleft()
    for n_node in links[prev]:
        if n_node not in done:
            parents[n_node] = prev
            levels[n_node] = levels[prev]+1
            que.append(n_node)
            done.add(n_node)


def get_LCA(a,b):
    while levels[a] != levels[b]:
        if levels[a] > levels[b]:
            a = parents[a]
        else:
            b = parents[b]

    while a != b:
        a=parents[a]
        b=parents[b]

    return a

M = int(input())
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    print(get_LCA(a,b))