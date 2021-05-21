'''
문제 설명
각 점에 가중치가 부여된 트리가 주어집니다. 당신은 다음 연산을 통하여, 이 트리의 모든 점들의 가중치를 0으로 만들고자 합니다.

임의의 연결된 두 점을 골라서 한쪽은 1 증가시키고, 다른 한쪽은 1 감소시킵니다.
하지만, 모든 트리가 위의 행동을 통하여 모든 점들의 가중치를 0으로 만들 수 있는 것은 아닙니다.
당신은 주어진 트리에 대해서 해당 사항이 가능한지 판별하고, 만약 가능하다면 최소한의 행동을 통하여 모든 점들의 가중치를 0으로 만들고자 합니다.

트리의 각 점의 가중치를 의미하는 1차원 정수 배열 a와 트리의 간선 정보를 의미하는 edges가 매개변수로 주어집니다.
주어진 행동을 통해 트리의 모든 점들의 가중치를 0으로 만드는 것이 불가능하다면 -1을,
가능하다면 최소 몇 번만에 가능한지를 찾아 return 하도록 solution 함수를 완성해주세요.
(만약 처음부터 트리의 모든 정점의 가중치가 0이라면, 0을 return 해야 합니다.)

제한사항
a의 길이는 2 이상 300,000 이하입니다.
a의 모든 수는 각각 -1,000,000 이상 1,000,000 이하입니다.
a[i]는 i번 정점의 가중치를 의미합니다.
edges의 행의 개수는 (a의 길이 - 1)입니다.
edges의 각 행은 [u, v] 2개의 정수로 이루어져 있으며, 이는 u번 정점과 v번 정점이 간선으로 연결되어 있음을 의미합니다.
edges가 나타내는 그래프는 항상 트리로 주어집니다.

입출력 예
a	edges	result
[-5,0,2,1,2]	[[0,1],[3,4],[2,3],[0,3]]	9
[0,1,0]	[[0,1],[1,2]]	-1
'''

from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 8)


def solution(a, edges):
    ans = 0
    if sum(a) == 0:#모든 점의 가중치를 0으로 만드는게 가능한 경우
        links = defaultdict(list)

        for n1, n2 in edges:
            links[n1].append(n2)
            links[n2].append(n1)

        def dfs(n, prev_n):#지금 방문한 노드, 이전에 방문한 노드
            nonlocal ans

            for node in links[n]:
                if node == prev_n: continue
                dfs(node, n)

            a[prev_n] += a[n]
            ans += abs(a[n])
            a[n] = 0

        dfs(0, 0)
    else:#불가능한 경우
        return -1
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (3.27ms, 69.9MB)
테스트 4 〉	통과 (562.74ms, 109MB)
테스트 5 〉	통과 (599.73ms, 109MB)
테스트 6 〉	통과 (3.30ms, 70MB)
테스트 7 〉	통과 (980.17ms, 392MB)
테스트 8 〉	통과 (1028.46ms, 331MB)
테스트 9 〉	통과 (3.28ms, 69.9MB)
테스트 10 〉	통과 (665.66ms, 112MB)
테스트 11 〉	통과 (645.44ms, 109MB)
테스트 12 〉	통과 (3.48ms, 70MB)
테스트 13 〉	통과 (451.28ms, 108MB)
테스트 14 〉	통과 (489.42ms, 109MB)
테스트 15 〉	통과 (3.21ms, 69.9MB)
테스트 16 〉	통과 (922.62ms, 247MB)
테스트 17 〉	통과 (648.99ms, 163MB)
테스트 18 〉	통과 (317.20ms, 108MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''