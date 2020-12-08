#아직 도전중================================================================
#T1(문제 이해 ~ 코딩 시작): 5분 31초
#T2(코딩 시작 ~ 제출): 8분 33초(3분 2초)
#T3(디버깅): 21분6초
from collections import Counter
def solution(n, computers):
    links = {i:i for i in range(n)}
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                links[j]= links[i]
    return len(Counter(links.values()))


from collections import Counter
def solution(n, computers):
    links = {i:i for i in range(n)}
    for i in range(n):
        for j in range(i):
            if computers[i][j]:
                links[i]= min(links[j],links[i])
                break
    return len(Counter(links.values()))


# T1(문제 이해 ~ 코딩 시작): 5분 31초
# T2(코딩 시작 ~ 제출): 8분 33초(3분 2초)
# T3(디버깅):40분 35초(32분 2초: 중단)
from collections import Counter
links = {}
def union(x, y):
    global links
    if links[x] < links[y]:
        links[y] = links[x]
    else:
        links[x] = links[y]


def solution(n, computers):
    global links
    links = {i: i for i in range(n)}
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)
    print(links)
    return len(Counter(links.values()))

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
테스트 6 〉	통과 (0.32ms, 10.2MB)
테스트 7 〉	실패 (0.06ms, 10.1MB)
테스트 8 〉	통과 (0.25ms, 10.2MB)
테스트 9 〉	실패 (0.16ms, 10.2MB)
테스트 10 〉	통과 (0.18ms, 10.2MB)
테스트 11 〉	통과 (1.02ms, 10.3MB)
테스트 12 〉	통과 (0.82ms, 10.3MB)
테스트 13 〉	통과 (0.43ms, 10.2MB)
'''

#45분 21초
from collections import Counter
def solution(n, computers):
    links = {i: i for i in range(n)}
    for i in range(n):
        mini = links[i]

        for j in range(n):
            if computers[i][j]:
                mini = min(mini, links[j])

        links[i] = mini
        for j in range(n):
            if computers[i][j]:
                links[j] = links[i]
    return len(Counter(links.values()))
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.50ms, 10.1MB)
테스트 7 〉	통과 (0.06ms, 10.2MB)
테스트 8 〉	통과 (0.37ms, 10.2MB)
테스트 9 〉	실패 (0.24ms, 10.2MB)   ---> 아씨 한개
테스트 10 〉	통과 (0.25ms, 10.2MB)
테스트 11 〉	통과 (1.37ms, 10.1MB)
테스트 12 〉	통과 (1.22ms, 10.3MB)
테스트 13 〉	통과 (0.65ms, 10.2MB)
'''