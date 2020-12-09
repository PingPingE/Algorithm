'''
문제 설명)
n개의 노드가 있는 그래프가 있습니다. 
각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 
가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 
1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

제한사항)
노드의 개수 n은 2 이상 20,000 이하입니다.
간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
'''

# T1: 6분 33초
# T2: 15분 33초(9분)
# T3: -
from collections import defaultdict, deque
import heapq
def solution(n, edge):
    INF = 987654321
    links = defaultdict(list)
    for a, b in edge:
        links[a].append(b)
        links[b].append(a)

    costs = [INF for _ in range(n + 1)]
    costs[0] = 0
    que = []
    heapq.heapify(que)
    heapq.heappush(que, (0, 1))  # 거리, 현 노드 번호
    costs[1] = 0
    while que:
        cost, num = heapq.heappop(que)
        for link in links[num]:
            if costs[link] > cost + 1:
                costs[link] = cost + 1
                que.append((costs[link], link))
    
    maxx = max(costs)
    return len(list(filter(lambda x: x == maxx, costs)))
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.39ms, 10MB)
테스트 5 〉	통과 (1.23ms, 10.4MB)
테스트 6 〉	통과 (3.19ms, 11MB)
테스트 7 〉	통과 (30.95ms, 17.7MB)
테스트 8 〉	통과 (36.44ms, 20.6MB)
테스트 9 〉	통과 (57.51ms, 21.2MB)
'''