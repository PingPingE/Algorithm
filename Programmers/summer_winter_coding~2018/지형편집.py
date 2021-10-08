#시도중(시간초과)

def solution(land, P, Q):
    min_N, max_N = min([min(i) for i in land]), max([max(i) for i in land])
    if max_N == 0:
        return 0

    answer = -1
    def get_cost(N):
        cost = 0
        for i in land:
            if answer > -1 and cost >= answer: return answer
            for j in i:
                if j < N:
                    cost += (N - j) * P
                else:
                    cost += (j - N) * Q
        return cost

    for N in range(min_N, max_N + 1):  # 높이
        if answer == -1:
            answer = get_cost(N)
        else:
            answer = min(answer, get_cost(N))
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.20ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (8.95ms, 10.2MB)
테스트 12 〉	통과 (144.34ms, 10.3MB)
테스트 13 〉	통과 (504.50ms, 10.2MB)
테스트 14 〉	통과 (3084.48ms, 10.3MB)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	통과 (0.03ms, 10.4MB)
테스트 22 〉	통과 (0.02ms, 10.4MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.07ms, 10.3MB)
테스트 26 〉	통과 (0.03ms, 10.2MB)
테스트 27 〉	통과 (0.11ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.03ms, 10.3MB)
테스트 30 〉	실패 (시간 초과)
테스트 31 〉	통과 (0.01ms, 10.2MB)
테스트 32 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''



def solution(land, P, Q):
    min_N, max_N = min([min(i) for i in land]), max([max(i) for i in land])
    answer = -1
    def get_cost(N):
        cost=0
        for i in land:
            if answer >-1 and cost >= answer: return answer
            # map으로
            for m in map(lambda x: x-N,i):
                if m<0:
                    cost-=m*P
                else:
                    cost+=m*Q
        return cost
    for N in range(min_N, max_N+1): #높이
        if answer == -1:
            answer = get_cost(N)
        else:
            answer = min(answer,get_cost(N))
    return answer

'''
정확성  테스트
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.30ms, 10.3MB)
테스트 3 〉	통과 (0.24ms, 10.3MB)
테스트 4 〉	통과 (0.15ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (14.74ms, 10.2MB)
테스트 12 〉	통과 (205.06ms, 10.2MB)
테스트 13 〉	통과 (826.23ms, 10.3MB)
테스트 14 〉	통과 (4520.92ms, 10.3MB)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
테스트 18 〉	실패 (시간 초과)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	통과 (0.03ms, 10.3MB)
테스트 22 〉	통과 (0.02ms, 10.2MB)
테스트 23 〉	통과 (0.02ms, 10.3MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.09ms, 10.3MB)
테스트 26 〉	통과 (0.04ms, 10.3MB)
테스트 27 〉	통과 (0.11ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.03ms, 10.3MB)
테스트 30 〉	실패 (시간 초과)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''