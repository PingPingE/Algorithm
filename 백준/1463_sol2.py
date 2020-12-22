#T1:11분 5초
#T2:29분(17분55초)
#T3:-
import sys
sys.setrecursionlimit(10**9)

def solution(m): #stack overflow(제출X)
    global memo
    if m<=0: return INF
    if memo[m] == INF:
        memo[m] = min(memo[m], solution(m//3 if m%3==0 else -1)+1, solution(m//2 if m%2==0 else -1)+1, solution(m-1)+1)
    return memo[m]

#제출:188420kb	172ms
X = int(input())
INF = 9876543
memo = list(INF for _ in range(X+1)) #index에 해당하는 숫자에서 1로 만들때 최소 연산 횟수
memo[1] = 0
for x in range(2, X+1):
    memo[x] = min(memo[x], memo[x//3]+1 if x%3 == 0 else INF, memo[x//2]+1 if x%2==0 else INF, memo[x-1]+1)
print(memo[X])
