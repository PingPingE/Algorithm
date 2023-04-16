'''
0. 가장 높은 알고력, 코딩력 구하기 -> goal 설정
1. 1의 시간당 1의 능력 높이거나 / 현재 풀 수 있는 문제를 풀어서 능력을 높인다
2. 각 능력에 도달하기까지의 최소 시간을 갱신한다
3. 1~2를 반복
4. goal 능력치에 도달하기 까지의 최소 시간 return
'''


# 최종 통과 코드
def solution(alp, cop, problems):
    goal_alp, goal_cop = 0, 0
    N = len(problems)
    exception = []

    for e, problem in enumerate(problems):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        goal_alp = max(alp, max(goal_alp, alp_req))
        goal_cop = max(cop, max(goal_cop, cop_req))

        #그냥 안푸는게 더 이득인 케이스(단위 시간당 얻는 능력치가 1도 안되는 경우)
        if alp_rwd / cost + cop_rwd / cost <= 1:
            exception.append(e)

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    # 각 능력치를 가지기까지의 걸린 최소 시간
    done = {(alp, cop): 0}

    for cur_alp in range(alp, goal_alp + 1):
        for cur_cop in range(cop, goal_cop + 1):

            if (cur_alp, cur_cop) not in done:
                done[(cur_alp, cur_cop)] = goal_alp + goal_cop
            cur_time = done[(cur_alp, cur_cop)]

            for e, problem in enumerate(problems):
                if e in exception: continue

                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if alp_req <= cur_alp and cop_req <= cur_cop:
                    new_time = cur_time + cost
                    new_alp = min(cur_alp + alp_rwd, goal_alp)
                    new_cop = min(cur_cop + cop_rwd, goal_cop)

                    if (new_alp, new_cop) not in done or done[(new_alp, new_cop)] > new_time:
                        done[(new_alp, new_cop)] = new_time

    return done[(goal_alp, goal_cop)]

#========================================================================================================
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

# print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))



'''
Q3 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 1, 1, 1],
        [150, 150, 1, 1, 100],
    ],
}

# 빠른길이 도착지에서 끝나지 않는 경우
Q4 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [4, 3, 1, 1, 100],
        [0, 0, 2, 2, 1],
    ],
}

# 한쪽 조건이 완료된 경우 1
Q5 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [0, 2, 1, 1, 100],
    ],
}

# 한쪽 조건이 완료된 경우 2
Q6 = {
    "alp": 1,
    "cop": 1,
    "problems": [
        [2, 0, 1, 1, 100],
    ],
}

# 모든 조건이 완료된 경우
Q7 = {
    "alp": 2,
    "cop": 2,
    "problems": [
        [1, 1, 1, 1, 100],
    ],
}

# Q4 + Q6
Q8 = {
    "alp": 10,
    "cop": 10,
    "problems": [
        [0, 0, 5, 5, 1],
        [30, 10, 1, 1, 100],
    ],
}

# 탐색범위가 굉장히 커질 수 있는 요지를 해결했는가
Q9 = {
    "alp": 0,
    "cop": 0,
    "problems": [
        [0, 0, 30, 2, 1],
        [150, 150, 30, 30, 100],
    ],
}

'''
