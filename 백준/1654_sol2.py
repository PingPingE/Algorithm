#T1: 4분 25초
#T2: 10분 52초
#T3: 19분 45초

#123352kb	124ms
def count(length):
    cnt = 0
    for i in li:
        cnt += i//length
    return cnt
import sys
K, N = map(int, input().split())
li = list(int(sys.stdin.readline()) for _ in range(K))
l,r = 1,max(li) #틀렸던 이유: l이 0부터 시작 -> 런타임에러(divide by zero) -> 그래서 1로바꿈
ans = 0
if N == 1: print(r)
else:
    while l<=r:
        m = (l+r)//2
        if count(m) >= N:
            l = m+1
            ans = m
        else:
            r = m-1
    print(ans)