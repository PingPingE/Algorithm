'''
문제)
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

입력)
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력)
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
둘째 줄에는 가장 긴 증가하는 부분 수열을 출력한다. 그러한 수열이 여러가지인 경우 아무거나 출력한다.

'''
#122484kb	176ms
import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
res = {i:[0,[]] for i in range(N)}
maxx = [0,0]
for i in range(len(A)):
    res[i][0] = 1
    res[i][1].append(A[i])
    for j in range(i):
        if A[i]>A[j] and res[i][0] < res[j][0]+1:
            res[i][0] = res[j][0]+1
            res[i][1] = res[j][1][:]
            res[i][1].append(A[i])
    if maxx[0] < res[i][0]:
        maxx[0] = res[i][0]
        maxx[1] = i

print(maxx[0])
print(' '.join(map(str,res[maxx[1]][1])))

