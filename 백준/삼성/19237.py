'''
문제
청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다.
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데,
1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.

입력)
첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)
그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.
그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 
하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 
두 번째 줄은 아래를 향할 때의 우선순위, 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 
각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 
가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.

맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.

출력)
1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.
'''
#124004kb	304ms
N,M,K = map(int, input().split())
sharks = [[-1,-1,-1] for _ in range(M)] #index: 각 상어의 번호, value: 현재 방향과 위치(y,x)
board = [[[-1,0]]*N for _ in range(N) ] #[냄새 뿌린 상어의 번호, 냄새가 없어지기 까지 남은 시간]
for _ in range(N):
    li = list(map(int, input().split()))
    for e,l in enumerate(li):
        if l >0:
            board[_][e] = [l-1, K]
            sharks[l-1][1] = _
            sharks[l-1][2] = e
# print(board)

p_dir = [] #index: 각 상어의 번호 value: 각 방향 당 우선순위(dict)
dir = {1:[-1,0], 2:[1,0], 3:[0,-1],4:[0,1]}
for e,d in enumerate(map(int,input().split())): #초기 위치
    sharks[e][0] = d

for s_num in range(M): #각 상어의 우선순위
    p_dic = {}
    for i in range(1,5):
        p_dic[i] = tuple(map(int, input().split()))
    p_dir.append(p_dic)
# print(p_dir)

total_time = 0 #1000초 넘기면 무조건 stop

def find_empty():
    empty_place = set()
    for i in range(N):
        for j in range(N):
            if board[i][j][0]==-1:
                empty_place.add((i,j))
    return empty_place

done = set() #죽은 상어
while total_time<1000 and len(done)<M-1:
    total_time += 1
    #냄새가 없는 공간 찾기
    empty_place = find_empty()
    #상하좌우 이동
    for e,shark in enumerate(sharks):
        # print("\n----shark:",e)
        if e in done: continue
        cur_d, y,x = shark
        # print("currnet:", y,x, "cur_d:",cur_d)
        candi = [] #빈 곳없으면 자신의 냄새가 있는 곳으로 돌아가도록

        # 이동할 곳 찾기 (우선순위 순으로 빈 곳)
        for nd in p_dir[e][cur_d]:
            ny,nx = y+dir[nd][0], x+dir[nd][1]
            if (ny,nx) in empty_place:
                if board[ny][nx][0] == -1: #그 전에 먼저 차지 하지 않았는지
                    board[ny][nx] = [e,K] # 냄새 뿌리기
                    sharks[e] = [nd,ny,nx]#상어 정보 갱신
                    # print("====move to:",ny,nx,"   dir:",nd)
                else: #누가 차지했으면 쫓겨남
                    done.add(e)
                break
            elif 0<=ny<N and 0<=nx<N and board[ny][nx][0] == e:#자기 자신의 냄새가 있는 곳이면?
                candi.append((nd,ny,nx))

        else: #인접한 곳에 아무 냄새가 없는 칸이 없다면 자신의 냄새가 있는 칸으로 방향을 잡는다
            nd,ny,nx = candi[0]
            # if board[ny][nx][0] != e:
            #     done.add(e)
            #     continue
            board[ny][nx][1] =K+1 # 냄새 뿌리기(밑에서 --되니까 K+1)
            sharks[e] = [nd, ny,nx] #상어 정보 갱신
    #냄새 유지 시간 --
    for a in range(N):
        for b in range(N):
            if (a,b) not in empty_place:
                # print("before:", board[a][b])
                board[a][b][1] -=1
                if board[a][b][1] == 0:
                    board[a][b][0] = -1
                # print("after:", board[a][b])

print(-1 if len(done)<M-1 else total_time)