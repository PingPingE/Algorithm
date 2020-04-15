'''
1260번) DFS와 BFS
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''
'''
입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는
두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
입력으로 주어지는 간선은 양방향이다.
'''
'''
출력:
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.

'''
import sys

N, M, V = map(int, sys.stdin.readline().split())
mapping = {}
for i in range(M):
    one, two =  map(int,sys.stdin.readline().split())
    if one not in mapping:
        mapping[one] = []
    mapping[one].append(two)
    if two not in mapping:
        mapping[two] =[]
    mapping[two].append(one)

def dfs(map, V):
    m = map
    result = ''
    stack = []
    done = set()
    stack.append(V)

    while stack:
        st = stack.pop()
        if st in done:
            continue
        result += str(st)+' '
        done.add(st)
        if st not in m:
            continue

        if len(m[st]) > 1:
            m[st].sort(reverse=True)
        for i in m[st]:
            if i not in done:
                stack.append(i)

    return result.rstrip()

def bfs(map,V):
    m =map
    result = ''
    que = []
    done = set()
    que.append(V)
    while que:
        q = que.pop(0)
        if q in done:
            continue
        result += str(q)+' '
        done.add(q)
        if q not in m:
            continue
        if len(m[q])>1:
            m[q].sort()
        for i in m[q]:
            if i not in done:
                que.append(i)
    return result.rstrip()

print(dfs(mapping,V))
print(bfs(mapping,V))
