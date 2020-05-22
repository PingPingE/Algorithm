'''
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때,
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''
import sys
N= int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
prefix_sum = [0,0]
sum = 0
cur = 1
for e,a in  enumerate(arr):
    prefix_sum[cur] = prefix_sum[cur^1]+a
    sum += prefix_sum[cur]
    cur ^= 1
print(sum)