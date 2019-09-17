from collections import deque
N,K = map(int, input().split())
if N>=K:
    print(N-K)
    print(1)
else:
    if K*2<=100000:
        maxx = K*2
    else: maxx = 100001
    #시간, 방법 수
    m={i:[-1,0] for i in range(maxx)}
    m[N][0] ,m[N][1] = 0,1
    que = deque()
    que.append(N)
    while que:
        q = que.popleft()
        for j in [q*2, q+1, q-1]:
            if 0<=j<maxx:
                #한번도 와본적 X
                if m[j][0] == -1:
                    m[j][0] = m[q][0]+1
                    m[j][1] += m[q][1]
                    que.append(j)
                #이미 와봤지만 시간이 같을때
                elif m[j][0] == m[q][0]+1:
                    m[j][1] += m[q][1]
    print(m[K][0])
    print(m[K][1])
