'''
스타트링크가 "스타트 택시"라는 이름의 택시 사업을 시작했다. 스타트 택시는 특이하게도 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다.

택시 기사 최백준은 오늘 M명의 승객을 태우는 것이 목표이다. 백준이 활동할 영역은 N×N 크기의 격자로 나타낼 수 있고, 각 칸은 비어 있거나 벽이 놓여 있다.
택시가 빈칸에 있을 때, 상하좌우로 인접한 빈칸 중 하나로 이동할 수 있다. 알고리즘 경력이 많은 백준은 특정 위치로 이동할 때 항상 최단경로로만 이동한다.

M명의 승객은 빈칸 중 하나에 서 있으며, 다른 빈칸 중 하나로 이동하려고 한다. 여러 승객이 같이 탑승하는 경우는 없다. 따라서 백준은 한 승객을 태워 목적지로
이동시키는 일을 M번 반복해야 한다. 각 승객은 스스로 움직이지 않으며, 출발지에서만 택시에 탈 수 있고, 목적지에서만 택시에서 내릴 수 있다.

백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을,
그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다. 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이다. 연료는 한 칸 이동할 때마다 1만큼 소모된다.
한 승객을 목적지로 성공적으로 이동시키면, 그 승객을 태워 이동하면서 소모한 연료 양의 두 배가 충전된다. 이동하는 도중에 연료가 바닥나면 이동에 실패하고, 그 날의 업무가 끝난다.
승객을 목적지로 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.

모든 승객을 성공적으로 데려다줄 수 있는지 알아내고, 데려다줄 수 있을 경우 최종적으로 남는 연료의 양을 출력하는 프로그램을 작성하시오.

입력
첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000) 연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.

다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.

다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.

그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다. 모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

출력
모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다. 단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다. 모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
'''
#124260kb	332ms
import sys
from collections import deque
def pick():
    global taxi,fuel
    que = deque()
    que.append((taxi[0], taxi[1], fuel)) #현위치, 현연료
    done =set()
    done.add((taxi[0],taxi[1]))
    candi =[-1,-1,-987654321]
    while que:
        y,x,cur = que.popleft()
        if (y,x) in passengers: #해당위치에 승객 있니?
            if candi[0] == -1:
                candi = [y,x,cur]
                continue
            if cur == candi[-1]: #연료 같
                if y<candi[0]: #행비교
                    candi = [y,x,cur]
                    continue
                elif y==candi[0]:
                    if x<candi[1]:#열비교
                        candi=[y,x,cur]
                        continue
                    else:
                        continue
                else:
                    continue
        if cur <= 0: break
        for d in range(4):
            ny,nx = y+dy[d] , x+dx[d]
            if ny<0 or nx<0 or ny>=N or nx>=N or board[ny][nx] == 1 or (ny,nx) in done:
                continue
            done.add((ny,nx))
            que.append((ny,nx,cur-1))
    if candi[0] != -1:
        taxi = (candi[0], candi[1])
        fuel = candi[-1]
        goal = passengers[(candi[0], candi[1])]
        passengers.pop((candi[0], candi[1]))
        return goal
    return None

def go_dest(dest):#목적지로 가기
    global fuel,taxi
    que = deque()
    done =set()
    done.add((taxi[0], taxi[1]))
    que.append((taxi[0],taxi[1],0))
    while que:
        y,x,cur = que.popleft()
        if (y,x) == dest:
            if cur <= fuel:#fuel, taxi위치 갱신
                fuel += cur
                taxi = (y,x)
            else:
                fuel -= cur
            return True
        for d in range(4):
            ny,nx = y+dy[d],x+dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or board[ny][nx] == 1 or (ny, nx) in done:
                continue
            done.add((ny,nx))
            que.append((ny,nx,cur+1))
    return False

dy= [-1,1,0,0]
dx= [0,0,-1,1]
N,M,fuel = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi = list(map(lambda x:int(x)-1, input().split()))
passengers = {}
for _ in range(M):
    tmp = list(map(lambda x:int(x)-1, sys.stdin.readline().split()))
    passengers[(tmp[0],tmp[1])] = (tmp[2],tmp[3])
ret = -1
stat = False
while M:
    M-=1
    goal = pick()
    if goal:
        res = go_dest(goal)
        if fuel <0 or not res:
            stat = True
            break
    else:
        stat = True
        break
print(-1 if stat else fuel)

