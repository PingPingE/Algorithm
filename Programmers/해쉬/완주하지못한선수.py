'''
문제 설명)
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항)
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

from collections import Counter
def solution(participant, completion):
    counter = Counter(participant)
    for target in completion:
        counter[target] -= 1
    return list(filter(lambda x: counter[x] >0, counter))[0]


'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.39ms, 10.4MB)
테스트 4 〉	통과 (0.75ms, 10.5MB)
테스트 5 〉	통과 (0.73ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (27.78ms, 21.8MB)
테스트 2 〉	통과 (47.80ms, 25.3MB)
테스트 3 〉	통과 (63.15ms, 27.6MB)
테스트 4 〉	통과 (63.15ms, 34MB)
테스트 5 〉	통과 (58.73ms, 34MB)
'''
#좀 더 짧은 코드-> 하지만 효율성은 조금 떨어짐
from collections import Counter
def solution(participant, completion):
    counter = Counter(participant)-Counter(completion) #Counter객체끼리 연산 가능
    return list(counter)[0]

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.37ms, 10.3MB)
테스트 4 〉	통과 (0.65ms, 10.4MB)
테스트 5 〉	통과 (0.73ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (33.56ms, 24.4MB)
테스트 2 〉	통과 (57.02ms, 27.8MB)
테스트 3 〉	통과 (75.36ms, 30.2MB)
테스트 4 〉	통과 (93.01ms, 39.1MB)
테스트 5 〉	통과 (91.49ms, 39.1MB)
'''