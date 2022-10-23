'''
문제)
오늘은 직사각형 모양의 방을 로봇 청소기를 이용해 청소하려고 한다. 이 로봇 청소기는 유저가 직접 경로를 설정할 수 있다.
방은 크기가 1×1인 정사각형 칸으로 나누어져 있으며, 로봇 청소기의 크기도 1×1이다. 칸은 깨끗한 칸과 더러운 칸으로 나누어져 있으며,
로봇 청소기는 더러운 칸을 방문해서 깨끗한 칸으로 바꿀 수 있다.

일부 칸에는 가구가 놓여져 있고, 가구의 크기도 1×1이다. 로봇 청소기는 가구가 놓여진 칸으로 이동할 수 없다.
로봇은 한 번 움직일 때, 인접한 칸으로 이동할 수 있다. 또, 로봇은 같은 칸을 여러 번 방문할 수 있다.
방의 정보가 주어졌을 때, 더러운 칸을 모두 깨끗한 칸으로 만드는데 필요한 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.

입력)
입력은 여러 개의 테스트케이스로 이루어져 있다.
각 테스트 케이스의 첫째 줄에는 방의 가로 크기 w와 세로 크기 h가 주어진다. (1 ≤ w, h ≤ 20) 둘째 줄부터 h개의 줄에는 방의 정보가 주어진다.
방의 정보는 4가지 문자로만 이루어져 있으며, 각 문자의 의미는 다음과 같다.

.: 깨끗한 칸
*: 더러운 칸
x: 가구
o: 로봇 청소기의 시작 위치
더러운 칸의 개수는 10개를 넘지 않으며, 로봇 청소기의 개수는 항상 하나이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력)
각각의 테스트 케이스마다 더러운 칸을 모두 깨끗한 칸으로 바꾸는 이동 횟수의 최솟값을 한 줄에 하나씩 출력한다. 만약, 방문할 수 없는 더러운 칸이 존재하는 경우에는 -1을 출력한다.
'''
import sys
from itertools import permutations
from collections import deque, defaultdict
dy, dx= [0,0,1,-1], [1,-1,0,0]
INF= sys.maxsize
while True:
    w,h = map(int, input().split())
    if w+h == 0:
        break

    board = []
    dirty_spots = set()
    dist = {}
    start = ()
    ans = sys.maxsize

    for row in range(h):
        tmp = list(sys.stdin.readline())
        board.append(tmp)
        for col,spot in enumerate(tmp):
            if spot == '*':
                dirty_spots.add((row,col))  #dirty_spot <-> 각 key지점 사이의 최소 거리
            elif spot == 'o':
                start = (row,col)

    def get_dist(from_):
        global dist
        tmp_dist = [[INF]*w for _ in range(h)]
        y,x= from_
        que =deque([[y,x,0]])
        done =set([from_])
        while que:
            cur_y, cur_x, cnt= que.popleft()
            tmp_dist[cur_y][cur_x] = min(cnt, tmp_dist[cur_y][cur_x])

            for d in range(4):
                ny,nx = cur_y+dy[d], cur_x+dx[d]
                if 0<=ny<h and 0<=nx<w and board[ny][nx]!='x' and (ny,nx) not in done:
                    done.add((ny,nx))
                    que.append([ny,nx,cnt+1])
        dist[from_] = tmp_dist

    for r in range(h):
        for c in range(w):
            get_dist((r,c))

    for perm in permutations(dirty_spots, len(dirty_spots)):
        tmp_ans=0
        prev_y,prev_x= start
        for p in perm:
            y,x=p
            tmp_ans += dist[(prev_y,prev_x)][y][x]
            prev_y,prev_x= y,x
        ans = min(ans, tmp_ans)

    print(ans if ans != sys.maxsize else -1)