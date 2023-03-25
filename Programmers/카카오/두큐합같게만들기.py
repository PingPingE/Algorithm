from collections import deque
def solution(queue1, queue2):
    s_q1, s_q2 = sum(queue1), sum(queue2)
    N = s_q1 + s_q2
    cnt = 0
    #구성이 같은지도 봐야할것 같은데
    if N % 2 == 0:
        q1, q2 = deque(queue1), deque(queue2)
        M = N // 2
        while s_q1 != M:
            if s_q1 < M:
                q2_pop = q2.popleft()
                q1.append(q2_pop)
                s_q1 += q2_pop
                s_q2 -= q2_pop
                cnt += 1
            else:
                q1_pop = q1.popleft()
                q2.append(q1_pop)
                s_q1 -= q1_pop
                s_q2 += q1_pop
                cnt += 1

            if not q1 or not q2:
                return -1

        return cnt
    else:
        return -1
