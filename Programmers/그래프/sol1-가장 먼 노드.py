from collections import defaultdict, deque
def solution(n, edge):
    d = defaultdict(set)
    for i, j in edge:
        # 양방향
        d[i].add(j)
        d[j].add(i)
    que = deque()
    que.append(d[1])
    done = set()
    done.add(1)
    while que:
        q = que.popleft()
        answer = len(q)
        done |= set(q)
        tmp = set()
        for i in q:
            for j in d[i]:
                if j not in done:
                    tmp.add(j)
        if len(tmp)>0:
            que.append(tmp)
        else:
            return len(q)


정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.7MB)
테스트 2 〉	통과 (0.07ms, 10.8MB)
테스트 3 〉	통과 (0.08ms, 10.9MB)
테스트 4 〉	통과 (0.36ms, 10.9MB)
테스트 5 〉	통과 (1.34ms, 12MB)
테스트 6 〉	통과 (3.07ms, 19.2MB)
테스트 7 〉	통과 (32.35ms, 88.9MB)
테스트 8 〉	통과 (63.73ms, 126MB)
테스트 9 〉	통과 (60.64ms, 125MB)