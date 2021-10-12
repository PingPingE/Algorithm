#참고:https://deok2kim.tistory.com/126

from itertools import chain
def solution(land, P, Q):
    flatten = sorted(chain.from_iterable(land))
    N = len(flatten)

    cost=0
    #초기화: 가장 낮은 높이로 다 맞추기
    for f in flatten[1:]:
        cost+=Q*(f-flatten[0])
    answer = cost

    #이제 차근 차근 다시 쌓아가는거임
    for e in range(1,N):
        #기존 높이와 현재 쌓아야할 높이의 차이
        diff = flatten[e]-flatten[e-1]

        #쌓아야할 높이보다 원래 높은 애들(e~N-1)은 기존 제거 비용을 다시 빼주고(무르기)
        #쌓아야할 높이보다 원래 낮은 애들(0~e-1)은 쌓는 비용을 더 내야하니 더하고
        cost = cost-(diff*Q*(N-e)) + (e*P*diff)
        answer = min(answer, cost)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.4MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (0.13ms, 10.3MB)
테스트 13 〉	통과 (0.30ms, 10.2MB)
테스트 14 〉	통과 (1.31ms, 10.3MB)
테스트 15 〉	통과 (2.35ms, 10.4MB)
테스트 16 〉	통과 (3.80ms, 10.5MB)
테스트 17 〉	통과 (4.60ms, 10.6MB)
테스트 18 〉	통과 (4.91ms, 10.6MB)
테스트 19 〉	통과 (5.81ms, 10.7MB)
테스트 20 〉	통과 (11.05ms, 10.7MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
테스트 22 〉	통과 (0.01ms, 10.3MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.09ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.06ms, 10.3MB)
테스트 30 〉	통과 (0.01ms, 10.3MB)
테스트 31 〉	통과 (0.02ms, 10.2MB)
테스트 32 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (59.82ms, 14.7MB)
테스트 2 〉	통과 (61.84ms, 15.3MB)
테스트 3 〉	통과 (54.39ms, 14.7MB)
테스트 4 〉	통과 (44.17ms, 14.7MB)
테스트 5 〉	통과 (40.60ms, 15.3MB)
테스트 6 〉	통과 (41.14ms, 12.1MB)
테스트 7 〉	통과 (46.90ms, 15.3MB)
테스트 8 〉	통과 (59.06ms, 14.9MB)
'''

#이미 있는 높이만 고려 + 2차원 -> 1차원으로 변형한 후 계산: 조오금 나아짐
from itertools import chain
def solution(land, P, Q):
    candi = set()
    for l in land:
        candi.update(l)
    flatten = list(chain.from_iterable(land))

    answer = -1

    def get_cost(N):
        cost = 0
        for m in map(lambda x: x - N, flatten):
            if m < 0:
                cost -= m * P
            else:
                cost += m * Q
        if answer > -1 and cost >= answer: return answer
        return cost

    for N in candi:  # 높이
        if answer == -1:
            answer = get_cost(N)
        else:
            answer = min(answer, get_cost(N))
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.2MB)
테스트 11 〉	통과 (1.02ms, 10.3MB)
테스트 12 〉	통과 (18.72ms, 10.3MB)
테스트 13 〉	통과 (50.97ms, 10.3MB)
테스트 14 〉	통과 (705.79ms, 10.4MB)
테스트 15 〉	통과 (2396.00ms, 10.4MB)
테스트 16 〉	통과 (5455.31ms, 10.9MB)
테스트 17 〉	통과 (8825.17ms, 11.1MB)
테스트 18 〉	통과 (8896.55ms, 11.1MB)
테스트 19 〉	실패 (시간 초과)
테스트 20 〉	실패 (시간 초과)
테스트 21 〉	통과 (0.02ms, 10.3MB)
테스트 22 〉	통과 (0.02ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (0.02ms, 10.2MB)
테스트 25 〉	통과 (0.04ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.2MB)
테스트 27 〉	통과 (0.10ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
테스트 29 〉	통과 (0.05ms, 10.3MB)
테스트 30 〉	통과 (0.02ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.3MB)
테스트 32 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (62.03ms, 11.7MB)
테스트 7 〉	통과 (64.14ms, 14.9MB)
테스트 8 〉	실패 (시간 초과)
'''


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
