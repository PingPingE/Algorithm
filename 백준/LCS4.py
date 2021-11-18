#시간초과
N = int(input())
A, B= list(map(int, input().split())), list(map(int, input().split()))
ans =0

#이전 행의 값만 참고하면 되지않나
arr = [[0]*(N+1) for _ in range(2)]
flag = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if A[i-1] == B[j-1]:
            arr[flag][j] = arr[not flag][j-1]+1
            ans = max(ans, arr[flag][j])
        else:
            arr[flag][j] = max(arr[not flag][j], arr[flag][j-1])
    flag= not flag

print(ans)
