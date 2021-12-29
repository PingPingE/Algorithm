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
from itertools import permutations
#1,2와 2,3의 CS를 구하고, 공통된 것중에 가장 긴 것 픽 -> 역시 시간초과
st_list = list(input() for _ in range(3))
set_12, set_23 = set(), set()
def get_CS(st1, st2):
    common = []
    for i in range(len(st1)):
        for j in range(len(st2)):
            if st1[i-1] == st2[j-1]:
                common.append(st1[i-1])
    return common
ans = 0
candi_st = [get_CS(st_list[0], st_list[1]), get_CS(st_list[1], st_list[2]), get_CS(st_list[0], st_list[2])]
min_size = min([len(candi_st[i]) for i in range(3)])
for size in range(1,min_size+1):
    perm_list = list(set(permutations(candi_st[i], size)) for i in range(3))
    if perm_list[0]&perm_list[1]&perm_list[2]:
        ans = size
print(size)
