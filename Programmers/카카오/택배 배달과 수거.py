import math
def solution(cap, n, deliveries, pickups):
    answer = 0

    def remove_zero(st):
        try:
            while st[-1] == 0:
                st.pop()
            return st
        except:
            return []

    while deliveries or pickups:
        deliveries = remove_zero(deliveries)
        pickups = remove_zero(pickups)
        dist = max(len(deliveries), len(pickups))

        d_cap = cap
        p_cap = cap

        while deliveries:
            d = deliveries.pop()
            if d_cap >= d:
                d_cap -= d
            else:
                deliveries.append(d - d_cap)
                d_cap = 0
                break

        while pickups:
            p = pickups.pop()
            if p_cap >= p:
                p_cap -= p
            else:
                pickups.append(p - p_cap)
                p_cap = 0
                break

        answer += dist * 2

    return answer


print(solution(4,5,[1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))



'''
첫번째 시도: 젤 뒷쪽 집부터 배달, 수거 다 끝내버리기
'''
def solution1(cap, n, deliveries, pickups):
    answer = 0
    # 뒤에서부터 0을 만들어버림
    start = n - 1
    while start >= 0:
        d_cap = cap
        p_cap = cap
        prev_start = start

        for i in range(start, -1, -1):
            d, p = min(deliveries[i], d_cap), min(pickups[i], p_cap)
            if d == 0 and p == 0:
                prev_start = i - 1
                continue

            d_cap -= d
            p_cap -= p
            deliveries[i] -= d
            pickups[i] -= p

            if deliveries[i] == 0 and pickups[i] == 0:
                start = i - 1

            if d_cap == 0 and p_cap == 0:
                break
        answer += (prev_start + 1) * 2

    return answer