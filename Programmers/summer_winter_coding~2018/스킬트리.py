# 0. skill에서 모든 가능한 문자열 남기기(candi)
# 1. skill에 있는 문자만 남기기
# 2. candi에 1.이후 남은 문자열이 있는지 확인
import re

def solution(skill, skill_trees):
    candi = set([sk for sk in skill])
    ans = 0

    for n in range(1, len(skill) + 1):
        candi.add(skill[:n])

    candi.add('')

    for sk in skill_trees: a
    filtered_sk = re.sub(f"[^{skill}]", '', sk)
    if filtered_sk in candi:
        # print(filtered_sk, sk)
        ans += 1

return ans