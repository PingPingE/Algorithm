from collections import deque
def solution(queue1, queue2):
    s_q1, s_q2 = sum(queue1), sum(queue2)
    max_n = max(max(queue1), max(queue2))
    N = s_q1 + s_q2

    #똑같은 구성으로 계속 반복되는지 체크를 해야하는데
    #일일이 다 기록하기에는 너무 방대한 양이라 limit을 두는 것으로 ㄱㄱ
    cnt_limit = len(queue1) * 4
    cnt = 0
    M = N // 2

    if N % 2 == 0 and max_n <= M:
        q1, q2 = deque(queue1), deque(queue2)
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
            if cnt > cnt_limit:
                return -1

        return cnt
    else:
        return -1
