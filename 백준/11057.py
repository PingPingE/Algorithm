N = int(input())
#행 : 시작 숫자, 열 : 숫자 길이
arr = [[0]*N for _ in range(10)]
for i in range(10):
    arr[i][0] = 1
sum = 0
#0~N까지 길이
for k in range(N):
    #0~9까지 시작숫자
    for kk in range(10):
        if arr[kk][k] == 0:
            for j in range(kk,10):
                arr[kk][k] += arr[j][k-1]%10007
        if k == N-1:
            sum += arr[kk][k]
print(sum%10007)