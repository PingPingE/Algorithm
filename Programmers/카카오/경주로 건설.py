import sys
from collections import deque
def solution(board):
    ban = {0:1,1:0,2:3,3:2} #반대방향
    INF = sys.maxsize
    N = len(board)
    costs = [[INF for _ in range(len(board))] for __ in range(len(board))]
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    que = deque()
    que.append((0,0,0,1)) #현위치(r,c), 비용, 방향
    que.append((0,0,0,3))
    while que:
        y,x,cur_cost,cur_dir = que.popleft()
        for d in range(4):
            if ban[cur_dir] is d:
                continue
            ny = y+dy[d]
            nx = x+dx[d]
            if ny<0 or nx<0 or ny>=N or nx>=N or board[ny][nx] == 1:
                continue
            add_cost = 100
            if (cur_dir in [0,1] and d in [2,3]) or (cur_dir in [2,3] and d in [0,1]):
                add_cost +=500
            if costs[ny][nx] >= cur_cost+add_cost:
                costs[ny][nx] = cur_cost+add_cost
                que.append((ny,nx,cur_cost+add_cost, d))       
    return costs[N-1][N-1]

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.7MB)
테스트 2 〉	통과 (0.05ms, 10.9MB)
테스트 3 〉	통과 (0.06ms, 10.8MB)
테스트 4 〉	통과 (0.08ms, 10.8MB)
테스트 5 〉	통과 (0.08ms, 10.8MB)
테스트 6 〉	통과 (0.40ms, 10.8MB)
테스트 7 〉	통과 (0.44ms, 10.8MB)
테스트 8 〉	통과 (0.40ms, 10.8MB)
테스트 9 〉	통과 (0.75ms, 10.8MB)
테스트 10 〉	통과 (0.76ms, 10.8MB)
테스트 11 〉	통과 (60.60ms, 10.8MB)
테스트 12 〉	통과 (1.99ms, 10.8MB)
테스트 13 〉	통과 (0.18ms, 10.8MB)
테스트 14 〉	통과 (0.30ms, 10.8MB)
테스트 15 〉	통과 (1.54ms, 10.8MB)
테스트 16 〉	통과 (1.55ms, 10.7MB)
테스트 17 〉	통과 (7.53ms, 10.8MB)
테스트 18 〉	통과 (4.06ms, 10.8MB)
테스트 19 〉	통과 (41.67ms, 10.8MB)
테스트 20 〉	통과 (1.84ms, 10.8MB)
테스트 21 〉	통과 (1.07ms, 10.7MB)
테스트 22 〉	통과 (0.12ms, 10.8MB)
테스트 23 〉	통과 (0.10ms, 10.9MB)
'''