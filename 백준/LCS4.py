#시간초과
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
