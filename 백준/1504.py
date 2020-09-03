'''
문제)
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력)
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다.
(v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력)
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''
#139800kb	460ms
import sys
from collections import defaultdict
import heapq
N,E = map(int, input().split())
dic = defaultdict(list) #key:정점, value: (연결된 정점, 비용)
for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    dic[a].append((b,c))
    dic[b].append((a,c))
v1,v2 = map(int, input().split())
target = {1:[], v1:[], v2:[]}
for start in target.keys(): #각각의 시작점에서 모든 정점까지의 최단거리 구하기
    heap = []
    costs = [sys.maxsize for _ in range(N+1)]
    heapq.heapify(heap)
    costs[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cost, ind  = heapq.heappop(heap)
        if costs[ind] < cost:
            continue
        for v,c in dic[ind]:
            tmp_cost = cost+c
            if costs[v] > tmp_cost:
                costs[v] = tmp_cost
                heapq.heappush(heap,(tmp_cost,v))
    target[start] = costs
res = min(target[1][v1]+target[v1][v2]+target[v2][N], target[1][v2]+target[v2][v1]+target[v1][N])
if res >= sys.maxsize: #가능한 경로가 없는 경우
    print(-1)
else:
    print(res)