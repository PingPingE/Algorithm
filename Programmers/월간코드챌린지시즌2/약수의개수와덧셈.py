'''
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서,
약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000

입출력 예
left	right	result
13	17	43
24	27	52
'''
def solution(left, right):
    ans = 0
    for n in range(left, right + 1):
        ans += -n if div_cnt(n) % 2 else n
    return ans


def div_cnt(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt

'''
정확성  테스트
테스트 1 〉	통과 (20.59ms, 10.2MB)
테스트 2 〉	통과 (4.50ms, 10.2MB)
테스트 3 〉	통과 (4.34ms, 10.2MB)
테스트 4 〉	통과 (2.30ms, 10.1MB)
테스트 5 〉	통과 (20.14ms, 10.2MB)
테스트 6 〉	통과 (1.55ms, 10.2MB)
테스트 7 〉	통과 (0.74ms, 10.2MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''