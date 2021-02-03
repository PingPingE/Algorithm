'''
문제)
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력)
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력)
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''
#141160kb	232ms
from collections import deque
N, K = map(int, input().split())
if N>= K: #수빈이가 더 멀리 있는 경우(-1만 가능)
    print(abs(N-K))
else:
    que = deque()
    que.append((N,0))
    minn = 100001
    done = set([N])
    while que:
        x,time = que.popleft()
        if time >= minn: continue
        if x >= K:
            minn = min(time+(x-K), minn)
            continue

        for e,t in enumerate([x-1,x+1,x*2]):
            if t<0: continue
            if t not in done:
                if t >= K:
                    tmp = 0 if e==2 else 1 #-1,+1로 t를 만든 경우는 시간+1 해줘야하므로
                    minn = min(time + (t - K) + tmp, minn)
                else:
                    if e==2:#*2로 간 경우
                        que.append((t,time))
                        done.add(x)
                    else:
                        que.append((t,time+1))
                        done.add(x)
    print(minn)
