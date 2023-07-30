'''
문제 설명)
n x m 격자 미로가 주어집니다. 당신은 미로의 (x, y)에서 출발해 (r, c)로 이동해서 탈출해야 합니다.
단, 미로를 탈출하는 조건이 세 가지 있습니다.
1. 격자의 바깥으로는 나갈 수 없습니다.
2. (x, y)에서 (r, c)까지 이동하는 거리가 총 k여야 합니다. 이때, (x, y)와 (r, c)격자를 포함해, 같은 격자를 두 번 이상 방문해도 됩니다.
3. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출해야 합니다.

이동 경로는 다음과 같이 문자열로 바꿀 수 있습니다.
l: 왼쪽으로 한 칸 이동
r: 오른쪽으로 한 칸 이동
u: 위쪽으로 한 칸 이동
d: 아래쪽으로 한 칸 이동

예를 들어, 왼쪽으로 한 칸, 위로 한 칸, 왼쪽으로 한 칸 움직였다면, 문자열 "lul"로 나타낼 수 있습니다.
미로에서는 인접한 상, 하, 좌, 우 격자로 한 칸씩 이동할 수 있습니다

격자의 크기를 뜻하는 정수 n, m, 출발 위치를 뜻하는 정수 x, y, 탈출 지점을 뜻하는 정수 r, c, 탈출까지 이동해야 하는 거리를 뜻하는 정수 k가 매개변수로 주어집니다.
이때, 미로를 탈출하기 위한 경로를 return 하도록 solution 함수를 완성해주세요.
단, 위 조건대로 미로를 탈출할 수 없는 경우 "impossible"을 return 해야 합니다.

제한사항)
2 ≤ n (= 미로의 세로 길이) ≤ 50
2 ≤ m (= 미로의 가로 길이) ≤ 50
1 ≤ x ≤ n
1 ≤ y ≤ m
1 ≤ r ≤ n
1 ≤ c ≤ m
(x, y) ≠ (r, c)
1 ≤ k ≤ 2,500
'''

#목적지 도착 여부 도착 후 남은 길이 검사 -> 시간 초과
from collections import deque
def solution2(n, m, x, y, r, c, k):
    answer = []
    que = deque([[x - 1, y - 1, '']])  # 현 위치,거쳐온 경로
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    d_map = {0: 'd', 1: 'u', 2: 'r', 3: 'l'}
    r_map = {0: 'u', 1: 'd', 2: 'l', 3: 'r'}

    # 남은 길이를 채울 경로 찾기
    rest_str = 'zz'
    for d in range(4):
        nx, ny = r - 1 + dx[d], c - 1 + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            rest_str = min(rest_str, d_map[d] + r_map[d])

    while que:
        cur_x, cur_y, path = que.popleft()
        # 도착했는지 검사
        if (cur_x, cur_y) == (r - 1, c - 1):
            rest_len = k - len(path)
            # 남은 길이가 0 or 짝수인 경우
            if rest_len % 2 == 0:
                answer.append(path + rest_str * (rest_len // 2))
                continue
            # 남은 길이가 홀수면 도달 못함
            else:
                continue
        elif len(path) >= k:
            continue

        for d in range(4):
            nx, ny = cur_x + dx[d], cur_y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                que.append([nx, ny, path + d_map[d]])

    return 'impossible' if not answer else sorted(answer)[0]

#k길이까지 도달했을 때 도착지 여부 검사 -> 시간 초과
def solution1(n, m, x, y, r, c, k):
    answer = 'z' * k
    que = deque([[x - 1, y - 1, '']])  # 현 위치,거쳐온 경로
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    d_map = {0: 'd', 1: 'u', 2: 'r', 3: 'l'}
    while que:
        cur_x, cur_y, path = que.popleft()
        #k 길이만큼의 경로 존재 시 체크
        if len(path) == k:
            if (cur_x, cur_y) == (r - 1, c - 1):
                answer = min(answer, path)
                continue
            else:
                continue

        for d in range(4):
            nx, ny = cur_x + dx[d], cur_y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                que.append([nx, ny, path + d_map[d]])

    return 'impossible' if answer.startswith('z') else answer

print(solution2(3,4,2,3,3,1,5))