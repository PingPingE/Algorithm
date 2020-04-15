from collections import deque
def solution(n, t, m, timetable):
    answer = ''
    T = {i: 0 for i in list(540 + j * t for j in range(n))}
    timetable.sort()
    que = deque()
    que.extend(timetable)
    time = 0
    while que:
        time = que.popleft().split(':')
        time = int(time[0]) * 60 + int(time[1])
        # 지각한 사람들만 있음 break
        if time > max(T.keys()):
            time = 0
            break
        # 마지막 타임 자리가 한자리밖에 없을 때
        if T[max(T.keys())] == m - 1:
            break
        for k, v in T.items():
            if time <= k and v < m:
                T[k] += 1
                if len(que) == 0:
                    time = 0
                break

    if time == 0:
        answer = max(T.keys())
    else:
        answer = time - 1

    return "{}:{}".format(str(answer // 60).zfill(2), str(answer % 60).zfill(2))
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))