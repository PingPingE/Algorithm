'''
문제)
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프들이 있습니다.
이 그래프들은 1개 이상의 정점과, 정점들을 연결하는 단방향 간선으로 이루어져 있습니다
그래프의 간선 정보를 담은 2차원 정수 배열 edges가 매개변수로 주어집니다.
이때, 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수를
순서대로 1차원 정수 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항)
1 ≤ edges의 길이 ≤ 1,000,000
edges의 원소는 [a,b] 형태이며, a번 정점에서 b번 정점으로 향하는 간선이 있다는 것을 나타냅니다.
1 ≤ a, b ≤ 1,000,000
문제의 조건에 맞는 그래프가 주어집니다.
도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프의 수의 합은 2이상입니다.
'''
from collections import defaultdict, deque


def solution(edges):
    answer = [0, 0, 0, 0]
    g_dict = defaultdict(list)  # key: from / value: to_list
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for edge in edges:
        from_, to_ = edge
        g_dict[from_].append(to_)
        in_degree[to_] += 1
        out_degree[from_] += 1

    # 임의 노드 찾기: indegree ==0인 노드 중 outdegree가 가장 큰 노드
    for node in sorted(out_degree.items(), key=lambda x: x[1], reverse=True):
        if in_degree[node[0]] == 0:
            answer[0] = node[0]
            break

    def check_shape(start_node):
        '''
        시작점 노드에 연결 되어있는 모든 노드를 따라가며 모양 찾기
        '''
        shape = 0
        que = deque()
        # edge 카운트, node 카운트
        e_count, n_count = 0, 0
        done = set([start_node])

        if g_dict[start_node]:
            next_node = g_dict[start_node].pop()
            que.append(next_node)
        # 사이클 유무
        is_cycle = False
        while que:
            cur_node = que.popleft()
            e_count += 1

            if cur_node in done:
                is_cycle = True

            done.add(cur_node)

            while g_dict[cur_node]:
                next_node = g_dict[cur_node].pop()
                que.append(next_node)

        n_count = len(done)
        if e_count == n_count and is_cycle:
            '''
            edge 개수 == 노드 개수 & 사이클 유
            '''
            shape = 1
        elif e_count + 1 == n_count and not is_cycle:
            '''
           edge 개수 +1  == 노드 개수 & 사이클 무
           '''
        shape = 2
        else:
        shape = 3

    return shape  # 1:도넛 /2:막대 /3: 8자


# 임의 노드가 가리키는 노드를 출발점으로 해서 각각의 그래프 모양 찾기
for start_node in g_dict[answer[0]]:
    ans_idx = check_shape(start_node)
    answer[ans_idx] += 1

return answer
