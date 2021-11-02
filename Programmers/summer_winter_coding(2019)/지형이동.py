#https://yeeybook.tistory.com/18


#1. 비용 0으로 갈 수 있는 좌표끼리 묶음 -> 그룹 생성
#2. 각 그룹으로 가는데 드는 최소비용 구하기
#3. 모든 그룹을 최소비용으로 방문하기

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
    
    links = {i:i for i in range(num)}
    
    #2. 각 그룹으로 이동하는 최소비용 구하기
    costs = [[10000]*num for _ in range(num)]
    que=[]
    for i in range(num):
        costs[i][i] =0
        for j in range(num):
            for y,x in groups[i]:
                for d in range(4):
                    ny,nx = y+dy[d] , x+dx[d]
                    if (ny,nx) in groups[j]:
                        costs[i][j] = min(costs[i][j], abs(land[y][x] - land[ny][nx]))
                        que.append([costs[i][j], i, j])
            
    #3. 모든 그룹을 최소비용으로 방문하기(크루스칼)
    cnt=0
    def find(x):
        if links[x] == x: return x
        return find(links[x])

    def union(a,b):
        nonlocal links
        a_ ,b_ = find(a), find(b)
        if a_ < b_:
            links[b_]=a_
        else:
            links[a_]=b_
            
    for cost,g1,g2 in sorted(que, key=lambda x: x[0]):
        if find(g1) == find(g2):
            continue
        union(g1,g2)
        answer += cost
        cnt+=1
        
    return answer
