#도전중============================
#T1: 9분
#T2: 20분 36초(11분 36초)
#T3: 30분 40초 ~
from collections import defaultdict
def solution(n, results):
    if n==1: return 1
    win_res = defaultdict(set)
    lose_res = defaultdict(set)
    for win,lose in results:
        win_res[win].add(lose)
        lose_res[lose].add(win)
        
    print("lose:",lose_res)
    print("win:", win_res)
    #이긴거 
    for k,v in list(win_res.items()):
        add_set =set()
        for vv in v: #k한테 지는 선수들이 이긴 선수 추가
            add_set.update(win_res[vv])
        win_res[k].update(add_set)
    
    #진거
    for k,v in list(lose_res.items()):
        add_set = set()
        for vv in v: #k를 이기는 선수들이 지는 선수 추가
            add_set.update(lose_res[vv])
        lose_res[k].update(add_set)
        
    print("lose:",lose_res)
    print("win:", win_res)
    
    return len(list(filter(lambda x: len(win_res[x]|lose_res[x]) == n-1, list(range(1,n+1)))))
'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	실패 (0.07ms, 10.3MB) -
테스트 3 〉	통과 (0.13ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.83ms, 10.3MB)
테스트 6 〉	통과 (1.34ms, 10.4MB)
테스트 7 〉	실패 (4.69ms, 10.6MB) -
테스트 8 〉	실패 (5.71ms, 10.9MB) -
테스트 9 〉	실패 (7.40ms, 11.4MB) -
테스트 10 〉	통과 (8.49ms, 11.4MB)
'''