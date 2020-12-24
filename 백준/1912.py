#T1:2분
#T2:8분 41초
#T3:51분 58초
#처음에 prefix sum으로 저장한 후 이중 for문으로 각 구간별로 확인을 했는데 시간초과가 났음
#참고:https://suri78.tistory.com/12

#135060kb	144ms
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
for i in range(1,n):
    arr[i] = (max(arr[i]+arr[i-1], arr[i])) #연속합이 더 큰지, 현재 값이 더 큰지
print(max(arr))