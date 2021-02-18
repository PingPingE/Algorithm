'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다
'''
#143820kb	224ms
from collections import deque
N,K = map(int, input().split())
if N>=K: print(N-K)
else:
    que = deque([[N,0]])
    done = set([N])
    while que:
        cur,time= que.popleft()
        if cur==K:
            print(time)
            break
        if cur-1>=0 and cur-1 not in done:
            done.add(cur-1)
            que.append([cur-1, time+1])
        if cur+1<=100000 and cur+1 not in done:
            done.add(cur+1)
            que.append([cur+1, time+1])
        if cur*2<=K*2 and cur*2 not in done:
            done.add(cur*2)
            que.append([cur*2, time+1])

#145752kb	188ms
#중복 줄이기
from collections import deque
N,K = map(int, input().split())
if N>=K: print(N-K)
else:
    que = deque([[N,0]])
    done = set([N])
    while que:
        cur,time= que.popleft()
        if cur==K:
            print(time)
            break
        for candi in [cur-1, cur+1, cur*2]:
            if 0<=candi<=2*K and candi not in done:
                done.add(candi)
                que.append([candi, time+1])