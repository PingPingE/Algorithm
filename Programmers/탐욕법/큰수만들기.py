'''
문제 설명)
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건)
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
'''

#T1: 6분 23초
#T2: 24분 28초(18분 5초)
#T3: 45분 37초 (21분 9초)
def solution(number, k):
    answer = []
    s = 0
    stat= True
    while k and stat:
        maxx = ['-1', 0]
        for i in range(s, s + k + 1):#인덱스 s부터 k+1개의 원소 보기
            if i>=len(number): #그냥 다 지워야하는 경우
                stat=False
                s=len(number)
                break
            if number[i] == '9': #가장 크니까 더 볼 필요 X
                answer.append(number[i])
                k -= i - s
                s = i + 1
                break
            if number[i] > maxx[0]:
                maxx = [number[i], i]
        else:#9가 max값이 아닌 경우
            answer.append(maxx[0])
            k -= maxx[1] - s
            s = maxx[1] + 1
    return ''.join(answer) + number[s:]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.19ms, 10.3MB)
테스트 6 〉	통과 (2.85ms, 10.3MB)
테스트 7 〉	통과 (4.12ms, 10.2MB)
테스트 8 〉	통과 (11.89ms, 10.3MB)
테스트 9 〉	통과 (1.13ms, 11.9MB)
테스트 10 〉	통과 (64.76ms, 11.6MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
'''