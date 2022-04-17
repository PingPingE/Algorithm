import sys
from collections import defaultdict, deque
T = int(input())
INF = sys.maxsize
while T:
    T-=1
    N, K = map(int, input().split())
    weight = [0] +  list(map(int, input().split()))
    D = defaultdict(int)
    G = defaultdict(list)
    for value in list( tuple(map(int, sys.stdin.readline().split()))for _ in range(K)):
        from_, to_ = value
        D[to_] += 1
        G[from_].append(to_)

    W = int(input())
    que = deque()

    def get_result(start):
        que = deque([start])
        done =set()
        result = 0

        # (현재값, 현재 노드) 이런식으로 넣어야하나?
        # 동시에 처리가능한거 고려(동시에 처리하는 것 중에서 가중치 젤 큰거만 반영)
        while que:
            cur = que.popleft()
            result += weight[cur]
            done.add(cur)
            if cur == W:
                break

            cur_weight = 0
            for i in G[cur]:
                cur_weight = max(cur_weight, weight[i])

            result+=cur_weight
            print("cur: ", cur, " result:", result, )
        return result

    ans = {}
    for n in range(1, N+1):
        if D[n] == 0:
            ans[n]= get_result(n)
    print(ans)








