'''
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''
#125740kb	132ms
import sys
N,B = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def cal(a,b):
    ret= [list(sum(i*j for i,j in zip(row,col))%1000 for col in zip(*b)) for row in a]
    return ret

def main_cal(n):
    global A
    #단위행렬로 초기화
    ret = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
    while n>0:
        if n%2:#홀수면 짝수(N-1)로 만들어주기 위해 ->  A*A^(N-1)
            ret= cal(A,ret) #분해한 A는 결과값에 저장
        A = cal(A, A)
        n //= 2
    return ret

ans = main_cal(B)
for r in range(N):
    print(' '.join(map(str, ans[r])))


