#T1: 7분 12초
#T2: 13분 24초(6분 12초)
#T3: -
#247760kb	492ms
import sys
def check(length):#M이상의 길이가 나오는지
    sum =0
    for i in range(N):
        if li[i] <= length: return False
        sum += li[i]-length
        if sum >= M: return True
    return False

N,M = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort(reverse= True)
l,r = 0, li[0]
ans = 0
while l<=r:
    m = (l+r)//2
    if check(m):
        l = m+1
        ans = m
    else:
        r = m-1
print(ans)