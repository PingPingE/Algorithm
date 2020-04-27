#sol2) 정규식을 활용한 짧은 코드
import re
from collections import Counter
def solution(s):
    m = Counter(re.findall("[0-9]+",s))
    return list(map(int, sorted(m.keys(), reverse = True, key = lambda x: m[x])))

# sol1) split을 활용한 노가다? 코드
def solution(s):
    answer = []
    s.split('"')
    s = s.split("{{")[1]
    s = s.split("}}")[0]
    s = s.split("},{")
    for ss in s:
        s_set = set()
        s_set.update(map(int, ss.split(',')))
        answer.append(s_set)
    answer.sort()
    ans = list()
    ans.extend(answer[0])
    for a in range(1,len(answer)):
        ans.extend(answer[a]-answer[a-1])
    return ans