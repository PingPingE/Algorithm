'''
문제 설명)
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항)
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''

#T1(문제 이해 ~ 코딩 시작): 5분 12초
#T2(코딩 시작 ~ 제출): 15분 19초(10분 7초)
#T3(디버깅): 15분 19초(0초)
from collections import deque
def solution(numbers, target):
    count = 0
    que = deque([i] for i in range(len(numbers)))

    if sum(numbers) == target:
        count += 1

    while que:
        targets = que.popleft()
        tmp = sum(list( - numbers[i] if i in targets else numbers[i] for i in range(len(numbers)) ))
        if tmp == target:
            count +=1
        for i in range(targets[-1]+1, len(numbers)):
            que.append(targets+[i])
    
    return count

'''
정확성  테스트
테스트 1 〉	통과 (4680.39ms, 43.2MB)
테스트 2 〉	통과 (4631.66ms, 43.5MB)
테스트 3 〉	통과 (2.78ms, 10.2MB)
테스트 4 〉	통과 (11.54ms, 10.3MB)
테스트 5 〉	통과 (106.38ms, 11.2MB)
테스트 6 〉	통과 (5.57ms, 10.2MB)
테스트 7 〉	통과 (3.06ms, 10.2MB)
테스트 8 〉	통과 (24.18ms, 10.4MB)
'''