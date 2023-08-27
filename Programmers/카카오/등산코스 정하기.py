
'''
최적화한 다익스트라
- 가장 크게 최적화된 부분: gates, summits를 set로 바꾼거... ㄷㄷ 엄청나게 최적화됨
- 그 다음은 1,2,3 번 조건문
 
'''
from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    INF = 987654321
    answer = [INF, INF]
    graph = defaultdict(lambda: defaultdict(int))
    #list -> set
    gates = set(gates)
    summits = set(summits)

    min_intensity = [INF] * (n + 1)
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w

    def get_min_intensity(from_node): #기존에는 from_node, to_node를 gate, summit의 모든 조합을 구해서 넣어줬는데 from_node만 받는걸로 수정
        que = []
        heapq.heappush(que, (0, from_node))
        min_intensity[from_node] = 0
        while que:
            intensity, node = heapq.heappop(que)
            if node in summits: #1. 산봉우리는 한번만 찍음
                continue

            if min_intensity[node] < intensity: #2. 최솟값만 봄
                continue

            for n_node in graph[node].keys():
                if n_node in gates: #3. gate는 한 번만 
                    continue
                n_intensity = graph[node][n_node]
                max_intensity = max(intensity, n_intensity)
                if max_intensity < min_intensity[n_node]:
                    heapq.heappush(que, (max_intensity, n_node))
                    min_intensity[n_node] = max_intensity

    for gate in gates:
        get_min_intensity(gate)

    for summit in sorted(summits):
        if min_intensity[summit] < answer[1]:
            answer = [summit, min_intensity[summit]]

    return answer

'''
다익스트라
'''

import heapq
from collections import defaultdict
from itertools import product
def solution(n, paths, gates, summits):
    INF = 987654321
    answer = [INF, INF]
    graph = defaultdict(lambda: defaultdict(int))
    all_nodes = set(gates + summits)
    min_intensity = [INF] * (n + 1)
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w

    def get_min_intensity(from_node, to_node):
        min_intensity = [INF] * (n + 1)
        heap = []
        min_intensity[from_node] = 0
        heapq.heappush(heap, (0, from_node))

        forbidden_nodes = all_nodes - set([from_node, to_node])

        while heap:
            intensity, node = heapq.heappop(heap)
            for n_node in graph[node].keys():
                if n_node in forbidden_nodes:
                    continue
                n_intensity = graph[node][n_node]
                if max(intensity, n_intensity) < min_intensity[n_node]:
                    heapq.heappush(heap, (max(intensity, n_intensity), n_node))
                    min_intensity[n_node] = max(intensity, n_intensity)

        return min_intensity[to_node]

    # 최솟값이나오면 skip?
    for comb in sorted(product(gates, summits), key=lambda x: x[1]):
        gate, summit = comb
        candi_intensity = get_min_intensity(gate, summit)

        if candi_intensity < answer[1]:
            answer = [summit, candi_intensity]

    return answer


'''
파라메트릭서치 + 디익스트라?
주의: 경로에 다른 산봉우리, 게이트가 있으면 안됨

다익스트라는 출발 -> 목적까지의 총 비용이 아니라 max weight
파라메트릭서치는 나올 수 있는 모든 weight를 대상으로 (list의 Index로)
'''

from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    inf = 987654321
    weights = set()
    links = defaultdict(lambda: defaultdict(int))

    for path in paths:
        i, j, w = path
        links[i][j] = w
        links[j][i] = w
        weights.add(w)

    weights = sorted(weights)
    answer = [inf, inf]
    summits_set = set(summits)
    gates_set = set(gates)

    #게이트도, 산봉우리도 아닌 노드들
    nodes = set(range(1,n+1)) - summits_set - gates_set

    #다익스트라 + 탈출 조건
    def check(g, s, w):
        que = []
        costs = {node: inf for node in nodes}
        costs[g] = 0
        costs[s] = inf
        que.append((0, g))
        heapq.heapify(que)
        while que:
            max_w, cur_g = heapq.heappop(que)
            if max_w > w:
                continue
            for next_g in links[cur_g]:
                next_max_w = max(max_w, links[cur_g][next_g])
                if next_g in costs and costs[next_g] > next_max_w:
                    costs[next_g] = next_max_w
                    heapq.heappush(que, (next_max_w, next_g))

        return True if costs[s] <= w else False


    #파라메트릭 서치
    def get_intensity(g, s):
        return_m = 0
        l, r = 0, len(weights)-1
        while l <= r:
            m = (l + r) // 2
            if check(g, s, weights[m]):
                r = m - 1
                return_m = m
            else:
                l = m + 1
        return weights[return_m]

    for gate in gates: #출발지
        for summit in sorted(summits): #목적지
            intensity = get_intensity(gate, summit)
            if answer[1] > intensity:
                answer[0] = summit
                answer[1] = intensity

    return answer
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],	[5] ))

