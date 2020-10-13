from collections import deque
dy, dx= [-1,0,0,1],[0,-1,1,0]
N,M,power = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
y,x = map(lambda x:int(x)-1, input().split())
passengers ={}
for _ in range(M):
    from1,from2,to1,to2 = map(lambda x: int(x)-1, input().split())
    passengers[(from1,from2)] = (to1,to2)
#taxi 정보: y,x,power
def get_passenger(): #taxi -> 상하좌우 ->
    mini = [987654321, (-1,-1)]  # 최소 거리,passengers의 key
    que = deque()
    que.append([0,y,x])
    done =set()
    done.add((y,x))
    while que:
        count,r,c = que.popleft()
        if (r,c) in passengers and count <= mini[0]:
            if count == mini[0]:
                if mini[1][0] >= r:
                    if mini[1][0] == r:
                        if mini[1][1]>r:
                            mini = [count, (r, c)]
                        else:
                            continue
                    else:
                        mini = [count, (r, c)]
                else:
                    continue
            else:
                mini =[count, (r,c)]
            continue

        if count >=mini[0]: break

        for d in range(4):
            nr,nc = r+dy[d] , c+dx[d]
            if nr<0 or nc<0 or nr>=N or nc>=N or board[nr][nc] == 1 or (nr,nc) in done:
                continue
            que.append([count+1, nr,nc])
            done.add((nr,nc))
    return mini

def go(taxi, goal):
    global power
    que = deque()
    que.append([0,taxi[0],taxi[1]])
    done = set()
    done.add((taxi[0],taxi[1]))
    while que:
        reduce,r,c = que.popleft()
        if (r,c) == goal:
            if reduce <=power:#목적지까지 가는데 소모되는 연료 체크
                power += reduce
                return True
            else:
                return False
        for d in range(4):
            ny,nx = r+dy[d], c+dx[d]
            if ny<0 or nx<0 or ny>=N or nx>=N or (ny,nx) in done or board[ny][nx] == 1:
                continue
            que.append([reduce+1, ny,nx])
            done.add((ny,nx))
    return False

stat = False
while M>0:
    M-=1
    target = get_passenger()
    power -= target[0]
    print(target)
    if target[0] == 987654321 or power<0: #가는 길에 연료 다 소모하면 땡
        stat = True
        break
    if go(target[1] , passengers[target[1]]):
        y,x = passengers[target[1]]
        passengers.pop(target[1])
    else:
        stat= True
        break
print(-1 if stat else power)




