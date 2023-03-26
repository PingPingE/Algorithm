'''
0. 가장 높은 알고력, 코딩력 구하기

-- 여기서 bfs를 해야하나?
1. 1의 시간당 1의 능력 높이거나 / 현재 풀 수 있는 문제를 풀어서 능력을 높인다
2. 현재 능력이 0에 부합하는지 체크 만약 부합하면 return 아님 다시 1로 ㄱㄱ
'''

#정확도 테스트는 통과했는데 효율성 테스트 불통과한 코드
from collections import deque
def solution(alp, cop, problems):
    goal_alp, goal_cop = 0, 0
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        goal_alp = max(goal_alp, alp_req)
        goal_cop = max(goal_cop, cop_req)

    answer = goal_alp + goal_cop

    def get_available_problems(alp, cop):
        ret = []
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
            if alp_req <= alp and cop_req <= cop:
                ret.append((alp_rwd, cop_rwd, cost))
        return ret

    que = deque([[alp, cop, 0]])
    while que:
        a_score, c_score, time = que.popleft()
        if a_score >= goal_alp and c_score >= goal_cop:
            answer = min(answer, time)
            continue

        if time >=answer:
            continue

        available_problems = get_available_problems(a_score, c_score)
        que.append([a_score + 1, c_score, time + 1])
        que.append([a_score, c_score + 1, time + 1])
        for problem in available_problems:
            alp_rwd, cop_rwd, cost = problem
            que.append([a_score + alp_rwd, c_score + cop_rwd, time + cost])

    return answer

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))