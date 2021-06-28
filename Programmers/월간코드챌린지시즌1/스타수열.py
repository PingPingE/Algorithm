#틀린 코드
from collections import deque
def solution(a):
    answer = 0
    que = deque()
    for i in a:
        que.append([i, None, None, 1, 1])
    while que:
        #idx로 순서대로 보니까 부분수열 조건 만족
        #prev1,prev2로 이전 집합의 원소 확인
        #inter로 교집합 원소 확인
        prev1, prev2, inter, cnt, idx = que.popleft()
        # print(prev1, prev2, inter, cnt, idx)
        
        if cnt % 2 == 0:
            answer = max(answer, cnt)

            for i in range(idx, len(a)):
                if a[i] in [prev1, prev2]:
                    que.append([a[i], None, inter, cnt + 1, i + 1])
                    continue
        else:
            #먼저 들어온 prev1이 교집합 원소와 같은 경우
            if inter == prev1:
                for i in range(idx, len(a)):
                    if a[i] != prev1:
                        que.append([prev1, a[i], inter, cnt + 1, i + 1])
                        continue
                        
            #교집합 원소가 없는 경우(시작)
            elif inter == None:
                for i in range(idx, len(a)):
                    if a[i] != prev1:
                        que.append([prev1, a[i], prev1, cnt + 1, i + 1])
                        que.append([prev1, a[i], a[i], cnt + 1, i + 1])
                        continue
                        
            #이번에 교집합 원소와 같은 값을 넣어야 하는 경우
            else:
                for i in range(idx, len(a)):
                    if a[i] == inter:
                        que.append([prev1, a[i], inter, cnt + 1, i + 1])
                        continue

    return answer
