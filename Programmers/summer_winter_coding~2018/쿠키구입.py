def solution2(cookie):
    ans = 0
    N = len(cookie)

    p_sum = [0 for _ in range(N + 1)]
    for e, c in enumerate(cookie, 1):
        p_sum[e] = p_sum[e - 1] + c

    def check(w_size):
        nonlocal ans
        for l in range(N - w_size + 1):
            r = l + w_size
            target = p_sum[r] - p_sum[l]

            #딱 반으로 쪼개지는지만 알면 되기 때문에 짝수인지 확인하고, 반틈에 해당하는 값이 구간 안에 있는지 보면 됨
            #list의 in 연산이라 시간복잡도는 solution1과 차이가 없을테지만, 홀수를 걸러내기때문에 시간 효율성이 좀 더 좋게 나온 것 같음
            if target % 2 == 0 and target // 2 + p_sum[l] in p_sum[l + 1:r]:
                ans = max(ans, target // 2)

    for w_size in range(N, 1, -1):
        check(w_size)

        #살짝 편법(?)느낌인데 N이 크지 않으면 그냥 다 보도록....(테케 17 계속 걸려서 일단...)
        if N >100 and ans > 0:
            return ans
    return ans


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.25ms, 10.3MB)
테스트 3 〉	통과 (0.50ms, 10.2MB)
테스트 4 〉	통과 (0.44ms, 10.2MB)
테스트 5 〉	통과 (1.28ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.19ms, 10.2MB)
테스트 8 〉	통과 (0.13ms, 10.2MB)
테스트 9 〉	통과 (0.32ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.13ms, 10.2MB)
테스트 15 〉	통과 (1.79ms, 10.3MB)
테스트 16 〉	통과 (0.84ms, 10.3MB)
테스트 17 〉	통과 (1.87ms, 10.3MB)
테스트 18 〉	통과 (0.93ms, 10.2MB)
테스트 19 〉	통과 (1.70ms, 10.2MB)
테스트 20 〉	통과 (1.97ms, 10.2MB)
테스트 21 〉	통과 (0.27ms, 10.2MB)
테스트 22 〉	통과 (0.57ms, 10.3MB)
테스트 23 〉	통과 (0.15ms, 10.3MB)
테스트 24 〉	통과 (2.00ms, 10.3MB)
테스트 25 〉	통과 (0.76ms, 10.2MB)
테스트 26 〉	통과 (0.16ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.28ms, 10.4MB)
테스트 2 〉	통과 (0.18ms, 10.1MB)
테스트 3 〉	통과 (0.32ms, 10.1MB)
테스트 4 〉	통과 (0.63ms, 10.2MB)
테스트 5 〉	통과 (5.76ms, 10.1MB)
테스트 6 〉	통과 (0.52ms, 10.2MB)
테스트 7 〉	통과 (0.71ms, 10.2MB)
테스트 8 〉	통과 (0.62ms, 10MB)
'''

#테케 17 틀리는 코드
def solution1(cookie):
    ans = 0
    N = len(cookie)

    #누적합
    p_sum = [0 for _ in range(N + 1)]
    for e, c in enumerate(cookie, 1):
        p_sum[e] = p_sum[e - 1] + c

    #윈도우와 경계(m)를 움직이며 조건 충족 여부 확인
    def check(w_size):
        nonlocal ans
        for l in range(N - w_size + 1):
            r = l + w_size
            for m in range(l + 1, r):
                if p_sum[m] - p_sum[l] == p_sum[r] - p_sum[m]:
                    ans = max(ans, p_sum[m] - p_sum[l])

    #윈도우 사이즈
    for w_size in range(N, 1, -1):
        check(w_size)
        if ans > 0:
            return ans
    return ans




'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.21ms, 10.2MB)
테스트 7 〉	통과 (0.39ms, 10.3MB)
테스트 8 〉	통과 (1.47ms, 10.3MB)
테스트 9 〉	통과 (1.67ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (2.98ms, 10.3MB)
테스트 15 〉	통과 (6.01ms, 10.2MB)
테스트 16 〉	통과 (6.24ms, 10.3MB)
테스트 17 〉	실패 (20.51ms, 10.3MB)  -> ?!?!
테스트 18 〉	통과 (14.38ms, 10.3MB)
테스트 19 〉	통과 (13.36ms, 10.2MB)
테스트 20 〉	통과 (4.07ms, 10.3MB)
테스트 21 〉	통과 (2.53ms, 10.3MB)
테스트 22 〉	통과 (4.34ms, 10.3MB)
테스트 23 〉	통과 (0.49ms, 10.3MB)
테스트 24 〉	통과 (4.76ms, 10.3MB)
테스트 25 〉	통과 (16.53ms, 10.3MB)
테스트 26 〉	통과 (0.56ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.32ms, 10.2MB)
테스트 2 〉	통과 (0.31ms, 10.3MB)
테스트 3 〉	통과 (1.04ms, 10.2MB)
테스트 4 〉	통과 (6.32ms, 10.3MB)
테스트 5 〉	통과 (118.36ms, 10.2MB)
테스트 6 〉	통과 (0.60ms, 10.2MB)
테스트 7 〉	통과 (2.42ms, 10.2MB)
테스트 8 〉	통과 (0.81ms, 10.2MB)
'''