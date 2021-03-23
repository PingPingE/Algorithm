'''
문제)
정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

입력)
첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진다.

출력)
A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.
'''
#sol1: BFS
#141648kb	180ms
from collections import deque

def op1(x): #2를 곱하는 연산
    return x*2

def op2(x): #1을 수의 가장 오른쪽에 추가하는 연산
    return x*10+1

A,B=map(int, input().split())
ans=-1
que=deque([(A,0)])
done=set([A])
while que:
    x,cnt = que.popleft()
    if x==B:
        ans = cnt+1
        break

    x1,x2=op1(x),op2(x)
    if x1 not in done and x1<=B:#조건 체크
        que.append((x1, cnt+1))
        done.add(x1)

    if x2 not in done and x1<=B:#조건 체크
        que.append((x2, cnt+1))
        done.add(x2)
print(ans)

#sol2: B -> A
#121220kb	112ms
A,B=map(int, input().split())
ans, cnt=-1,0
if A==B:
    ans=0
else:
    while A<=B: #굳이 큐에 넣을 필요가 없다
        if A==B:
            ans=cnt+1
            break
        #나머지 연산으로 조건 체크
        if B%2==0:
            B//=2
        elif B%10==1:
            B//=10
        else:
            break
        cnt+=1
print(ans)