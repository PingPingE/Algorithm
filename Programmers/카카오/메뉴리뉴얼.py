'''
[문제]
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 스카피가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
스카피가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다.
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
'''
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    cnt = {c:defaultdict(int) for c in course} #{key: 메뉴 개수, value: {key: 조합, value: 해당 조합의 등장 횟수}}
    maxx_len = {c:0 for c in course} #key: 메뉴 개수, value: 해당 개수로 구성된 조합의 최대 등장 횟수
    for o in orders:
        o = sorted(o)#일관성을 위해 정렬
        for c in course:
            for comb in combinations(o,c):
                cnt[c][comb]+=1 #횟수 추가
                maxx_len[c] = max(maxx_len[c], cnt[c][comb]) #maxx_len 갱신
    ans = []
    for c in course:
        if maxx_len[c] >=2:#등장 횟수가 최소 2이상
            for f in filter(lambda x: cnt[c][x]==maxx_len[c], cnt[c]):
                ans.append(''.join(list(f)))
    return sorted(ans)

'''
정확성  테스트
테스트 1 〉	통과 (0.17ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.3MB)
테스트 3 〉	통과 (0.11ms, 10.2MB)
테스트 4 〉	통과 (0.17ms, 10.2MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (0.47ms, 10.2MB)
테스트 7 〉	통과 (0.49ms, 10.2MB)
테스트 8 〉	통과 (3.75ms, 10.3MB)
테스트 9 〉	통과 (2.58ms, 10.4MB)
테스트 10 〉	통과 (3.39ms, 10.6MB)
테스트 11 〉	통과 (1.94ms, 10.4MB)
테스트 12 〉	통과 (2.32ms, 10.6MB)
테스트 13 〉	통과 (2.36ms, 10.6MB)
테스트 14 〉	통과 (1.69ms, 10.4MB)
테스트 15 〉	통과 (3.11ms, 10.5MB)
테스트 16 〉	통과 (0.74ms, 10.3MB)
테스트 17 〉	통과 (0.51ms, 10.4MB)
테스트 18 〉	통과 (0.21ms, 10.3MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.64ms, 10.4MB)
'''
