C = int(input())
res = {1: 'YES', 0:'NO'}
def dp(cur_i, cur_j):#done도 없앰
    if cur_i<0 or cur_j<0 or cur_i>=n or cur_j >= n or board[cur_i][cur_j] == -1:
        return 0
    if board[cur_i][cur_j] == 0:
        return 1
    tmp = board[cur_i][cur_j]
    board[cur_i][cur_j] = -1#-1로 done 대체
    return max(dp(cur_i+tmp, cur_j), dp(cur_i, cur_j+tmp))
for _ in range(C):
    n = int(input())
    board = list(list(map(int, input().split())) for i in range(n))
    print(res[dp(0,0)])

#결과: 477B	정답	224ms