'''
다익스트라
'''

import heapq
from collections import defaultdict
from itertools import product
def solution(n, paths, gates, summits):
    INF = 987654321
    answer = [INF, INF]
    graph = defaultdict(lambda: defaultdict(int))
    all_nodes = set(gates + summits)
    min_intensity = [INF] * (n + 1)
    for i, j, w in paths:
        graph[i][j] = w
        graph[j][i] = w

    def get_min_intensity(from_node, to_node):
        min_intensity = [INF] * (n + 1)
        heap = []
        min_intensity[from_node] = 0
        heapq.heappush(heap, (0, from_node))

        forbidden_nodes = all_nodes - set([from_node, to_node])

        while heap:
            intensity, node = heapq.heappop(heap)
            for n_node in graph[node].keys():
                if n_node in forbidden_nodes:
                    continue
                n_intensity = graph[node][n_node]
                if max(intensity, n_intensity) < min_intensity[n_node]:
                    heapq.heappush(heap, (max(intensity, n_intensity), n_node))
                    min_intensity[n_node] = max(intensity, n_intensity)

        return min_intensity[to_node]

    # 최솟값이나오면 skip?
    for comb in sorted(product(gates, summits), key=lambda x: x[1]):
        gate, summit = comb
        candi_intensity = get_min_intensity(gate, summit)

        if candi_intensity < answer[1]:
            answer = [summit, candi_intensity]

    return answer

'''
파라메트릭서치 + 디익스트라?
주의: 경로에 다른 산봉우리, 게이트가 있으면 안됨

다익스트라는 출발 -> 목적까지의 총 비용이 아니라 max weight
파라메트릭서치는 나올 수 있는 모든 weight를 대상으로 (list의 Index로)
'''



from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    inf = 987654321
    weights = set()
    links = defaultdict(lambda: defaultdict(int))

    for path in paths:
        i, j, w = path
        links[i][j] = w
        links[j][i] = w
        weights.add(w)

    weights = sorted(weights)
    answer = [inf, inf]
    summits_set = set(summits)
    gates_set = set(gates)

    #게이트도, 산봉우리도 아닌 노드들
    nodes = set(range(1,n+1)) - summits_set - gates_set

    #다익스트라 + 탈출 조건
    def check(g, s, w):
        que = []
        costs = {node: inf for node in nodes}
        costs[g] = 0
        costs[s] = inf
        que.append((0, g))
        heapq.heapify(que)
        while que:
            max_w, cur_g = heapq.heappop(que)
            if max_w > w:
                continue
            for next_g in links[cur_g]:
                next_max_w = max(max_w, links[cur_g][next_g])
                if next_g in costs and costs[next_g] > next_max_w:
                    costs[next_g] = next_max_w
                    heapq.heappush(que, (next_max_w, next_g))

        return True if costs[s] <= w else False


    #파라메트릭 서치
    def get_intensity(g, s):
        return_m = 0
        l, r = 0, len(weights)-1
        while l <= r:
            m = (l + r) // 2
            if check(g, s, weights[m]):
                r = m - 1
                return_m = m
            else:
                l = m + 1
        return weights[return_m]

    for gate in gates: #출발지
        for summit in sorted(summits): #목적지
            intensity = get_intensity(gate, summit)
            if answer[1] > intensity:
                answer[0] = summit
                answer[1] = intensity

    return answer
print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],[1, 3],	[5] ))
