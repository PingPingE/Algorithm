#T1~T2:35분
#127844kb	180ms
import sys
def check(length): #이 정도 길이(length) 가능한지
    cnt= C-1 #첫번째 집은 무조건 설치이므로
    i = 0
    while i<N and cnt>0:
        for t in range(i+1, N):
            if X[t]-X[i] >= length:
                i = t
                cnt -= 1
                break
        else:
            return False

    if cnt ==0:
        return True
    else: return False

N, C = map(int, input().split())
X = list(int(sys.stdin.readline()) for _ in range(N))
X.sort()
l,r = 1, X[-1]-X[0]+1
ans = 0
while l<=r:
    m = (l+r)//2
    if check(m):
        l = m+1
        ans = max(ans, m)
    else:
        r = m-1
print(ans)
