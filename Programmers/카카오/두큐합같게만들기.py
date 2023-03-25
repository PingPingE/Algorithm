from collections import deque
def solution(queue1, queue2):
    answer = -1
    N = sum(queue1) + sum(queue2)

    if N % 2 == 0:
        M = N // 2
        que = deque([[queue1, queue2, 0]])
        done = set()
        done.add(f"{sorted(queue1)}")
        done.add(f"{sorted(queue2)}")
        while que:
            q1, q2, n = que.popleft()
            if sum(q1) == M:
                if answer == -1:
                    answer = n
                else:
                    answer = min(n, answer)
                continue

            try:
                t1 = q1[1:]
                t2 = q2[:] + [q1[0]]
                if f"{sorted(t2)}" not in done:
                    que.append([q1[1:], q2[:] + [q1[0]], n + 1])
                    done.add(f"{sorted(t2)}")
            except:
                pass
            try:
                t1 = q1[:]+[q2[0]]
                t2 = q2[1:]
                if f"{sorted(t1)}" not in done:
                    que.append([q1[:]+[q2[0]], q2[1:], n + 1])
                    done.add(f"{sorted(t1)}")
            except:
                pass
    return answer

print(solution([3, 2, 7, 2]	, [4, 6, 5, 1]))