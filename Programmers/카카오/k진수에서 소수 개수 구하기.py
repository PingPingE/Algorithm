'''
문제 설명
양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.
0P0처럼 소수 양쪽에 0이 있는 경우
P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
P처럼 소수 양쪽에 아무것도 없는 경우
단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
예를 들어, 101은 P가 될 수 없습니다.
예를 들어, 437674을 3진수로 바꾸면 211020101011입니다. 여기서 찾을 수 있는 조건에 맞는 소수는 왼쪽부터 순서대로 211, 2, 11이 있으며, 총 3개입니다.
(211, 2, 11을 k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다는 점에 주의합니다.) 211은 P0 형태에서 찾을 수 있으며, 2는 0P0에서, 11은 0P에서 찾을 수 있습니다.
정수 n과 k가 매개변수로 주어집니다. n을 k진수로 바꿨을 때, 변환된 수 안에서 찾을 수 있는 위 조건에 맞는 소수의 개수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
1 ≤ n ≤ 1,000,000
3 ≤ k ≤ 10

'''
import string, re, math
def solution(n, k):
    answer = -1
    tmp = string.digits + string.ascii_lowercase
    #10진수 -> k진수
    def convert(num, base):
        q, r = divmod(num, base) #몫, 나머지
        if q == 0:
            return tmp[r]
        else:
            return convert(q, base) + tmp[r]
    #소수 체크
    def is_prime(n):
        if n<2: return False
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True

    #일치 패턴 찾기
    def pattern_check(n):
        str_n = str(n)
        cnt = 0
        s,e =0,0
        while s<=e and e < len(n):
            if str_n[e] != '0':
                e+=1
            else:
                if s!=e and is_prime(int(str_n[s:e].strip('0'))):
                    # print(str_n[s:e+1])
                    cnt +=1
                e+=1
                s=e
        #마지막꺼까지 체크
        if s != e and is_prime(int(str_n[s:e].strip('0'))):
            # print(str_n[s:e + 1])
            cnt += 1
        return cnt
    answer = pattern_check(convert(n,k))
    return answer

# solution(1000000,3)
solution(437674, 3)

