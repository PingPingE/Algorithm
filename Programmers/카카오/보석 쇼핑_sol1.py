#C++로 구현한 방식 그대로 옮겨서 실행하면 시간초과남(효율성13번)
def solution(gems):
    zero =set(gems)#종류 카운트 겸 현재 개수가 0개인거 담는 용도
    jew_map = {i:e for e,i in enumerate(zero)}#인덱싱
    goal = len(jew_map)
    jew = [0 for _ in range(goal)] #종류별 개수
    total= len(gems)
    minn = [0,total] #시작인덱스, 길이
    s,e=0,0
    stat = False
    while s<=e and e<len(gems):
        if total-s <goal or minn[1]==goal: #볼 필요없음
            break
        if e-s >=minn[1]: #구간을 줄여야함
            jew[jew_map[gems[s]]] -= 1
            if jew[jew_map[gems[s]]] == 0:
                zero.add(gems[s])
                stat = False
            s+=1
            continue
        if stat: #기존에 if 0 not in jew로 했을 땐 시간초과...
            #최소니?
            if e-s < minn[1]:
                minn =[s,e-s]
            #먼저 시작하니?
            elif e-s == minn[1] and s<minn[0]:
                minn[0]=s
            
            #구간을 줄임
            jew[jew_map[gems[s]]] -=1
            if jew[jew_map[gems[s]]] == 0:
                zero.add(gems[s])
                stat = False
            s +=1
        else:
            #구간을 늘임
            jew[jew_map[gems[e]]] += 1
            
            if gems[e] in zero:
                zero.remove(gems[e])
                if len(zero) == 0:
                    stat = True
            e += 1
            
    return [minn[0]+1, minn[0]+minn[1]]

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.8MB)
테스트 2 〉	통과 (0.11ms, 10.8MB)
테스트 3 〉	통과 (0.27ms, 10.7MB)
테스트 4 〉	통과 (0.14ms, 10.9MB)
테스트 5 〉	통과 (0.05ms, 10.9MB)
테스트 6 〉	통과 (0.47ms, 10.8MB)
테스트 7 〉	통과 (0.49ms, 10.8MB)
테스트 8 〉	통과 (0.58ms, 10.8MB)
테스트 9 〉	통과 (0.66ms, 10.9MB)
테스트 10 〉	통과 (0.58ms, 10.9MB)
테스트 11 〉	통과 (0.74ms, 11MB)
테스트 12 〉	통과 (1.08ms, 10.9MB)
테스트 13 〉	통과 (1.50ms, 11.1MB)
테스트 14 〉	통과 (1.53ms, 11.3MB)
테스트 15 〉	통과 (2.94ms, 11.2MB)
효율성  테스트
테스트 1 〉	통과 (3.86ms, 11.4MB)
테스트 2 〉	통과 (6.25ms, 15.2MB)
테스트 3 〉	통과 (11.35ms, 19.3MB)
테스트 4 〉	통과 (10.04ms, 23.3MB)
테스트 5 〉	통과 (19.46ms, 27.2MB)
테스트 6 〉	통과 (22.43ms, 31.2MB)
테스트 7 〉	통과 (27.48ms, 35.1MB)
테스트 8 〉	통과 (30.07ms, 39.1MB)
테스트 9 〉	통과 (33.98ms, 44MB)
테스트 10 〉	통과 (37.65ms, 47.7MB)
테스트 11 〉	통과 (45.36ms, 55MB)
테스트 12 〉	통과 (36.09ms, 62.7MB)
테스트 13 〉	통과 (47.86ms, 72.7MB)
테스트 14 〉	통과 (67.13ms, 80.3MB)
테스트 15 〉	통과 (74.24ms, 88MB)
'''