'''
문제
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
'''
import sys
from collections import deque
N,M = map(int, input().split())
A = deque(map(int, sys.stdin.readline().split()))
B = deque(map(int, sys.stdin.readline().split()))
res = []

#sol2: 335772kb 1756ms -> popleft + append 연산때문에 더 느려진듯하다.
while A and B:
    if A[0]  > B[0]:
        res.append(B.popleft())
    else:
        res.append(A.popleft())
res.extend(A)
res.extend(B)
print(*res)

#sol1: 340228kb 1216ms
a,b=0,0
while a<len(A) and b<len(B):
    if A[a] >B[b]:
        res.append(B[b])
        b+=1
    else:
        res.append(A[a])
        a+=1
res.extend(A[a:])
res.extend(B[b:])
print(*res)
