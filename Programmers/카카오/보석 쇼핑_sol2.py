def solution(gems):
    answer = [1,len(gems)]
    dic = {i:0 for i in gems}
    pick = set()
    s,e = 0,0
    kind_n = len(dic)
    while e<=len(gems):
        if len(pick) == kind_n:
            if answer[1]-answer[0] > e-s-1:
                answer= [s+1, e]
            dic[gems[s]] -=1
            if dic[gems[s]] == 0:
                pick.remove(gems[s])
            s+=1
        else:
            try:
                dic[gems[e]] += 1
                if dic[gems[e]] == 1:
                    pick.add(gems[e])
            except:
                pass
            e+=1            
    return answer

'''
#시간초과 코드
def solution(gems):
    answer = [1,len(gems)]
    dic = {i:0 for i in set(gems)}
    #pick = set()
    s,e = 0,0
    while e<=len(gems):
        if 0 not in dic.values():
            if answer[1]-answer[0] > e-s-1:
                answer= [s+1, e]
            dic[gems[s]] -=1
            # if dic[gems[s]] == 0:
            #     pick.remove(gems[s])
            s+=1
        else:
            try:
                dic[gems[e]] += 1
                # if dic[gems[e]] == 1:
                #     pick.add(gems[e])
            except:
                pass
            e+=1            
    return answer

'''
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.10ms, 10.8MB)
테스트 3 〉	통과 (0.23ms, 10.8MB)
테스트 4 〉	통과 (0.27ms, 10.8MB)
테스트 5 〉	통과 (0.42ms, 10.8MB)
테스트 6 〉	통과 (0.04ms, 10.8MB)
테스트 7 〉	통과 (0.05ms, 10.8MB)
테스트 8 〉	통과 (0.39ms, 10.9MB)
테스트 9 〉	통과 (0.57ms, 10.9MB)
테스트 10 〉	통과 (0.45ms, 10.9MB)
테스트 11 〉	통과 (0.62ms, 11MB)
테스트 12 〉	통과 (0.95ms, 10.9MB)
테스트 13 〉	통과 (1.30ms, 11MB)
테스트 14 〉	통과 (1.17ms, 11.1MB)
테스트 15 〉	통과 (2.55ms, 11.3MB)
효율성  테스트
테스트 1 〉	통과 (3.20ms, 11.4MB)
테스트 2 〉	통과 (4.61ms, 15.4MB)
테스트 3 〉	통과 (9.58ms, 19.4MB)
테스트 4 〉	통과 (8.01ms, 23.3MB)
테스트 5 〉	통과 (16.68ms, 27.2MB)
테스트 6 〉	통과 (19.47ms, 31.2MB)
테스트 7 〉	통과 (24.08ms, 35.1MB)
테스트 8 〉	통과 (26.60ms, 39.1MB)
테스트 9 〉	통과 (30.01ms, 42.8MB)
테스트 10 〉	통과 (35.78ms, 48.2MB)
테스트 11 〉	통과 (39.03ms, 54.9MB)
테스트 12 〉	통과 (25.81ms, 62.8MB)
테스트 13 〉	통과 (36.65ms, 70.7MB)
테스트 14 〉	통과 (60.03ms, 78.9MB)
테스트 15 〉	통과 (61.09ms, 87.5MB)
'''