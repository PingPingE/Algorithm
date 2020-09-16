'''
문제)
 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.
뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

입력)
첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.
게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력)
첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
'''
#122540kb	184ms -> move함수X
#122536kb	208ms -> move함수
def move(timelimit):
    global time,apple,cur_yx
    if timelimit>=0:
        while time < timelimit:
            time += 1
            y, x = cur_yx[-1]
            ny, nx = y + d_map[cur_d][0], x + d_map[cur_d][1]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or (ny, nx) in cur_yx:  # 벽 or 자기자신에 부딛힌 경우
                return True
            cur_yx.append((ny, nx))
            if (ny, nx) in apple:  # 사과가 있으면
                apple.remove((ny, nx))
            else:
                cur_yx.popleft()  # 없으면 꼬리 쪽 없애기
    else:
        while True:
            time += 1
            y, x = cur_yx[-1]
            ny, nx = y + d_map[cur_d][0], x + d_map[cur_d][1]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or (ny, nx) in cur_yx:  # 벽 or 자기자신에 부딛힌 경우
                return True
            cur_yx.append((ny, nx))
            if (ny, nx) in apple:  # 사과가 있으면
                apple.remove((ny, nx))
            else:
                cur_yx.popleft()  # 없으면 꼬리 쪽 없애기
    return False
from collections import deque
N = int(input())
K = int(input())
apple = set() #사과가 놓인 곳
for _ in range(K):
    i, j =map(int, input().split())
    apple.add((i-1,j-1))
L = int(input())
time = 0 #현 시각(초)
cur_yx, cur_d= deque(),'D' # 'D' #뱀이 있는 곳, 방향
cur_yx.append((0,0))
d_map ={'D':[0,1], 'L':[0,-1],'U':[-1,0], 'DD':[1,0]} #우좌상하
rev_D = {'D':'DD', 'L':'U', 'U':'D','DD':'L'} #각 방향에서 오른쪽으로 90도 회전 시 갱신된 방향
rev_L = {'D':'U','L':'DD','U':'L','DD':'D'}#각 방향에서 왼쪽으로 90도 회전 시 갱신된 방향
que =deque()
for _ in range(L):
    X,C = map(str, input().split()) #게임 시작 X초 후 이동 방향은 C (L:왼, D:오)로 90도 회전
    X = int(X)
    que.append((X,C))
stat = False
while que:
    X, C = que.popleft()
    stat= move(X)
    if stat: break
    if C == 'L':
        cur_d = rev_L[cur_d]
    else:
        cur_d = rev_D[cur_d]
if stat^1: move(-1)
print(time)