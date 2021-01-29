'''
문제)
nCm을 출력한다.

입력)
n과 m이 주어진다. (5 ≤ n ≤ 100, 5 ≤ m ≤ 100, m ≤ n)

출력)
nCm을 출력한다.
'''
#28776kb	68ms
memo= [-1 for _ in range(101)]
memo[1] = 1
def factorial(x):
    global memo
    if memo[x]==-1:
        memo[x] = x*factorial(x-1)
    return memo[x]

def combinations(n,m):
    if n==m: return 1
    return factorial(n)//(memo[n-m]*memo[m])

n,m = map(int, input().split())
print(combinations(n,m))
#math모듈에 comb, factorial함수가 있음. 단, factorial은 3.9부터 사라졌고, comb는 3.9부터 생겼다고 한다.