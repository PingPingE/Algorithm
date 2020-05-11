'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

'''
#40672kb	180ms
from collections import deque
N,K = map(int, input().split())
if N>=K:#언니가 더 멀리 있는 경우는 '-'연산밖에 적용이 안됨
    print(abs(N-K))
else:
    que = deque()
    que.append((N, 0))
    min_time = K-N
    done = set()
    done.add(N)
    while que:
        cur, time = que.popleft()
        if time >=min_time:
            continue
        if cur == K:
            min_time = time
            break
        for i in [cur+1, cur-1, cur*2]:
            if i not in done and 0<=i<=100001:#시간,메모리 낭비 방지
                que.append((i,time+1))
                done.add(i)
    print(min_time)

