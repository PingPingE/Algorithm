'''
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 40, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''

#기존 부분수열의합1 -> O(2^N)으로도 가능 but 이건 시초 -> 반으로 나누어서 왼쪽 수열의 부분수열을 A에 저장 후 오른쪽 진행
#참고: https://junho0956.tistory.com/166
from collections import defaultdict
import sys
N, S = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
ans = 0
A = defaultdict(int)
def sol(num, idx, end, stat): #현재까지 합, 인덱스, 인덱스 범위(끝), 왼쪽인지 오른쪽인지
    global ans, A
    if idx >= end:
        if stat:
            A[num] += 1
        else:
            ans += A[S-num]
        return
    sol(num+li[idx], idx+1, end, stat)
    sol(num, idx+1, end, stat)

sol(0,0,N//2,1)
sol(0,N//2,N,0)
print(ans if S != 0 else ans-1)
