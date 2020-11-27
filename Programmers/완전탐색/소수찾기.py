'''
문제 설명)
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항)
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''

from itertools import permutations
N = 10000000 #최대 7이하 문자열 대상이므로(최대 9999999)
check = [0 for _ in range(N)] #소수면 0 아니면 1
check[0] = 1
check[1] = 1
for num in range(2,N):
    if check[num]: continue
    for n in range(num*num,N,num):
        check[n] = 1

def solution(numbers):
    answer = set()
    for num in range(1,len(numbers)+1):
        for p in permutations(numbers,num):
            integer = int(''.join(p))
            if integer in answer: continue
            if not check[integer]:
                answer.add(integer)
    return len(answer)

'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 86.4MB)
테스트 2 〉	통과 (0.75ms, 86.4MB)
테스트 3 〉	통과 (0.04ms, 86.5MB)
테스트 4 〉	통과 (0.62ms, 86.5MB)
테스트 5 〉	통과 (3.91ms, 86.6MB)
테스트 6 〉	통과 (0.04ms, 86.5MB)
테스트 7 〉	통과 (0.06ms, 86.4MB)
테스트 8 〉	통과 (4.18ms, 86.5MB)
테스트 9 〉	통과 (0.04ms, 86.5MB)
테스트 10 〉	통과 (0.70ms, 86.5MB)
테스트 11 〉	통과 (0.16ms, 86.5MB)
테스트 12 〉	통과 (0.14ms, 86.5MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''