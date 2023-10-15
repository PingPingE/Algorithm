from collections import deque, defaultdict

def solution(info, edges):
    answer = 0
    que = deque([[1, 0, 0, []]])  # 양 수 / 늑대 수 / 현재 노드 / visited (stack)
    links = defaultdict(list)
    r_links = defaultdict(list)
    for e in edges:
        links[e[0]].append(e[1])
        r_links[e[1]].append(e[0])

    N = len(info)
    dp = [0] * N  # 각 위치에 존재할 때 얻을 수 있는 가장 많은 양의 수
    dp[0] = 1

    # 역방향 체크
    def r_check(from_node, visited):
        if from_node not in visited and info[from_node] == 0:
            return True
        for node in r_links[from_node]:
            check(node, visited)
        return False

    def check(from_node, visited):
        if from_node not in visited and info[from_node] == 0:
            return True
        for node in links[from_node]:
            check(node, visited)
        return False

    while que:
        s_count, w_count, cur_node, visited = que.popleft()
        if s_count <= w_count:
            continue

        # 역방향 체크
        if visited and r_check(visited[-1], visited):
            que.append([s_count, w_count, cur_node, visited])

        visited.append(cur_node)
        answer = max(s_count, answer)
        for node in links[cur_node]:
            if node not in visited:
                if info[node] == 0:
                    que.append([s_count + 1, w_count, node, visited])
                else:
                    que.append([s_count, w_count + 1, node, visited])

            # 순방향 체크
            elif check(node, visited):
                que.append([s_count, w_count, node, visited])

    return answer