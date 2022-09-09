#점화식 parent[x][k] = parent[parent[x][k-1]][k-1]
## x번째 노드의 k번째 조상 = x번째 노드의 k-1 조상인 노드의 k-1번째 조상
#https://velog.io/@shiningcastle/최소-공통-조상-알고리즘

import sys
from collections import defaultdict
T= int(input())
while T:
    T-=1
    N = int(input())
    parent = [0]*(N+1)
    level = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, sys.stdin.readline().split())
        parent[b]=a

    t1,t2= map(int, input().split())

    #level 구하기
    for i in range(1, N+1):
        cnt = 0
        p = parent[i]
        while p>0:
            cnt+=1
            prev=p
            p=parent[prev]
        level[i] = cnt

    print(level)
    print(parent)
    print("------")

    t_level = min(level[t1], level[t2])
    #level이 같아질때까지 부모타고 올라가기
    for t in [t1, t2]:
        if level[t] == t_level:
            continue
        else:
            level[t] -=1
            n_p = parent[t]
            parent[t] = parent[n_p]

    print(level)
    print(parent)