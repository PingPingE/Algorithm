from collections import deque
N,K = map(int, input().split())
if N >= K:
    print(N-K)
    arr  = []
    for i in range(N,K-1,-1):
        arr.append(str(i))
    print(' '.join(arr).strip())
else:
    que = deque()
    que.append(N)
    m = {N:-1}
    while K not in m:
        q = que.popleft()
        for j in [q*2, q+1, q-1]:
            if 0<= j<100001 and j not in m:
                m[j] = q
                que.append(j)

    que.clear()
    tmp = K
    while tmp != -1:
        que.appendleft(str(tmp))
        tmp = m[tmp]

    print(len(que)-1)
    print(' '.join(que).strip())
