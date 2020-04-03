C = int(input())
res = {1: 'YES', 0:'NO'}
def dp(cur_i, cur_j,board,done):#done을 넣지 않으면 시간초과
    if cur_i<0 or cur_j<0 or cur_i>=n or cur_j >= n or (cur_i,cur_j) in done:
        return 0
    if board[cur_i][cur_j] == 0:#n을 없앴으니 이렇게 도착여부 확인
        return 1
    done.add((cur_i,cur_j))
    return max(dp(cur_i+board[cur_i][cur_j], cur_j, board,done), dp(cur_i, cur_j+board[cur_i][cur_j], board,done))
for _ in range(C):
    n = int(input())
    board = list(list(map(int, input().split())) for i in range(n))
    print(res[dp(0,0,board,set())])#매개변수 n을 없앰

#결과:	518B	정답	256ms