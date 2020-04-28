#121808kb	160ms
N, M = map(int, input().split())
A = list(map(int, input().split(' ')))
sum, s,e ,cnt= 0,0,0,0
while 1:
    if sum>=M:
        sum -= A[s]
        s+= 1
    elif e==N:
        break
    else:
        sum += A[e]
        e += 1
    if sum == M:
        cnt += 1
print(cnt)