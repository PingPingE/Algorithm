from collections import deque, defaultdict
def solution(board, r, c):
    INF = 987654321
    dic = defaultdict(list)
    que = deque()
    ans = INF
    dy, dx = [0, 0, 1, -1], [-1, 1, 0, 0]

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                dic[board[i][j]].append((i, j))

    # rc1 -> rc2로 가는 최단거리
    def get_count(rc1, rc2, remain):
        m_que = deque([[rc1, 0]])
        done = set([rc1])
        cnt = INF
        while m_que:
            rc, tmp_cnt = m_que.popleft()
            if rc == rc2:
                cnt = min(tmp_cnt, cnt)
                continue

            if tmp_cnt >= cnt:
                continue

            for d in range(4):
                ny, nx = rc[0] + dy[d], rc[1] + dx[d]
                if ny < 0 or nx < 0 or ny > 3 or nx > 3: continue
                # 그냥 해당 방향으로 한칸 이동
                if (ny, nx) not in done:
                    done.add((ny, nx))
                    m_que.append([(ny, nx), tmp_cnt + 1])

                # 컨트롤 + 방향키 이동(카드가 처음 나오는 칸까지 or 마지막 칸까지)
                cy, cx = ny, nx
                while board[cy][cx] not in remain:
                    if 0 <= cy + dy[d] < 4 and 0 <= cx + dx[d] < 4:
                        cy += dy[d]
                        cx += dx[d]
                    else:
                        break

                if (cy, cx) in done:
                    continue
                done.add((cy, cx))
                m_que.append([(cy, cx), tmp_cnt + 1])
        return cnt

    que.append([(r, c), 0, set(dic.keys())])
    while que:
        rc, cnt, remain = que.popleft()
        # print(rc, cnt, remain)
        if not remain:
            ans = min(ans, cnt)
            continue

        if cnt >= ans:
            continue

        # 어느 카드부터 짝 맞출지
        for k in remain:
            v1 = dic[k][0]
            v2 = dic[k][1]
            #=====지금껏 틀린 이유: 도착점(다음 rc)을 잘못 넣음....  (rc -> v1 -> v2 순으로 가놓고 도착점을 v2가 아닌 v1으로 해놓음)
            que.append([v2, cnt + get_count(rc, v1, remain) + get_count(v1, v2, remain) + 2, remain - {k}])
            que.append([v1, cnt + get_count(rc, v2, remain) + get_count(v2, v1, remain) + 2, remain - {k}])

    return ans

'''
정확성  테스트
테스트 1 〉	통과 (3.31ms, 10.2MB)
테스트 2 〉	통과 (2.93ms, 10.3MB)
테스트 3 〉	통과 (3.30ms, 10.3MB)
테스트 4 〉	통과 (2.71ms, 10.3MB)
테스트 5 〉	통과 (23.00ms, 10.3MB)
테스트 6 〉	통과 (21.81ms, 10.3MB)
테스트 7 〉	통과 (27.75ms, 10.4MB)
테스트 8 〉	통과 (25.48ms, 10.2MB)
테스트 9 〉	통과 (248.70ms, 11.2MB)
테스트 10 〉	통과 (259.57ms, 11.1MB)
테스트 11 〉	통과 (225.13ms, 11.2MB)
테스트 12 〉	통과 (236.59ms, 11.2MB)
테스트 13 〉	통과 (3040.68ms, 24.6MB)
테스트 14 〉	통과 (3305.43ms, 24.6MB)
테스트 15 〉	통과 (2619.73ms, 24.6MB)
테스트 16 〉	통과 (3121.31ms, 24.5MB)
테스트 17 〉	통과 (0.13ms, 10.2MB)
테스트 18 〉	통과 (0.07ms, 10.2MB)
테스트 19 〉	통과 (0.62ms, 10.2MB)
테스트 20 〉	통과 (0.48ms, 10.3MB)
테스트 21 〉	통과 (19.52ms, 10.3MB)
테스트 22 〉	통과 (3462.06ms, 24.6MB)
테스트 23 〉	통과 (3192.93ms, 24.5MB)
테스트 24 〉	통과 (27.22ms, 10.2MB)
테스트 25 〉	통과 (3406.72ms, 24.6MB)
테스트 26 〉	통과 (25.30ms, 10.2MB)
테스트 27 〉	통과 (27.75ms, 10.3MB)
테스트 28 〉	통과 (3.76ms, 10.2MB)
테스트 29 〉	통과 (3.10ms, 10.3MB)
테스트 30 〉	통과 (3.10ms, 10.2MB)
'''


#삽질 기록=============
from collections import deque, defaultdict
def solution(board, r, c):
    INF = 987654321
    dic = defaultdict(list)
    que = deque()
    ans = INF

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                dic[board[i][j]].append((i, j))

    len_dic = len(dic)

    def move_col(rc1, rc2, remain):  # 좌우
        diff = rc2[1] - rc1[1]
        if diff==0:
            return 0
        r = rc1[0]
        if diff < 0:  # 좌
            for c in range(rc1[1]-1, rc2[1], -1):
                if board[r][c] in remain:
                    return 1+move_col((r,c),rc2,remain)
            else:
                if rc2[1] >0 and board[r][rc2[1]] == 0:
                    return abs(diff)
                return 1 #끝까지 갔거나, 카드가 있는 경우는 컨트롤 사용 가능

        else:  # 우
            for c in range(rc1[1]+1, rc2[1]):
                if board[r][c] in remain:
                    return 1+move_col((r,c),rc2,remain)
            else:
                if rc2[1] <3 and board[r][rc2[1]] ==0:
                    return abs(diff)
                return 1


    def move_row(rc1, rc2,remain):  # 상하
        diff = rc2[0] - rc1[0]
        if diff==0:
            return 0
        c = rc1[1]
        if diff < 0:  # 상
            for r in range(rc1[0]-1, rc2[0], -1):
                if board[r][c] in remain:
                    return 1+move_row((r,c), rc2,remain)
            else:
                if rc2[0] >0 and board[rc2[0]][c] ==0:
                    return abs(diff)
                return 1

        else:  # 하
            for r in range(rc1[0]+1, rc2[0]):
                if board[r][c] in remain:
                    return 1+move_row((r,c), rc2,remain)
            else:
                if rc2[0] < 3 and board[rc2[0]][c] ==0:
                    return abs(diff)
                return 1

    def get_count(rc1, rc2, remain):
        if rc1 == rc2:
            return 0
        #상하 -> 좌우
        tmp1 = (rc2[0],rc1[1])
        cnt1 = move_row(rc1, tmp1, remain)+move_col(tmp1,rc2,remain)

        #좌우 -> 상하
        tmp2 = (rc1[0],rc2[1])
        cnt2 = move_col(rc1, tmp2,remain)+move_row(tmp2,rc2,remain)

        return min(cnt1,cnt2)

    que.append([(r, c), 0, set(dic.keys())])
    while que:
        rc, cnt, remain = que.popleft()
        if not remain:
            ans = min(ans, cnt)
            continue

        if cnt >= ans:
            continue

        for k in remain:
            v1 = dic[k][0]
            v2 = dic[k][1]
            que.append([v1, cnt + get_count(rc, v1, remain-{k}) + get_count(v1, v2, remain-{k}), remain - {k}])
            que.append([v2, cnt + get_count(rc, v2, remain-{k}) + get_count(v2, v1, remain-{k}), remain - {k}])

    return ans + len_dic * 2