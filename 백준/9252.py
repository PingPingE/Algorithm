'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력한다.

LCS가 여러 가지인 경우에는 아무거나 출력하고, LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.
'''
#LCS 참고:https://twinw.tistory.com/126, https://beginthread.tistory.com/142, https://pacific-ocean.tistory.com/435
#131100kb 136ms
# get_lcs()함수 구현에 굉장히 오래 걸린 문제 (시도1에 대한 반례를 찾지 못했다)

def get_len():
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                memo[i][j] = memo[i - 1][j - 1] + 1  # 현재 값을 보기 전인 왼쪽 위 값 + 1
            else:
                memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])  # 위나 왼쪽 원소 중 더 큰 값
    return memo[-1][-1]

def get_lcs():#9251번 문제에서 추가된 점
    # maxx = memo[-1][-1]
    # if not maxx: return
    r,c=len(str1), len(str2)#끝에서부터 역방향으로
    ans = []
    while r>0 and c>0:
        #시도2
        if memo[r][c-1] == memo[r][c]:
            c-=1
        elif memo[r-1][c] == memo[r][c]:
            r-=1
        else:
            ans.append(str1[r-1])
            r-=1
            c-=1
    '''
    #시도1 => 왜 틀렸을까
    while maxx>0:
        if memo[r][c-1]==memo[r-1][c]:
            ans.append(str1[r-1])
            maxx-=1
            r-=1
            c-=1

        else:
            if memo[r][c-1] > memo[r-1][c]:
                c -= 1
            else:
                r -= 1
    '''

    return ''.join(ans[::-1])

str1,str2=input(), input()
ans=''
memo = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
print(get_len())
print(get_lcs())