def solution(gems):
    answer = [1,len(gems)]
    dic = {i:0 for i in gems}
    pick = set()
    s,e = 0,0
    while e<=len(gems):
        if len(pick) == len(dic):
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
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.7MB)
테스트 2 〉	통과 (0.10ms, 10.8MB)
테스트 3 〉	통과 (0.25ms, 10.6MB)
테스트 4 〉	통과 (0.29ms, 10.8MB)
테스트 5 〉	통과 (0.47ms, 10.8MB)
테스트 6 〉	통과 (0.05ms, 10.7MB)
테스트 7 〉	통과 (0.05ms, 10.7MB)
테스트 8 〉	통과 (0.42ms, 11MB)
테스트 9 〉	통과 (0.59ms, 10.8MB)
테스트 10 〉	통과 (0.49ms, 10.9MB)
테스트 11 〉	통과 (0.69ms, 11MB)
테스트 12 〉	통과 (1.00ms, 11MB)
테스트 13 〉	통과 (1.35ms, 11MB)
테스트 14 〉	통과 (1.32ms, 11.2MB)
테스트 15 〉	통과 (2.76ms, 11.1MB)
효율성  테스트
테스트 1 〉	통과 (3.38ms, 11.4MB)
테스트 2 〉	통과 (5.54ms, 15.3MB)
테스트 3 〉	통과 (11.10ms, 19.3MB)
테스트 4 〉	통과 (8.73ms, 23.3MB)
테스트 5 〉	통과 (19.15ms, 27.2MB)
테스트 6 〉	통과 (21.68ms, 31.2MB)
테스트 7 〉	통과 (26.04ms, 35.2MB)
테스트 8 〉	통과 (29.98ms, 39MB)
테스트 9 〉	통과 (35.22ms, 42.8MB)
테스트 10 〉	통과 (39.43ms, 46.9MB)
테스트 11 〉	통과 (44.41ms, 55MB)
테스트 12 〉	통과 (29.66ms, 64.7MB)
테스트 13 〉	통과 (40.94ms, 70.7MB)
테스트 14 〉	통과 (70.39ms, 79.3MB)
테스트 15 〉	통과 (69.62ms, 87.9MB)
'''