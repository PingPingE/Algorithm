'''
문제
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)
이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때,
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.

출력
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''
'''
현재 방법)
상하좌우 네 방향으로 갈 수 있는데,
한 방향(현재는 '좌')만 구현하고 회전한 보드를 인풋으로 넣어줘서 네 방향으로 이동할 수 있도록 한다.
-> 개선점: 왼쪽으로 당길 때 좀 더 효율적으로(당길 때 중간에도 빈칸(0)이 없도록)
'''
from collections import deque
def renew_maxx():
    global maxx,board
    for b in board:
        maxx=max(maxx, max(b))

def left():#=====좌로 이동 구현
    global board
    print("before======")
    for b in board:
        print(b)
    print('============')
    #===왼쪽으로 당기기(왼쪽에 빈칸(0) 없애기 위함)
    for i in range(N):
        que= deque(board[i][:])
        for _ in range(N):
            if que[0]>0:break
            que.rotate(-1)
        print(que)
        board[i][:] = list(que)

    for i in range(N):#===당긴 후 합치기 
        cur_j = 0
        cur_value = 0
        for j in range(N):
            if board[i][j]>0:
                if board[i][j] == cur_value:
                    board[i][cur_j] = cur_value * 2
                    cur_value = 0
                else:
                    board[i][cur_j] = board[i][j]
                    cur_value=board[i][j]
                board[i][j] = 0
                cur_j += 1

    print("after========")
    for b in board:
        print(b)
    print('============')

def rotation():
    tmp=list([0]*N for _ in range(N))
    for i in range(N):
        for j in range(N):
            tmp[i][j] = board[N-1-j][i]
    return tmp

def dfs(cnt):
    global board
    if cnt>=5:
        return
    renew_maxx()
    for _ in range(4):
        board = rotation()#회전하고
        left()#좌로 이동
        dfs(cnt+1)

N=int(input())
board=[list(map(int, input().split()))for _ in range(N)]
maxx=0
dfs(0)
print(maxx)

'''
Test Case

3
2 2 2
4 4 4
8 8 8

5
0 0 2 0 3
0 5 0 0 0
2 0 0 2 0
0 0 0 0 0
0 0 5 0 3
'''