'''
문제 설명)
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항)
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
'''

# T1: 5분 20초
# T2: 18분 1초(12분 41초)
# T3: 39분 18초(21분 17초) + a
import heapq
def solution(N, number):
    inf = 987654321
    answer = 0
    candi = [int(str(N) * i) for i in range(1,6)]  # 최대 5자리
    que = []
    heapq.heapify(que)
    memo ={} #value: key값을 만드는데 사용한 N의 최소 갯수
    for e, n in enumerate(candi, 1):
        if n == number: return e
        heapq.heappush(que, (e,n))
        memo[n] = e
        heapq.heappush(que, (e,-n)) #첨에 -로 시작할 수 있으므로
        memo[-n] = e
    memo[number] = inf
    while que:
        cnt, cur = heapq.heappop(que)
        if cnt>=memo[number]: continue
        if cnt > 8: continue
        for e, c in enumerate(candi, 1):
            tmp = [cur + c, cur - c, cur * c, cur // c]
            for t in tmp:
                memo[t] = memo.get(t,inf)
                if t == number:
                    memo[number] = min(memo[number], cnt+e)
                    continue
                if memo[t] > cnt + e:
                    heapq.heappush(que, (cnt + e, t)) 
                    memo[t] = cnt + e
    return -1 if memo[number]>8 else memo[number]


'''
정확성  테스트
테스트 1 〉	통과 (5.36ms, 10.9MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.22ms, 10.5MB)
테스트 4 〉	통과 (141.80ms, 20.3MB)
테스트 5 〉	통과 (32.86ms, 12.4MB)
테스트 6 〉	통과 (1.78ms, 10.5MB)
테스트 7 〉	통과 (2.03ms, 10.6MB)
테스트 8 〉	통과 (47.99ms, 14.3MB)
테스트 9 〉	통과 (0.21ms, 10.4MB)
'''