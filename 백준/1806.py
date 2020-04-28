import sys
N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
res = N+1
sum, s, e =0,0,0
while 1: #35212kb 188ms
    if sum>=S:
        res = min(res, e-s)
        sum -= A[s]
        s += 1
    elif e==N:
        break
    else:
        sum += A[e]
        e+= 1

if res == N+1:
    print(0)
else:
    print(res)
