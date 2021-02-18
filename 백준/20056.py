'''
문제)
어른 상어가 마법사가 되었고, 파이어볼을 배웠다.

마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.

격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.

파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.

7	0	1
6	 	2
5	4	3
마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
파이어볼은 4개의 파이어볼로 나누어진다.
나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

입력)
첫째 줄에 N, M, K가 주어진다.
둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다. 파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

출력)
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.

제한)
4 ≤ N ≤ 50
0 ≤ M ≤ N2
1 ≤ K ≤ 1,000
1 ≤ ri, ci ≤ N
1 ≤ mi ≤ 1,000
1 ≤ si ≤ 1,000
0 ≤ di ≤ 7
'''
#147872kb	344ms
import sys
from collections import defaultdict,deque
def cnt_odd_even(v):#합쳐지는 파이어볼의 방향 홀/짝 카운트 및 질량과 속력의 합 구하기
    m_sum, s_sum = 0,0
    even, odd = 0, 0
    for m, s, d in v:
        m_sum += m
        s_sum += s
        if d % 2:
            odd += 1
        else:
            even += 1
    return m_sum, s_sum, even,odd

N,M,K =map(int, input().split())
balls = deque()
for _ in range(M):
    r,c,m,s,d = map(int, sys.stdin.readline().split())
    balls.append([r-1 ,c-1,m,s,d])
dir={0:[-1,0], 1:[-1,1],2:[0,1],3:[1,1],4:[1,0],5:[1,-1],6:[0,-1],7:[-1,-1]}

while K:
    K-=1
    tmp=defaultdict(list)
    while balls:
        r, c, m, s, d = balls.popleft()
        nr,nc = (r+dir[d][0]*s)%N, (c+dir[d][1]*s)%N #나머지를 나누는 수(N)와 부호가 동일 *참고: http://mobilelab.khu.ac.kr/webpythonbbs/?vid=19
        print("raw:",(r+dir[d][0]*s, c+dir[d][1]*s),"from r,c:",(r,c), "==to: ",(nr,nc), "dir:",dir[d], '==s:', s)
        tmp[(nr,nc)].append([m,s,d])

    for k,v in tmp.items():
        if len(v)>=2:#2개 이상 겹칠 경우
            cnt= len(v)
            m_sum,s_sum,even,odd = cnt_odd_even(v)
            nm = m_sum//5
            ns = s_sum//cnt
            nd = []
            if nm == 0: continue
            if odd == cnt or even==cnt:
                for d in [0,2,4,6]:
                    balls.append([k[0],k[1],nm,ns,d])
            else:
                for d in [1,3,5,7]:
                    balls.append([k[0],k[1],nm,ns,d])
        else:
            balls.append([k[0],k[1]]+v[0][:])

total_m = 0
while balls:
    r,c,m,s,d=balls.popleft()
    total_m+=m
print(total_m)