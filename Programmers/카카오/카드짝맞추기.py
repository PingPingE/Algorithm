#시도 중
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
            else:#컨트롤 + 방향키로 한 번에
                return 1

        else:  # 우
            for c in range(rc1[1]+1, rc2[1]):
                if board[r][c] in remain:
                    return 1+move_col((r,c),rc2,remain)
            else:#컨트롤 + 방향키로 한 번에
                return 1


    def move_row(rc1, rc2,remain):  # 상하
        diff = rc2[0] - rc1[0]
        if diff==0:
            return 0
        c = rc1[1]
        if diff < 0:  # 하
            for r in range(rc1[0]-1, rc2[0], -1):
                if board[r][c] in remain:
                    return 1+move_row((r,c), rc2,remain)
            else:#컨트롤 + 방향키로 한 번에
                return 1

        else:  # 상
            for r in range(rc1[0]+1, rc2[0]):
                if board[r][c] in remain:
                    return 1+move_row((r,c), rc2,remain)
            else:#컨트롤 + 방향키로 한 번에
                return 1

    def get_count(rc1, rc2, remain):
        print("from:",rc1, "    to:", rc2, "remain:", remain)
        if rc1 == rc2:
            return 0
        #상하 -> 좌우
        tmp1 = (rc2[0],rc1[1])
        cnt1 = move_row(rc1, tmp1, remain)+move_col(tmp1,rc2,remain)
        print("상하 -> 좌우: ", cnt1)
        #좌우 -> 상하
        tmp2 = (rc1[0],rc2[1])
        cnt2 = move_col(rc1, tmp2,remain)+move_row(tmp2,rc2,remain)
        print("좌우 -> 상하: ", cnt2)

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
            que.append([v1, cnt + get_count(rc, v1, remain - {k}) + get_count(v1, v2, remain - {k}), remain - {k}])
            que.append([v2, cnt + get_count(rc, v2, remain - {k}) + get_count(v2, v1, remain - {k}), remain - {k}])

    return ans + len_dic * 2
