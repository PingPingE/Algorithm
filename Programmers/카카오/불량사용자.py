import re 
from itertools import product
done = set()
def solution(user_id, banned_id):
    mat =[[] for _ in range(len(banned_id))]
    for e, b_id in enumerate(banned_id):
        b_id = b_id.replace('*', '.')
        for u_id in user_id:
            if len(u_id) == len(b_id) and re.match(b_id, u_id):
                mat[e].append(u_id)  
    '''
    # sol1)
    done = set()
    for p in map(lambda x: list(x) if len(set(x))==len(banned_id) else 0, product(*mat)):
        if p != 0:
            p.sort()
            s = ''.join(p)
            if s not in done:
                done.add(s)
    '''
    #sol2)
    done = []
    for p in map(lambda x: list(x) if len(set(x))==len(banned_id) else 0, product(*mat)):
        if p:
            p = set(p)
            if p not in done:
                done.append(p)
    return len(done)

'''
정확성  테스트(sol1)
테스트 1 〉	통과 (0.09ms, 10.9MB)
테스트 2 〉	통과 (0.20ms, 10.8MB)
테스트 3 〉	통과 (0.19ms, 10.8MB)
테스트 4 〉	통과 (0.17ms, 10.9MB)
테스트 5 〉	통과 (6332.70ms, 10.7MB)
테스트 6 〉	통과 (1.95ms, 10.9MB)
테스트 7 〉	통과 (0.18ms, 10.7MB)
테스트 8 〉	통과 (0.21ms, 10.8MB)
테스트 9 〉	통과 (0.21ms, 10.8MB)
테스트 10 〉	통과 (0.27ms, 10.8MB)
테스트 11 〉	통과 (0.24ms, 10.8MB)


정확성  테스트(sol2)
테스트 1 〉	통과 (0.09ms, 10.7MB)
테스트 2 〉	통과 (0.20ms, 10.9MB)
테스트 3 〉	통과 (0.17ms, 10.7MB)
테스트 4 〉	통과 (0.17ms, 10.7MB)
테스트 5 〉	통과 (6189.85ms, 10.7MB)
테스트 6 〉	통과 (2.16ms, 10.8MB)
테스트 7 〉	통과 (0.18ms, 10.8MB)
테스트 8 〉	통과 (0.21ms, 10.8MB)
테스트 9 〉	통과 (0.21ms, 10.7MB)
테스트 10 〉	통과 (0.27ms, 10.8MB)
테스트 11 〉	통과 (0.23ms, 10.7MB)

'''

