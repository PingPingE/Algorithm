from collections import deque

import sys
n = int(input())
A = deque()
B= deque()
C = deque()
D = deque()
for _ in range(n):
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = {}
cd = {}
for i in range(n):
    for j in range(len(A)):
        # A+B : key, key의 등장 횟수(중복수) : value
        if A[i]+B[j] in ab:
            ab[A[i]+B[j]] += 1
        else:
            ab[A[i]+B[j]] = 1
        # -(C+D) : key, key의 등장 횟수(중복수) : value
        if (-(C[i] + D[j])) in cd:
            cd[(-(C[i] + D[j]))] += 1
        else:
            cd[(-(C[i] + D[j]))] = 1

res = 0
while ab:
    k1,v1 = ab.popitem()
    #ab의 키 값과 cd의 키 값이 매칭 되면,
    #해당 value들을 곱해줌
    if k1 in cd:
        res += v1*cd[k1]

print(res)

# #숏코딩
# from collections import Counter
# tot = 0
# n = int(input())
# A, B, C, D = ([0] * n for _ in range(4))
# for i in range(n):
#     A[i], B[i], C[i], D[i] = map(int, input().split())
#
# c_d = Counter((c+d for c in C for d in D))
#
# for n in (a+b for a in A for b in B):
#     tot += c_d[-n]
# print(tot)