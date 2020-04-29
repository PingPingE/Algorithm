import sys
#	134764kb	524ms
N, M = map(int, sys.stdin.readline().split())
p_sum = [[0 for _ in range(N+1)] for __ in range(N+1)]
for r in range(N):
    c = 0
    for A in list(map(int, sys.stdin.readline().split())):
        #p_sum[r+1][c+1] : (0,0)~(r,c)까지의 구간 합
        p_sum[r+1][c+1] = p_sum[r+1][c] + p_sum[r][c+1] - p_sum[r][c] +A
        c+= 1
while M>0:
    M -= 1
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
    print(p_sum[x2][y2]-p_sum[x1-1][y2] - p_sum[x2][y1-1] + p_sum[x1-1][y1-1])