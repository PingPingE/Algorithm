'''
문제 설명)
다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.
rect_1.png
지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.
만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.
즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.
다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.
한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.
지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때,
캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.


제한사항)
rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
itemX, itemY는 1 이상 50 이하인 자연수입니다.
지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.
전체 배점의 50%는 직사각형이 1개인 경우입니다.
전체 배점의 25%는 직사각형이 2개인 경우입니다.
전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.

'''
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    N = 51
    answer = N * N
    board = [[0] * N for _ in range(N)]

    def fill(x1, y1, x2, y2):
        nonlocal board
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    for a1, a2, a3, a4 in rectangle:
        fill(a1, a2, a3, a4)

    # 테두리만 남기기
    dy, dx = [0, 0, 1, -1, -1, -1, 1, 1], [1, -1, 0, 0, -1, 1, -1, 1]
    remove_targets = set()
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cnt = 0
                for d in range(8):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                        cnt += 1
                if cnt == 8:
                    remove_targets.add((x, y))
    for x, y in remove_targets:
        board[x][y] = 0

    # char -> item
    que = deque([[characterX, characterY, 0]])
    done = set([characterX, characterY])

    print(characterX, characterY, itemX, itemY)
    while que:
        x, y, cnt = que.popleft()
        if cnt >= answer: continue
        if x == itemX and y == itemY:
            answer = cnt
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in done and board[nx][ny]:
                que.append([nx, ny, cnt + 1])
                done.add((nx, ny))

    for b in board[:10]:
        print(b[:10])
    return answer

#움푹파인 곳이 한칸일때 코너와 겹쳐져서 표현이 안됨 / 표현이 되어도 최소 거리를 구할 때 정상적인 루트로 가지 않게 됨
#전자 케이스
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))

#후자 케이스
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
