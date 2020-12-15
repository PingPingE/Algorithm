'''
문제 설명)
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.
다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, 
B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항)
섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
'''

#T1:9분 35초
#T2: 24분 55초 (15분20초)
#T3: -
links = {}
def find(x):
    global links
    if links[x] == x:
        return x
    links[x] = find(links[x])
    return links[x]

def union(a,b):
    global links
    a= find(a)
    b= find(b)
    if a<b: links[b] = a
    else: links[a] = b
        
from collections import deque
import heapq
def solution(n, costs):
    global links
    answer = 0
    links = {i:i for i in range(n)}
    que = []
    heapq.heapify(que)
    for a,b,cost in costs:
        heapq.heappush(que,(cost, a,b))
    cnt = 0
    while que:
        cost, from_, to_ = heapq.heappop(que)
        if find(from_) == find(to_): #사이클 X
            continue
        union(from_,to_)
        cnt +=1
        answer += cost
        if cnt == n-1: break #연결 다 했으면
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
'''