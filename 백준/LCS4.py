'''
문제)
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, [1, 2, 3]과 [1, 3, 2]의 LCS는 [1, 2] 또는 [1, 3] 이다.

1부터 N까지 정수가 모두 한 번씩 등장하는 두 수열 A와 B가 주어졌을 때, 두 수열의 LCS 크기를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 두 수열의 크기 N (1 ≤ N ≤ 100,000)이 주어진다.

둘째 줄에는 수열 A에 들어있는 수가, 셋째 줄에는 수열 B에 들어있는 수가 주어진다.

출력)
두 수열의 LCS의 크기를 출력한다.
'''
#155944ms	196kb

#솔루션(참고: https://chanhuiseok.github.io/posts/algo-49/)
#1부터 N까지 정소가 모두 한 번씩 등장하는거니 A,B의 원소 구성은 같다. 순서만 다를 수 있는거지
#1. 각 A의 원소가 B수열에서는 어느 위치에(인덱스) 있는지 구하기
#2. 1에서 구한 수열의 LIS 구하기

N = int(input())
A, B= list(map(int, input().split())), {value: e  for e, value in enumerate(map(int, input().split()))}
#1.각 A의 원소가 B수열에서는 어느 위치에(인덱스) 있는지 구하기
AB_idx = [B[A[i]] for i in range(N)]

#2. LIS구하기
ans = [AB_idx[0]]
def binary_search(target):
    global ans
    l, r = 0, len(ans)-1

    while l <= r:
        m = (l + r) // 2
        if ans[m] < target:
            l= m+1
        else:
            r= m-1
    if l >= len(ans):
        ans.append(target)
    else:
        ans[l] = target

# print(AB_idx)
for i in range(1,N):
    binary_search(AB_idx[i])
print(len(ans))

'''
TC)
5
1 3 2 4 5
3 2 1 4 5

6
1 6 3 2 4 5
3 2 1 4 5 6
'''

#==========================================
#시간초과
'''
N = int(input())
A, B= list(map(int, input().split())), list(map(int, input().split()))
ans =0
start, end = 0, N

#처음과 마지막 원소가 같지 않을때까지 pop
while  start<=end and A[start] == B[start]:
    start+=1

while start <= end and A[end-1] == B[end-1]:
    end-=1

N= len(A)
#이전 행의 값만 참고하면 되지않나
arr = [[0]*(N+1) for _ in range(2)]
flag = 0

for i in range(start+1, end+1):
    for j in range(start+1, end+1):
        if A[i-1] == B[j-1]:
            arr[flag][j] = arr[not flag][j-1]+1
            ans = max(ans, arr[flag][j])
        else:
            arr[flag][j] = max(arr[not flag][j], arr[flag][j-1])
    flag= not flag
print(ans+start+N-end)
'''
