'''
문제)
강토는 Day Of Mourning의 기타리스트로, 다가오는 공연을 준비하고 있다.

어느 날 강토의 집에 도둑이 들어서 기타를 모두 도둑맞고 말았다. 기타를 사야 한다.

강토는 공연 때 연주할 노래의 목록을 뽑아 놓았다. 하지만, 하나의 기타로 모든 곡을 연주할 수는 없다. 어떤 기타는 어떤 곡을 연주할 때, 이상한 소리가 나기 때문이다.
항상 완벽을 추구하는 강토는 이런 일을 용납하지 않는다.

최대한 많은 곡을 제대로 연주하려고 할 때, 필요한 기타의 최소 개수를 구하는 프로그램을 작성하시오.

예를 들어, GIBSON으로 1, 2, 3번 곡을 제대로 연주할 수 있고, FENDER로 1, 2, 5번 곡을 제대로 연주할 수 있고,
EPIPHONE으로 4, 5번 곡을 제대로 연주할 수 있고, ESP로 1번곡을 제대로 연주할 수 있다면, 세준이는 EPIPHONE과 GIBSON을 사면 최소의 개수로 모든 곡을 연주할 수 있다.

입력)
첫째 줄에 기타의 개수 N과 곡의 개수 M이 주어진다. N은 10보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 기타의 이름과 기타가 연주할 수 있는 곡의 정보가 차례대로 주어진다. Y는 연주할 수 있는 것이고, N은 없는 것이다.
기타의 이름은 알파벳 대문자로만 이루어져 있고, 길이는 50 이하이다.

출력)
첫째 줄에 필요한 기타의 개수를 출력한다. 만약 연주할 수 있는 곡이 없으면 -1을 출력한다.
'''
#123456kb	132ms
import sys
N,M=map(int, input().split())
guitars=[]
ans=[-1,-1]#곡 수, 기타 수
dic = {'Y':1, 'N':0}
for _ in range(N):
    g,info =sys.stdin.readline().split()
    guitars.append([dic[i] for i in info])

def dfs(from_, s_cnt, g_cnt): #guitars 시작 인덱스, 곡 비트 마스킹, 기타 수
    s = sum(s_cnt)
    # print(s_cnt, g_cnt)
    if ans[0] < s:
        ans[0] = s
        ans[1] = g_cnt
    elif ans[0] == s:
        ans[1] = min(ans[1], g_cnt)

    if from_ >= N:
        return

    for i in range(from_, N):
        tmp = s_cnt[:]
        for e,j in enumerate(guitars[i]):
            tmp[e] = 1 if j+tmp[e] >=1 else 0
        dfs(i+1, tmp[:] ,g_cnt+1)

dfs(0,[0 for _ in range(M)], 0)
print(-1 if ans[0]==0 else ans[1])#연주할 곡 없으면 -1

