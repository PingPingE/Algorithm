'''
문제
문자열과 놀기를 세상에서 제일 좋아하는 영식이는 오늘도 문자열 2개의 LCS(Longest Common Subsequence)를 구하고 있었다.
어느 날 영식이는 조교들이 문자열 3개의 LCS를 구하는 것을 보았다. 영식이도 도전해 보았지만 실패하고 말았다.

이제 우리가 할 일은 다음과 같다. 영식이를 도와서 문자열 3개의 LCS를 구하는 프로그램을 작성하라.

입력
첫 줄에는 첫 번째 문자열이, 둘째 줄에는 두 번째 문자열이, 셋째 줄에는 세 번째 문자열이 주어진다. 각 문자열은 알파벳 소문자로 이루어져 있고, 길이는 100보다 작거나 같다.

출력
첫 줄에 첫 번째 문자열과 두 번째 문자열과 세 번째 문자열의 LCS의 길이를 출력한다.
'''
#1,2와 2,3의 CS를 구하고, 공통된 것중에 가장 긴 것 픽 -> 역시 시간초과

#솔루션: 기존 2차원 풀이를 3차원으로
#134228kb	188ms
st_list = list(input() for _ in range(3))

def get_CS(st_list):
    ans = 0
    st1,st2,st3 = st_list
    cs = list(list([0]*(len(st3)+1) for _ in range(len(st2)+1)) for __ in range(len(st1)+1))
    for i in range(1,len(st1)+1):
        for j in range(1,len(st2)+1):
            for k in range(1,len(st3)+1):
                if st1[i-1] == st2[j-1] == st3[k-1]:
                    cs[i][j][k] = cs[i-1][j-1][k-1] +1
                    ans = max(ans,cs[i][j][k])
                else:
                    cs[i][j][k] = max(cs[i-1][j][k], cs[i][j-1][k] , cs[i][j][k-1])

    return ans

print(get_CS(st_list))
