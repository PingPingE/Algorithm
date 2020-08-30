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
import sys
def dp(cur, ind):
    global memo
    if ind >=N:
        return cur[:]
    if len(memo[ind])>0:
        return memo[ind][:]

    case1,case2 = [],[A[ind]]
    case1= dp(cur[:], ind+1) #현재꺼 택X

    if len(case1)>0 and case1[0] > case2[0]:
        case2.extend(case1[:])

    if len(case1) >= len(case2):
        memo[ind] = case1[:]
        return case1[:]
    else:
        memo[ind] = case2[:]
        return case2[:]

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
memo = {k:[] for k in range(len(A))}
dp([],0)
# print(len(memo[0]))
# print(' '.join(map(str,memo[0][::-1])))
print(memo)

