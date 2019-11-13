from collections import deque
def solution(N, stages):
    answer = deque()
    # 각 [스테이지별 현재 플레이어 수, 지나간or현재 플레이어수]
    m = {i: [0, 0] for i in range(1, N + 2)}
    for j in stages:
        # 현 플레이어 수 +1
        m[j][0] += 1
        for k in range(j, 0, -1):
            # 전체 플레이어 수 +1
            m[k][1] += 1
    del(m[N+1])
    #실패율 계산
    for k, v in m.items():
        if v[0]==0 or v[1] == 0:
            m[k] = 0
            continue
        m[k] = v[0]/v[1]

    for k,v in m.items():
        if len(answer) == 0:
            answer.append(k)
            continue
        if m[answer[0]] < v:
            answer.appendleft(k)
        else:
            stat = False
            for h in range(0,len(answer)):
                if m[answer[h]] < v:
                    answer.insert(h,k)
                    stat = True
                    break
                elif m[answer[h]] == v:
                    if k < answer[h]:
                        answer.insert(h,k)
                        stat = True
                        break
            if stat is False:
                answer.append(k)
    return list(answer)

# def solution(N, stages):
#     answer = {}
#     cnt = len(stages)
#     for s in range(1,N+1):
#         if cnt > 0 :
#             tmp = stages.count(s)
#             answer[s] = tmp/cnt
#             cnt -= tmp
#         else:
#             answer[s] = 0
#     answer = sorted(answer, key = lambda x: answer[x], reverse = True)
#     return answer
# # 만약에 1,2,3이 모두 같은 실패율을 가졌으면, key = lamda x: answer[x] -> 이부분에서 오름차순으로 1,2,3 이렇게 정렬이 되고, 한묶음이 됨
# #reverse = True를 통해 한묶음으로 내림차순 정렬이 되는 것임 ex) before 12345 -> after 54123 ---> 123은 한 묶음이 돼버렸음
print(solution(5,[1,2,3,4,5,5,3,6,4,3,5,5,2]))

#def solution(N, stages):
    # answer = []
    # #각 스테이지의 실패율(초기: 0)
    # m = {i:0 for i in range(1,N+2)}
    # #각각의 n번째 칸은 n번째 스테이지에 도달한 플레이어 수
    # tmp = [0 for _ in range(N+2)]
    # for s in stages:
    #     for t in range(1,s+1):
    #         tmp[t] += 1
    #
    # for i in range(1,N+1):
    #     if tmp[i] == 0:
    #         continue
    #     m[i] = stages.count(i)/tmp[i]
    # m.pop(N+1)
    # answer = sorted(m.keys(), reverse= True,key= lambda x: m[x])
    # return answer

