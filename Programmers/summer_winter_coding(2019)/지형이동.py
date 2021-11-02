#https://yeeybook.tistory.com/18
#1. 비용 0으로 갈 수 있는 좌표끼리 묶음 -> 그룹 생성
#2. 각 그룹으로 가는데 드는 최소비용 구하기
from collections import deque
def solution(land, height):
    answer = 0
    N = len(land)
    groups = {0:[(0,0)]}
    dy,dx = [1,-1,0,0], [0,0,1,-1]
    que = deque()
    done =set()
    num=0
    
    #1. 그룹만들기
    for i in range(N):
        for j in range(N):
            if (i,j) not in done:
                que.append((i,j))
                groups[num] = [(i,j)]
                done.add((i,j))
                while que:
                    y,x= que.popleft()
                    for d in range(4):
                        ny,nx = y+dy[d], x+dx[d]
                        if ny<0 or nx<0 or ny>=N or nx>=N or (ny,nx) in done: continue
                        diff = abs(land[y][x] - land[ny][nx])
                        if diff>height: continue
                        groups[num].append((ny,nx))
                        done.add((ny,nx))
                        que.append((ny,nx))
                num+=1
            else: continue
            
    # print(num)
    # print(groups)

    #2. 각 그룹으로 이동하는 최소비용 구하기
    links = {i:i for i in range(num)}
    
    return answer
