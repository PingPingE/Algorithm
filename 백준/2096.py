'''
문제)
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.
먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다.
바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다. 이 제약 조건을 그림으로 나타내어 보면 다음과 같다.
별표는 현재 위치이고, 그 아랫 줄의 파란 동그라미는 원룡이가 다음 줄로 내려갈 수 있는 위치이며, 빨간 가위표는 원룡이가 내려갈 수 없는 위치가 된다.
숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합이다.

입력)
첫째 줄에 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 숫자가 세 개씩 주어진다. 숫자는 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중의 하나가 된다.

출력)
첫째 줄에 얻을 수 있는 최대 점수와 최소 점수를 띄어서 출력한다.

'''
#solution2
#122892kb	256ms
import sys
N = int(input())
cur_max= [0,0,0]
cur_min = [0,0,0]

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    tmp_max = cur_max[:]
    tmp_min = cur_min[:]

    # 해당 칸으로 이동할 수 있는 칸의 이전 값 중 최댓값+각 칸
    cur_max[0] = arr[0] + max(tmp_max[:2])
    cur_max[1] = arr[1] + max(tmp_max)
    cur_max[2] = arr[2] + max(tmp_max[1:])

    # 해당 칸으로 이동할 수 있는 칸의 이전 값 중 최솟값+각 칸
    cur_min[0] = arr[0] + min(tmp_min[:2])
    cur_min[1] = arr[1] + min(tmp_min)
    cur_min[2] = arr[2] + min(tmp_min[1:])

print(f"{max(cur_max)} {min(cur_min)}")

#solution1
#29380kb	432ms
# import sys
# N = int(input())
# minn = [[0,0,0],[0,0,0]]#이전, 현재
# maxx = [[0,0,0], [0,0,0]]#이전, 현재
# minn[0] = list(map(int, sys.stdin.readline().split()))
# maxx[0] = minn[0][:]
# cur = 1
# for _ in range(N-1):
#     a,b,c = map(int, sys.stdin.readline().split())
#     maxx[cur][0] = max(maxx[not cur][0:2])+a
#     maxx[cur][1] = max(maxx[cur][0]-a,maxx[not cur][2])+b
#     maxx[cur][2] = max(maxx[not cur][1:3])+c
#
#     minn[cur][0] = min(minn[not cur][0:2]) + a
#     minn[cur][1] = min(minn[cur][0]- a, minn[not cur][2]) + b
#     minn[cur][2] = min(minn[not cur][1:3]) + c
#     cur = not cur#이전, 현재의 위치 바꾸기
# print(f"{max(maxx[not cur])} {min(minn[not cur])}")