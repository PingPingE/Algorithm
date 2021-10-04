def solution(sticker):
    answer = 0
    N = len(sticker)
    if N <= 3:
        return max(sticker)

    # memo[idx]: sticker 리스트에서, idx-1번째 원소를 뜯었을 때 현재까지의 최댓값 저장
    memo1 = [0 for _ in range(N + 1)]  # 0번째 원소 뜯
    memo2 = [0 for _ in range(N + 1)]  # 안뜯

    # 0번째 원소 뜯 -> N-1까지만 봄(못뜯으니)
    memo1[1] = sticker[0]
    memo1[2] = 0  # 0번 원소를 뜯었으니 1번 원소는 못뜯음

    for i in range(3, N):
        memo1[i] = max(memo1[i - 2] + sticker[i - 1], memo1[i - 3] + sticker[i - 1])

    # 안뜯 -> N까지 봄
    memo2[1] = 0  # sticker[0]이 아닌 0으로 초기화(안뜯)
    memo2[2] = sticker[1]  # 0번 원소 안뜯었으니 1번 원소는 뜯기 가능

    for i in range(3, N + 1):
        memo2[i] = max(memo2[i - 2] + sticker[i - 1], memo2[i - 3] + sticker[i - 1])

    return max(max(memo1), max(memo2))


'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (1.08ms, 10.3MB)
테스트 8 〉	통과 (1.15ms, 10.2MB)
테스트 9 〉	통과 (1.47ms, 10.3MB)
테스트 10 〉	통과 (0.74ms, 10.3MB)
테스트 11 〉	통과 (0.74ms, 10.3MB)
테스트 12 〉	통과 (0.79ms, 10.3MB)
테스트 13 〉	통과 (1.16ms, 10.3MB)
테스트 14 〉	통과 (1.55ms, 10.2MB)
테스트 15 〉	통과 (1.28ms, 10.2MB)
테스트 16 〉	통과 (0.75ms, 10.2MB)
테스트 17 〉	통과 (1.50ms, 10.3MB)
테스트 18 〉	통과 (0.80ms, 10.2MB)
테스트 19 〉	통과 (0.74ms, 10.3MB)
테스트 20 〉	통과 (0.75ms, 10.3MB)
테스트 21 〉	통과 (0.78ms, 10.3MB)
테스트 22 〉	통과 (0.76ms, 10.3MB)
테스트 23 〉	통과 (0.76ms, 10.3MB)
테스트 24 〉	통과 (1.31ms, 10.4MB)
테스트 25 〉	통과 (0.79ms, 10.4MB)
테스트 26 〉	통과 (0.81ms, 10.3MB)
테스트 27 〉	통과 (0.75ms, 10.3MB)
테스트 28 〉	통과 (1.04ms, 10.3MB)
테스트 29 〉	통과 (0.79ms, 10.3MB)
테스트 30 〉	통과 (1.34ms, 10.3MB)
테스트 31 〉	통과 (0.76ms, 10.3MB)
테스트 32 〉	통과 (0.99ms, 10.3MB)
테스트 33 〉	통과 (0.00ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (86.28ms, 18.5MB)
테스트 2 〉	통과 (76.44ms, 18.5MB)
테스트 3 〉	통과 (85.76ms, 18.6MB)
테스트 4 〉	통과 (87.34ms, 18.6MB)
'''

'''
#삽질 기록
import sys
sys.setrecursionlimit(10**8)
def solution(sticker):
    answer = 0
    copy = sticker[:]
    N = len(sticker)

    def dfs(ans, sum_):
        nonlocal answer, copy
        if sum_ == 0:
            answer = max(ans, answer)
            return

        for i in range(N):
            if copy[i] != -1:
                right = i + 1 if i + 1 < N else 0
                left = i - 1
                flag = [0,0]

                copy[i] = -1
                if copy[left] != -1:
                    copy[left] = -1
                    flag[0] =1

                if copy[right] != -1:
                    copy[right] = -1
                    flag[1] = 1

                dfs(ans + sticker[i], sum_-(sticker[i]+flag[0]*sticker[left]+flag[1]*sticker[right]))

                copy[i] = sticker[i]
                if flag[0]:
                    copy[left] = sticker[left]
                if flag[1]:
                    copy[right] = sticker[right]

    dfs(0, sum(copy))
    return answer
'''
