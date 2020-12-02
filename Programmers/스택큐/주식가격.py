'''
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    cur_time = -1
    stack = []#(가격, 들어온 시간)
    for i in range(len(prices)):
        cur_time += 1
        while stack:
            price, time = stack[-1]
            if price > prices[i]: #가격이 떨어졌으면
                answer[time] = cur_time - time
                stack.pop()
            else:
                break
        stack.append((prices[i],cur_time))
    
    while stack:
        price, time = stack.pop()
        answer[time] = cur_time-time
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.44ms, 10.3MB)
테스트 4 〉	통과 (0.55ms, 10.3MB)
테스트 5 〉	통과 (0.58ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.30ms, 10.2MB)
테스트 8 〉	통과 (0.35ms, 10.3MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.59ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (31.90ms, 18.7MB)
테스트 2 〉	통과 (23.74ms, 17.6MB)
테스트 3 〉	통과 (35.76ms, 19.5MB)
테스트 4 〉	통과 (25.34ms, 18.2MB)
테스트 5 〉	통과 (19.65ms, 17.1MB)
'''
