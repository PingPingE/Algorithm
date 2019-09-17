import sys
sys.setrecursionlimit(10**8)
N= int(input())
res = [0 for _ in range(N+1)]
def sol(n):
    if n<=0 : return 0
    if res[n] == 0:
        res[n] = max(sol(n-1)+1, sol(n-3)*2, sol(n-4)*3, sol(n-5)*4)
    return res[n]
print(sol(N))