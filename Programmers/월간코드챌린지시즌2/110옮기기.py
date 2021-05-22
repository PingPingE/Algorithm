from collections import deque
def solution(s):
    answer = []
    for target in s:
        if len(target) <= 3:
            answer.append(target)
            continue
        done=set()
        while target[:] not in done:
            que=deque()
            done.add(target[:])
            #왼 <- 오
            for e in range(len(target),2,-1):
                if target[e-3:e] == '110':
                    end=e-4
                    break
                else:
                    que.appendleft(target[e-1])

            else:#110이 없으면
                que.extend(target[:2])
                break

            #왼쪽으로 가면서 0찾기
            for j in range(end,-1,-1):
                if target[j]=='0':
                    que.extendleft('011')
                    que.extendleft(target[:j+1])
                    break
                else:
                    que.appendleft(target[j])
            else:
                que.extendleft('011')
            target = ''.join(que)

        answer.append(target)
    return answer