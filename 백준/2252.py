'''
N명의 학생들을 키 순서대로 줄을 세우려고 한다.
각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다.
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

첫째 줄에 N(1≤N≤32,000), M(1≤M≤100,000)이 주어진다. M은 키를 비교한 회수이다.
다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

학생들의 번호는 1번부터 N번이다.
'''
#136188kb 480ms
from collections import deque, defaultdict
N,M = map(int, input().split())
node = defaultdict(list)
degree = {i:0 for i in range(1, N+1)} #진입차수

for _ in range(M):
    a,b =map(int, input().split())
    node[a].append(b)
    degree[b] += 1

#진입차수가 0인것만 큐에 넣음
que = deque(filter(lambda x: degree[x] == 0, degree.keys()))
result = []
while len(que) >0:
    target = que.popleft()
    result.append(target)
    for i in node[target]: #target노드의 간선 제거
        degree[i] -= 1#간선이 제거되었으므로 -1
        if degree[i] ==0: #제거 후 진입차수가 0이 되었으면 큐에 넣기
            que.append(i)
print(" ".join(map(str, result)))
