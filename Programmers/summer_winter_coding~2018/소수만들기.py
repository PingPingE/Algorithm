'''

문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

'''

from itertools import combinations
def solution(nums):
    ans = 0
    # 0:소수 O / 1:소수 X
    primes = [0 for _ in range(3000)]

    primes[0] = 1
    primes[1] = 1

    for i in range(2, 3000):
        if primes[i]: continue
        for j in range(i * i, 3000, i):
            primes[j] = 1

    for comb in combinations(nums, 3):
        target = sum(comb)
        ans += not primes[target]

    return ans

'''
정확성  테스트
테스트 1 〉	통과 (1.60ms, 10.1MB)
테스트 2 〉	통과 (2.41ms, 10.1MB)
테스트 3 〉	통과 (0.82ms, 10.2MB)
테스트 4 〉	통과 (0.54ms, 10.1MB)
테스트 5 〉	통과 (2.60ms, 10.1MB)
테스트 6 〉	통과 (1.55ms, 10.1MB)
테스트 7 〉	통과 (0.46ms, 10MB)
테스트 8 〉	통과 (3.13ms, 10MB)
테스트 9 〉	통과 (0.65ms, 10.1MB)
테스트 10 〉	통과 (4.64ms, 10.2MB)
테스트 11 〉	통과 (0.48ms, 10.2MB)
테스트 12 〉	통과 (0.77ms, 10.2MB)
테스트 13 〉	통과 (0.78ms, 10.1MB)
테스트 14 〉	통과 (0.50ms, 10.1MB)
테스트 15 〉	통과 (0.45ms, 10.2MB)
테스트 16 〉	통과 (3.03ms, 10.2MB)
테스트 17 〉	통과 (3.37ms, 10.1MB)
테스트 18 〉	통과 (0.46ms, 10.1MB)
테스트 19 〉	통과 (0.67ms, 10.1MB)
테스트 20 〉	통과 (3.70ms, 10.1MB)
테스트 21 〉	통과 (3.47ms, 10.1MB)
테스트 22 〉	통과 (2.16ms, 10.1MB)
테스트 23 〉	통과 (0.43ms, 10MB)
테스트 24 〉	통과 (6.20ms, 10.1MB)
테스트 25 〉	통과 (2.91ms, 10MB)
테스트 26 〉	통과 (0.47ms, 10.1MB)
'''