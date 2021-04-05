'''
문제)
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다.
Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는
1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

입력)
첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고,
i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력)
첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.
'''
#sol1: 내장 함수로 조합 구하기
#123512kb	884ms
from itertools import combinations
import sys
def get_diff(t1,t2):#=======team1과 team2의 능력치 차이 구하기
    return abs(get_sum(t1)-get_sum(t2))

def get_sum(t):#=======team의 능력치 합 구하기
    sum=0
    for i in t:
        for j in t:
            sum+=S[i][j]
    return sum

N=int(input())
S=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total=set(range(N))
ans=sys.maxsize
for comb in combinations(range(N),N//2):#=======조합 구하기
    team1=set(comb)
    team2=total-team1
    ans=min(ans, get_diff(team1,team2))
print(ans)

#sol2: bit masking으로 조합 구하기
#123628kb	868ms
import sys
def get_team1(x):#=====bit 체크하면서 team1 set에 구성원 index 담기
    tmp=set()
    n=0
    while x:
        if x&1:tmp.add(n)
        x>>=1
        n+=1
    return tmp

def get_diff(t1,t2):
    return abs(get_sum(t1)-get_sum(t2))

def get_sum(t):
    sum=0
    for i in t:
        for j in t:
            sum+=S[i][j]
    return sum

N=int(input())
S=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans=sys.maxsize
total=set(range(N))
for i in range(1<<N):
    team1=get_team1(i)
    if len(team1)==N//2:
        ans=min(ans, get_diff(team1,total-team1))
print(ans)


#sol3: 최적화
#123756kb	708ms (868 -> 708 속도 개선)
import sys
def count_bits(x):#=====count만(조건에 못미치는데 계속 set에 add연산을 했으니까)
    n=0
    while x:
        if x&1:n+=1
        x>>=1
    return n

def get_diff(t1,t2):
    return abs(get_sum(t1)-get_sum(t2))

def get_sum(t):
    sum=0
    for i in t:
        for j in t:
            sum+=S[i][j]
    return sum

N=int(input())
S=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans=sys.maxsize
for i in range(1<<N):
    if count_bits(i)==N//2: #====카운트만 해서 조건에 만족하면
        team1,team2=set(),set()
        for j in range(N):#====팀 구하는 걸로
            if i&(1<<j): team1.add(j)
            else: team2.add(j)
        ans=min(ans, get_diff(team1,team2))
print(ans)