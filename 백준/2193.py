N = int(input())
#끝자리 0갯수, 1갯수
m = {1:(0,1), 2:(1,0),3:(1,1)}
if N ==1 or N==2:
    print(1)
else:
    del(m[1])
    del(m[2])
    for i in range(4,N+1):
        cnt0 = 0
        cnt1 = 0
        c0, c1 = m[i-1]
        m[i] = (c0+c1, c0)
        del(m[i-1])
    a,b = m[N]
    print(a+b)