'''
문제)
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력)
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 자연수 N이 주어진다.

출력)
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력한다.
정답이 여러 가지인 경우에는 아무거나 출력한다.
'''
#1124220kb	136ms
from collections import deque
N = int(input())
done = set([N])
que = deque()
que.append([N])
ans = []
while que:
    n = que.popleft()
    num = n[-1]
    if num == 1:
        print(len(n)-1)
        print(*list(n))
        break
    if num%3 == 0 and num//3 not in done:
        que.append((n+[num//3]))
        done.add(num//3)
    if num%2 == 0 and num//2 not in done:
        que.append((n+[num//2]))
        done.add(num//2)
    if num-1>=1 and num-1 not in done:
        que.append((n+[num-1]))
        done.add(num-3)

#done을 set->list
#132028kb	140ms
from collections import deque
N = int(input())
done = [0 for _ in range(1000001)]
que = deque()
que.append([N])
ans = []
while que:
    n = que.popleft()
    num = n[-1]
    if num == 1:
        print(len(n)-1)
        print(*list(n))
        break
    if num%3 == 0 and not done[num//3] :
        que.append((n+[num//3]))
        done[num//3]=1
    if num%2 == 0 and not done[num//2]:
        que.append((n+[num//2]))
        done[num//2]=1
    if num-1>=1 and not done[num-1]:
        que.append((n+[num-1]))
        done[num-1]=1

#1083480kb	2904ms -> done체크X
from collections import deque
N = int(input())
que = deque()
que.append([N])
ans = []
while que:
    n = que.popleft()
    num = n[-1]
    if num == 1:
        print(len(n)-1)
        print(*list(n))
        break
    if num%3 == 0:
        que.append((n+[num//3]))
    if num%2 == 0:
        que.append((n+[num//2]))
    if num-1>=1:
        que.append((n+[num-1]))