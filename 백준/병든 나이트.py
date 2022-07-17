'''
문제)
병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.

2칸 위로, 1칸 오른쪽
1칸 위로, 2칸 오른쪽
1칸 아래로, 2칸 오른쪽
2칸 아래로, 1칸 오른쪽

병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 병든 나이트의 이동 횟수가 4번보다 적지 않다면,
이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.

체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.

입력)
첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.

출력)
병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다
'''
#규칙을 찾아야하는 문제(핵노가다) -> 움직일 수 있는 조건을 보면 N>=3, M>=7일때부터 정답이 같아짐(그 전엔 구간별로 룰작성)
N,M = map(int, input().split())
ans = 0

#규칙 : M<=6까지는 최대 4까지 나올 수 밖에 없음
if N == 1:
    ans = 1
elif N<=2:
    ans = min((M+1)//2,4)
elif M<=6:
    ans = min(M, 4)
else:
    ans = M-2

print(ans)

'''
삽질 기록)
로직은 맞지만 비효율적인 코드
'''
'''
from collections import deque
N,M = map(int, input().split())
board = list([0]*M for _ in range(N))
dir = [(-2,1), (-1,2), (1,2), (2,1)] 

ans = 0

def dfs(y,x,visited_node,visited_dir):
    global ans

    for dy,dx in dir:
        ny,nx = y+dy, x+dx
        if 0<=ny<N and 0<=nx<M and (ny,nx) not in visited_node:
            dfs(ny,nx,visited_node|set([(ny,nx)]), visited_dir|set([(dy,dx)]))

    tmp_ans=len(visited_node)
    if ans < tmp_ans:
        if tmp_ans >=5 and len(visited_dir)  == len(dir) :
            ans = tmp_ans

        elif tmp_ans < 5:
            ans = tmp_ans


def bfs(y,x):
    global ans
    que = deque([(y,x, set([(y,x)]), set())])

    while que:
        cur_y,cur_x, visited_node, visited_dir = que.popleft()
        tmp_ans = len(visited_node)
        if ans < tmp_ans:
            if tmp_ans >=5 and  len(visited_dir)  == len(dir):
                ans = tmp_ans
            elif tmp_ans < 5:
                ans = tmp_ans
        else: pass

        for dy, dx in dir:
            ny, nx = cur_y + dy, cur_x + dx
            if 0 <= ny < N and 0 <= nx < M and (ny,nx) not in visited_node:
                que.append((ny,nx,visited_node|set([(ny,nx)]), visited_dir|set([(dy,dx)])))

# dfs(N-1,0,set([(N-1,0)]), set())
bfs(N-1,0)
'''