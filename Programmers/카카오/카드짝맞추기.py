# 시도 중
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
            que.append([v1, cnt + get_count(rc, v1, remain) + get_count(v1, v2, remain) + 2, remain - {k}])
            que.append([v2, cnt + get_count(rc, v2, remain) + get_count(v2, v1, remain) + 2, remain - {k}])

    return ans
print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
# print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
# print(solution(	[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1, 1))


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