'''
문제
남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다.
그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 김지민은 K개의 글자를 가르칠 시간 밖에 없다.
김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다.
김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다.
학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N과 K가 주어진다. N은 50보다 작거나 같은 자연수이고, K는 26보다 작거나 같은 자연수 또는 0이다.
둘째 줄부터 N개의 줄에 남극 언어의 단어가 주어진다. 단어는 영어 소문자로만 이루어져 있고, 길이가 8보다 크거나 같고, 15보다 작거나 같다.
모든 단어는 중복되지 않는다.

출력
첫째 줄에 김지민이 K개의 글자를 가르칠 때, 학생들이 읽을 수 있는 단어 개수의 최댓값을 출력한다.
'''
#====시간초과=====
import sys
def count():#현재 알고있는 알파벳으로 읽을 수 있는 단어 개수
    tmp_cnt=0
    for word in words:
        for i in range(26):
            if word[i]==0: continue
            if word[i] and not known[i]: break
        else:
            tmp_cnt+=1
    return tmp_cnt

def dfs(cur_cnt):
    global cnt,K
    if sum(known) == K:
        cnt = max(cnt, cur_cnt)
        return

    for i in range(26):
        if not known[i]:
            known[i]=1
            dfs(count())
            known[i]=0

N,K= map(int, input().split())
words=[[0]*26 for _ in range(N)] #비트마스킹으로 각 단어에 포함된 알파벳 표시
for _ in range(N):
    for s in set(sys.stdin.readline().rstrip()):
        words[_][ord(s)-97] =1
cnt=0
if K<5: cnt=0
elif K==26: cnt=N
else:
    known=[0]*26
    for i in ['a','n','t','i','c']: #필수 포함 알파벳
        known[ord(i)-97]=1
    dfs(count())
print(cnt)