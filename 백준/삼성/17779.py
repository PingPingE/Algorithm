'''
문제)
재현시의 시장 구재현은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 구재현은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 재현시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.

재현시는 크기가 N×N인 격자로 나타낼 수 있다. 격자의 각 칸은 구역을 의미하고, r행 c열에 있는 구역은 (r, c)로 나타낼 수 있다. 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

선거구를 나누는 방법은 다음과 같다.

기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
다음 칸은 경계선이다.
(x, y), (x+1, y-1), ..., (x+d1, y-d1)
(x, y), (x+1, y+1), ..., (x+d2, y+d2)
(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
(x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
구역 (r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다. 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.

입력)
첫째 줄에 재현시의 크기 N이 주어진다.
둘째 줄부터 N개의 줄에 N개의 정수가 주어진다. r행 c열의 정수는 A[r][c]를 의미한다.

출력)
첫째 줄에 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 출력한다.

제한)
5 ≤ N ≤ 20
1 ≤ A[r][c] ≤ 100

'''
#125816kb	580ms
import sys
N = int(input())
board= [[0 for __ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    target = list(map(int, sys.stdin.readline().split()))
    for e,b in enumerate(target,1):
        board[i][e] = b
ans = sys.maxsize
for x in range(1,N+1):
    for y in range(1,N+1):
        for d1 in range(1,N+1):
            for d2 in range(1,N+1):
                if 1<=x<x+d1+d2 and x+d1+d2<=N and 1<=y-d1<y and y<y+d2<=N:
                    pass
                else:
                    continue
                dic = {n:0 for n in range(1,6)} #각 선거구 인구 수
                tmp = [[0 for _ in range(N+1)] for __ in range(N+1)]

                tmp[x][y] = 5

                for i in range(d1+1):
                    nx=x+i
                    ny=y-i
                    if ny<0 or nx<0 or ny>N or nx>N:
                        break
                    tmp[nx][ny] =5
                    tmp[x+d2+i][y+d2-i] = 5

                for j in range(d2+1):
                    nx = x+j
                    ny = y+j
                    if ny < 0 or nx < 0 or ny > N or nx > N:
                        break
                    tmp[nx][ny] = 5
                    tmp[x+d1+j][y-d1+j] =5

                for tx in range(1,x+d1):
                    for ty in range(1,y+1):
                        if tmp[tx][ty] !=0:
                            break
                        tmp[tx][ty] = 1

                for tx in range(1,x+d2+1):
                    for ty in range(N,y,-1):
                        if tmp[tx][ty] !=0:
                            break
                        tmp[tx][ty] = 2

                for tx in range(x+d1, N+1):
                    for ty in range(1,y-d1+d2):
                        if tmp[tx][ty] !=0:
                            break
                        tmp[tx][ty] =3

                for tx in range(x+d2, N+1):
                    for ty in range(N,y-d1+d2-1, -1):
                        if tmp[tx][ty] !=0:
                            break
                        tmp[tx][ty] = 4

                for i in range(1,N+1):
                    for j in range(1, N+1):
                        if tmp[i][j] == 0: #5번 선거구는 경계선 빼고 안에는 채우지 않았기에...
                            dic[5] += board[i][j]
                        else:
                            dic[tmp[i][j]] += board[i][j]
                res = sorted(dic.values())
                ans = min(ans, res[-1]-res[0])

print(ans)