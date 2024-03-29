'''
문제 설명)
xx 회사의 2xN명의 사원들은 N명씩 두 팀으로 나눠 숫자 게임을 하려고 합니다. 두 개의 팀을 각각 A팀과 B팀이라고 하겠습니다. 숫자 게임의 규칙은 다음과 같습니다.

먼저 모든 사원이 무작위로 자연수를 하나씩 부여받습니다.
각 사원은 딱 한 번씩 경기를 합니다.
각 경기당 A팀에서 한 사원이, B팀에서 한 사원이 나와 서로의 수를 공개합니다. 그때 숫자가 큰 쪽이 승리하게 되고, 승리한 사원이 속한 팀은 승점을 1점 얻게 됩니다.
만약 숫자가 같다면 누구도 승점을 얻지 않습니다.
전체 사원들은 우선 무작위로 자연수를 하나씩 부여받았습니다. 그다음 A팀은 빠르게 출전순서를 정했고 자신들의 출전 순서를 B팀에게 공개해버렸습니다.
B팀은 그것을 보고 자신들의 최종 승점을 가장 높이는 방법으로 팀원들의 출전 순서를 정했습니다. 이때의 B팀이 얻는 승점을 구해주세요.
A 팀원들이 부여받은 수가 출전 순서대로 나열되어있는 배열 A와 i번째 원소가 B팀의 i번 팀원이 부여받은 수를 의미하는 배열 B가 주어질 때,
B 팀원들이 얻을 수 있는 최대 승점을 return 하도록 solution 함수를 완성해주세요.

제한사항)
A와 B의 길이는 같습니다.
A와 B의 길이는 1 이상 100,000 이하입니다.
A와 B의 각 원소는 1 이상 1,000,000,000 이하의 자연수입니다.
'''

def solution(A, B):
    ans=0
    A=sorted(A)
    B=sorted(B)
    while A:
        a= A.pop()
        if a < B[-1]:
            ans+=1
            B.pop()
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.03ms, 10.1MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.24ms, 10.1MB)
테스트 10 〉	통과 (0.15ms, 10.2MB)
테스트 11 〉	통과 (0.42ms, 10.2MB)
테스트 12 〉	통과 (0.18ms, 10.2MB)
테스트 13 〉	통과 (1.74ms, 10.4MB)
테스트 14 〉	통과 (2.93ms, 10.7MB)
테스트 15 〉	통과 (3.83ms, 10.5MB)
테스트 16 〉	통과 (2.79ms, 10.8MB)
테스트 17 〉	통과 (0.25ms, 10.3MB)
테스트 18 〉	통과 (0.34ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (52.75ms, 19.3MB)
테스트 2 〉	통과 (49.63ms, 19.3MB)
테스트 3 〉	통과 (47.70ms, 19.2MB)
'''