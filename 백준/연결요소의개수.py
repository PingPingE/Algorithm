'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''
#115700kb	360ms
import sys
def union(x,y):
    global links
    x_ = find(x)
    y_ = find(y)
    if x_ < y_:
        links[y_]= x_
    else:
        links[x_] = y_

def find(x):
    global links
    if links[x] == x:
        return x
    links[x] = find(links[x])
    return links[x]

N,M =map(int, input().split())
links = {k:k for k in range(1,N+1) }
for _ in range(M):
    x,y = map(int, sys.stdin.readline().split())
    union(x,y)

#마지막에 하나씩 다 확인하고 parent 갱신해줘야함 (이것때매 계속 80%대에서 ㅂㄷㅂㄷ)
for k in links:
    find(k)

print(len(set(links.values())))
