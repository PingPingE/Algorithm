def tmp(r):
    if r>0:
        return 1
    return 0
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
res = 0
for a in A:
    a -= B
    res += 1
    if a<= 0:
        continue
    if a<=C:
        res += 1
        continue
    r1 = tmp(a%C)
    res += (a//C)+r1

print(res)



