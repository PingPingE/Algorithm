'''
문제)
반도체를 설계할 때 n개의 포트를 다른 n개의 포트와 연결해야 할 때가 있다.

예를 들어 왼쪽 그림이 n개의 포트와 다른 n개의 포트를 어떻게 연결해야 하는지를 나타낸다.
하지만 이와 같이 연결을 할 경우에는 연결선이 서로 꼬이기 때문에 이와 같이 연결할 수 없다.
n개의 포트가 다른 n개의 포트와 어떻게 연결되어야 하는지가 주어졌을 때, 연결선이 서로 꼬이지(겹치지, 교차하지) 않도록 하면서 최대 몇 개까지 연결할 수 있는지를 알아내는 프로그램을 작성하시오

입력)
첫째 줄에 정수 n(1 ≤ n ≤ 40,000)이 주어진다.
다음 줄에는 차례로 1번 포트와 연결되어야 하는 포트 번호, 2번 포트와 연결되어야 하는 포트 번호, …, n번 포트와 연결되어야 하는 포트 번호가 주어진다.
이 수들은 1 이상 n 이하이며 서로 같은 수는 없다고 가정하자.

출력)
첫째 줄에 최대 연결 개수를 출력한다.
'''
import sys
from collections import deque
n= int(input())
links = {from_: to_ for from_, to_ in enumerate(map(int, sys.stdin.readline().split()),1)}
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    print(dp)
    j = i-1
    tmp = 0
    while j>0 and links[j]>links[i]:
        j-=1
    print(j)
    dp[i] = max(dp[j]+1, dp[i-1])

print(dp[-1])

#영원히 끝나지 않음
def sol(n, li):
    links = {from_: to_ for from_, to_ in enumerate(li, 1)}
    que = deque()
    ans = 0
    for i in range(1, n + 1):
        que.append([i, 0])  # 현재 포트, 연결 개수

    while que:
        port, cnt = que.popleft()
        ans = max(ans, cnt)

        for n_port in range(links[port], n + 1):
            if links[n_port] > links[port]:
                que.append([n_port, cnt + 1])
    return ans

#틀림
def sol2(n, li):
    links = {from_: to_ for from_, to_ in enumerate(li, 1)}
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        j = i - 1
        tmp = 0
        while j > 0 and links[j] > links[i]:
            j -= 1
        dp[i] = max(dp[j] + 1, dp[i - 1])
    return dp[-1]
# print(sol2(40000, range(1,40001)))