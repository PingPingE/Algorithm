#시간 초과 ㅠ
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 8)

def solution(sales, links):
    teams = defaultdict(set)
    link = {}
    link[1] = 0  # value: 상위 노드
    for p, c in links:
        teams[p].add(c)
        link[c] = p

    def get_degree(x, cnt):
        if x == 1:
            return cnt
        return get_degree(link[x], cnt + 1)

    degree = {}
    for k in teams:
        degree[k] = get_degree(k, 0)

    answer = 987654321
    leaders = set(teams.keys())

    print(degree)

    def dfs(teams, done, ans):
        nonlocal answer
        print(done, ans)
        if len(done) == len(teams):
            answer = min(answer, ans)
            return

        for k, v in sorted(teams.items(), key=lambda x: degree[x[0]]):
            if k in done:
                continue
            print("leader:", k)
            # 팀장 중 최소
            tmp_set = (leaders & v)
            if tmp_set:
                t_x = min(tmp_set, key=lambda x: sales[x - 1])
                dfs(teams, done | {k, t_x}, ans + sales[t_x - 1])

            # 팀원 중 최소
            tmp_set2 = v - leaders
            if tmp_set2:
                m_x = min(tmp_set2 | {k}, key=lambda x: sales[x - 1])
                dfs(teams, done | {k}, ans + sales[m_x - 1])

    dfs(teams, set(), 0)
    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17]	,[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
