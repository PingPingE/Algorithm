def solution(arrows):
    answer = 0
    # 상 / 우상 / 우 / 우하 / 하/ 좌하 / 좌 / 좌상
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    all_yx = []
    cur_yx = (0, 0)

    # 1. 모든 좌표를 구한다
    for d in arrows:
        y, x = cur_yx
        ny, nx = y + dy[d], x + dx[d]
        all_yx.append((ny, nx))
        cur_yx = (ny, nx)

    return answer

#답: 3
print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))