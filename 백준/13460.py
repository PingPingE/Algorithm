'''
문제
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.
이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
'''
#127212kb	220ms
from collections import deque
N,M=map(int, input().split())
board=[]
red,blue=(0,0),(0,0) #빨간 구슬과 파란 구슬은 위치 따로 저장
dy,dx=[-1,1,0,0],[0,0,-1,1]
for _ in range(N):
    tmp = list(input())
    for e,t in enumerate(tmp):
        if t=='R':
            red=(_,e)
            tmp[e]='.'
        elif t=='B':
            blue=(_,e)
            tmp[e]='.'
    board.append(tmp)

def move(rc,d):#시작 지점, 방향
    y,x=rc
    while board[y][x]=='.':
        nr,nc=y+dy[d], x+dx[d]
        if nr<0 or nc<0 or nr>=N or nc>=M or board[nr][nc]=='#':
            break
        y,x=nr,nc
    return (y,x)

def is_goal(rc):#goal에 도착했는지
    if board[rc[0]][rc[1]]=='O':
        return True
    return False

def get_distance(from_, to_):#두 구슬이 만났을 때
    y= abs(from_[0]-to_[0])
    x= abs(from_[1]-to_[1])
    return y+x

que=deque([[red,blue,0]])
done=set([(red,blue)]) #====틀렸던 이유1: red와 blue가 각각 따로 done_r, done_b를 가졌었다. -> 그게 아니라 둘의 위치를 같이 체크해야했다
stat=True
while que and stat:
    r,b,cnt=que.popleft()
    if cnt>=10:#====틀렸던 이유2: cnt>10으로 했었는데, 그럼 11까지 출력되어버린다.
        break

    for d in range(4):
        new_r=move(r,d)
        new_b=move(b,d)

        if (new_r,new_b) in done or is_goal(new_b): continue #이미 거쳤던 곳이나 파란 구슬이 들어간 경우
        if is_goal(new_r):#빨간 구슬이 들어간 경우, 바로 break
            print(cnt+1)
            stat=False
            break

        if new_r == new_b:#두 구슬이 겹친 경우
            dist_r,dist_b=get_distance(r,new_r), get_distance(b,new_b)
            if dist_r<dist_b:
                new_b=(new_b[0]-dy[d],new_b[1]-dx[d]) #파란 구슬이 한 칸 뒤로
            else:
                new_r=(new_r[0]-dy[d],new_r[1]-dx[d]) #빨간 구슬이 한 칸 뒤로
        que.append([new_r,new_b,cnt+1])
        done.add((new_r,new_b))

if stat: print(-1)#빨간 구슬만 뺄 수 없는 경우