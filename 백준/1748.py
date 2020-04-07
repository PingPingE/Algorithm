from time import time
N = int(input())
# st = ''
# s = time()
# for i in range(1,N+1):
#     st += str(i)
# print(len(st.strip()), time()-s)
# 5888896 2.9661037921905518

prev = 0
res = 0
i = 1
s =time()
while True:
    if (10**i) <= N:
        res += i*((10**i)-1-prev)
        prev = ((10**i)-1)
        i += 1
        continue
    else:
        n = N-prev
        res += i*n
        break
print(res, time()-s)
# 5888896 0.0