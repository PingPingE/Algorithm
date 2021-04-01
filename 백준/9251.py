'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''
#131112kb	164ms
def get_len():#LCS 길이 구하기
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i - 1][j - 1] + 1 # 현재 값을 보기 전인 왼쪽 위 값 + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])  # 위나 왼쪽 원소 중 더 큰 값
    return memo[-1][-1]
str1,str2=input(), input()
ans=''
memo = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
print(get_len())