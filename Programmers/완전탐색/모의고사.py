'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
'''

def solution(answers):
    ans = [ [1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]#반복구간만
    scores =[0,0,0]#각자(index)의 정답 개수
    
    for idx in range(len(answers)):
        target = answers[idx]
        for i in range(3): #세 사람
            if ans[i][idx%len(ans[i])] ==target:
                scores[i] += 1
                
    maxx = max(scores)
    return list(filter(lambda x: scores[x-1]==maxx, range(1,4)))


'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.06ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (3.58ms, 10.3MB)
테스트 8 〉	통과 (1.32ms, 10.3MB)
테스트 9 〉	통과 (6.10ms, 10.3MB)
테스트 10 〉	통과 (3.08ms, 10.2MB)
테스트 11 〉	통과 (6.31ms, 10.3MB)
테스트 12 〉	통과 (5.97ms, 10.3MB)
테스트 13 〉	통과 (0.60ms, 10.3MB)
테스트 14 〉	통과 (6.77ms, 10.2MB)
'''