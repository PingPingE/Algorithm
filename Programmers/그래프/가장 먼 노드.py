'''
문제 설명
n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
입출력 예
n	vertex								return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
'''
#sol) dijkstra 알고리즘 기반으로 해결
from collections import defaultdict,Counter
import heapq
def solution(n, edge):
    graph= defaultdict(set)
    for i,j in edge:
        graph[i].add(j)
        graph[j].add(i)
    cost = [n for _ in range(n+1)]
    que = [[0,1]]
    heapq.heapify(que)
    cost[1] = 0
    while que:
        cur_cost, node = heapq.heappop(que)
        for g in graph[node]:
            if cost[g] > cur_cost+1:
                cost[g] = cur_cost+1
                heapq.heappush(que, [cost[g], g])
    maxx = max(cost[1:])
    return Counter(cost[1:])[maxx]

'''
정확성  테스트
테스트 1 〉	통과 (0.10ms, 10.8MB)
테스트 2 〉	통과 (0.10ms, 10.7MB)
테스트 3 〉	통과 (0.11ms, 10.8MB)
테스트 4 〉	통과 (0.45ms, 10.9MB)
테스트 5 〉	통과 (1.58ms, 12MB)
테스트 6 〉	통과 (3.96ms, 19.3MB)
테스트 7 〉	통과 (49.36ms, 89MB)
테스트 8 〉	통과 (75.37ms, 125MB)
테스트 9 〉	통과 (74.16ms, 125MB)
'''