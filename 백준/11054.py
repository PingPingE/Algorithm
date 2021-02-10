'''
문제)
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 수열 A의 크기 N이 주어지고, 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ N ≤ 1,000, 1 ≤ Ai ≤ 1,000)

출력)
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.
'''
#123276kb	132ms
import sys
def max_ascending(k):
    for i in range(k):
        if A[i] < A[k]:
            mem_a[k] = max(mem_a[k], mem_a[i]+1)

def max_descending(k):
    for i in range(N-1,k,-1):
        if A[i] < A[k]:
            mem_d[k] = max(mem_d[k], mem_d[i]+1)

N = int(input())
A= list(map(int, sys.stdin.readline().split()))
mem_a,mem_d = [1 for _ in range(N)], [1 for _ in range(N)]
ans = 0
for k in range(N): #오름차순
    max_ascending(k)
for k in range(N-1,-1,-1): #내림차순(뒤에서부터 오름차순)
    max_descending(k)
for k in range(N):
    ans = max(ans, mem_a[k]+mem_d[k]-1)
print(ans)