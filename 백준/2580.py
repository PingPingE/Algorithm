'''
문제)
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 
게임 시작 전 몇 몇 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.
게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.

입력)
아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 
스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.

출력)
모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
'''

# #138728kb	3600ms
# import sys
# def get_candi(r,c):
#     all = list(str(i) for i in range(1,10))
#     for i in range(9):
#         if board[r][i] in all:
#             all.remove(board[r][i])
#         if board[i][c] in all:
#             all.remove(board[i][c])
#
#     for i in range(r//3*3, r//3*3+3):
#         for j in range(c//3*3, c//3*3+3):
#             if board[i][j] in all:
#                 all.remove(board[i][j])
#     return all
# def sol(n):
#     global board
#     if n>=len(zero):
#         for b in board:
#             print(' '.join(b))
#         exit()
#     r,c = zero[n]
#     #set를 만들고 연산 하는 이 과정이 오래 걸리는 듯
#     # s_set = all_set - (set(board[r][:]) | set(b[c] for b in board))
#     # s_set -= set(bb for b in board[r//3*3:r//3*3+3] for bb in b[c//3*3:c//3*3+3])
#     s_set = get_candi(r,c)
#     for s in s_set:
#         board[r][c] = s
#         sol(n+1)
#         board[r][c] = '0'
# board = []
# zero = []
# for _ in range(9):
#     li = list(sys.stdin.readline().split())
#     for e,l in enumerate(li):
#         if l == '0':
#             zero.append((_,e))
#     board.append(li)
# sol(0)

#sol2) 비트마스킹으로 가로/세로/3*3의 요소들 검사
#128484kb	1028ms
import sys
def sol(n):
    global board
    if n>=len(zero):
        for b in board:
            print(' '.join(map(str,b)))
        exit() #바로 종료
    r,c = zero[n]
    #bit masking으로 후보 구하기
    bit = 0
    for i in range(9):
        bit |= 1<<board[r][i]
        bit |= 1<<board[i][c]
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            bit |= 1<<board[i][j]
    for i in range(1,10):
        if bit & (1<<i):
            continue
        board[r][c] = i
        sol(n+1)
        board[r][c] =0

zero = []
board = []
for _ in range(9):
    li = list(list(map(int, sys.stdin.readline().split())))
    for e,l in enumerate(li):
        if l == 0:
            zero.append((_,e))
    board.append(li)
sol(0)