'''
한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다.
각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때,
A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 T(-1,000,000,000 ≤ T ≤ 1,000,000,000)가 주어진다. 다음 줄에는 n(1 ≤ n ≤ 1,000)이 주어지고, 그 다음 줄에 n개의 정수로 A[1], …, A[n]이 주어진다.
다음 줄에는 m(1≤m≤1,000)이 주어지고, 그 다음 줄에 m개의 정수로 B[1], …, B[m]이 주어진다. 각각의 배열 원소는 절댓값이 1,000,000을 넘지 않는 정수이다.
'''
T = int(input())
n =int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
#1. 두 배열 모두 부분 집합을 구한다.
#단, 처음 구하는 A의 부분집합은 배열에 담고 뒤에 구하는 B의 부분집합은 맵에 담아서 빠른 검색하도록하기
#2. A의 부분집합을 차례로 보면서 T값이 되기 위한 값이 B의 부분집합에 있는지 검색한다. -> 있으면 value(개수)만큼  count
#204864kb 328ms
pA ,mB= [], {}
A_a = pA.append
for i in range(n):
    tmp_sum = A[i]
    A_a(tmp_sum)
    for j in range(i+1, n):
        tmp_sum += A[j]
        A_a(tmp_sum)

for i in range(m):
    tmp_sum = B[i]
    mB[tmp_sum] = mB.get(tmp_sum, 0) + 1
    for j in range(i+1, m):
        tmp_sum += B[j]
        mB[tmp_sum] = mB.get(tmp_sum, 0) + 1
cnt = 0
for i in pA:
    if T-i in mB:
        cnt += mB[T-i]
print(cnt)