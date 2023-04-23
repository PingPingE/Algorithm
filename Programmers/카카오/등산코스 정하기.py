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