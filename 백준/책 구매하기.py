'''
문제
총 N명의 사람이 책을 구매하려고 한다. 각 사람은 1번부터 N번까지 번호가 매겨져 있고, 각 사람이 사려고하는 책의 개수는 A1, A2, ..., AN권이다.
이 책을 판매하는 온라인 서점은 총 M곳이 있다.각 서점도 1번부터 M번까지 번호가 매겨져 있으며, 각 서점이 가지고 있는 책의 개수는 B1, B2, ..., BM권 이다.

이 책을 사려고 하는 사람은 N명밖에 없으며, 서점에서 가지고 있는 책의 개수의 합과 사람들이 사려고 하는 책의 개수의 합은 같다.

이 온라인 서점은 책을 한권씩만 택배로 보낸다. 또, 택배비는 서점과 사람들 사이의 거리, 회원 등급등 여러 가지 요인에 따라 결정된다.
서점 i에서 사람 j에게 책을 한 권 보내는데 필요한 배송비는 Cij원이다.
모든 서점과 사람 사이의 배송비가 주어졌을 때, 각 사람이 책을 A1, A2, ..., AN권을 사는데 필요한 배송비의 합의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 사람의 수 N과 온라인 서점의 수 M이 주어진다. (1 ≤ N, M ≤ 100)
둘째 줄에는 각 사람이 사려고 하는 책의 개수 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100)
셋째 줄에는 각 온라인 서점이 가지고 있는 책의 개수 B1, B2, ..., BM이 주어진다. (1 ≤ Bi ≤ 100)
넷째 줄부터 M개의 줄에는 각 온라인 서점이 각 사람들에게 책을 한 권 보내는데 필요한 배송비 Cij가 주어진다.
i번째 줄의 j번째 숫자는 온라인 서점 i에서 사람 j에게 책을 한 권 보내는데 필요한 배송비 Cij이다. (1 ≤ Cij ≤ 1,000)

A1 + A2 + ... + AN은 B1 + B2 + ... + BM과 같다.

출력
첫째 줄에 배송비의 최솟값을 출력한다.
'''
import sys
from collections import deque
#참고: https://cael0.github.io/problem%20solving/BOJ11405/

INF = sys.maxsize

N, M = map(int,input().split())
A= list(map(int, input().split()))
B= list(map(int, input().split()))
C= list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
graph = [[] for _ in range(M+N+2)]

#source -> 서점
for i in range(1, M+1): #서점
    #[노드, capacity]
    graph[0].append([i, B[i-1]])

    #서점 -> 사람
    for j in range(M+1, M+N+1): #사람
        graph[i].append([j, INF])

#사람 -> target
for j in range(M+1,M+N+1): #사람
    graph[j].append([M+N+1, A[j-M-1]])

T=1
#최종 return 값
weight = 0
while True:
    print("=====", T, "=======")
    T+=1
    #비용 초기화
    res = [INF] * (M+N+2)
    res[0] = 0

    #돌아갈 노드 저장
    prev = [-1] * (M+N+2)
    visit = [0] * (M+N+2)

    #source부터
    queue = deque([0])

    #최단 경로(최소 비용) 찾기: SPFA(Shortest Path Faster Algorithm)
    while queue:
        cur = queue.popleft()
        visit[cur] = 0

        for nxt, capacity in graph[cur]:
            if 0 < cur < nxt < M+N+1: #서점 -> 사람 비용
                cost = C[cur - 1][nxt - M - 1]
            elif 0 < nxt < cur < M+N+1: #서점 <- 사람 (음의 간선) 비용
                cost = - C[nxt - 1][cur - M - 1]
            else: # source 나 target이면 capacity는 무한대, 비용은 0
                cost = 0

            #최소비용 갱신
            if res[nxt] > res[cur] + cost:
                res[nxt] = res[cur] + cost
                prev[nxt] = cur #이전 노드 저장

                if not visit[nxt]:
                    queue.append(nxt)
                    visit[nxt] = 1

    if res[-1] == INF:
        break

    #최대 유량 흘려주기: 최단거리에 포함된 간선들 중 최소의 capacity만큼
    flow = INF
    nxt = M+N+1

    #최단거리에 포함된 간선들 중 capacity 최솟값 구하기 -> flow
    while nxt:
        cur = prev[nxt]
        for i in range(len(graph[cur])):
            if graph[cur][i][0] == nxt:
                flow = min(flow, graph[cur][i][1])
                break
        nxt = cur

    #최대로 흘려줄 수 있는 flow를 구했으니 Flow 구하기
    nxt = M+N+1 #사람
    while nxt:
        cur = prev[nxt] #서점

        #배송비(weight) 갱신
        if 0 < cur < nxt < M+N+1:
            weight += flow * C[cur - 1][nxt-M-1]
        elif 0 < nxt < cur < M+N+1:
            weight -= flow * C[nxt - 1][cur-M-1]

        #서점 capacity 갱신
        for i in range(len(graph[cur])):
            if graph[cur][i][0] == nxt:
                graph[cur][i][1] -= flow
                if graph[cur][i][1] == 0: #용량이 다 찬경우 remove(상한값(flow)이 있으니 음수(flow > capacity)가 될 일은 없음)
                    graph[cur].remove([nxt, 0])
                break

        #흘려준 유량 더하기
        for i in range(len(graph[nxt])):
            if graph[nxt][i][0] == cur:
                graph[nxt][i][1] += flow
                break
        else:
            graph[nxt].append([cur, flow])

        nxt = cur
    print("flow:", flow, " weight:", weight)
    print("prev: ",prev)
    print(res)
    print("graph")
    for e,g in enumerate(graph):
        print(f"{e}: {g}")
print(graph)

print(weight)