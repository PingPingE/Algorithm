'''
문제
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다.
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

출력
첫째 줄에 구하고자 하는 최소의 길이를 출력한다. 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
'''
#sol2: 원본 list는 없고 부분합을 받는 list 존재
#135244kb	200ms
# import sys
# N, S = map(int, input().split())
# prefix_s = [0]
# pre_ap = prefix_s.append
# start,end,ans = 0,0,sys.maxsize
# for e,num in enumerate(list(map(int, sys.stdin.readline().split()))):
#     pre_ap(prefix_s[e]+num)
#     if end == 0 and prefix_s[e+1] >= S:
#         end = e+1
#
# while start<=end and end<=N:
#     if prefix_s[end]-prefix_s[start] >= S:
#         ans = min(ans, end - start)
#         start+=1
#     else:
#         end+=1
# print(0 if ans==sys.maxsize else ans)

#sol1: 원본 리스트(A)가 있고, 부분합은 int형 변수(sum) 하나에 저장
#35212kb	188ms
import sys
N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
res = N+1
sum, s, e =0,0,0
while 1:
    if sum>=S:
        res = min(res, e-s)
        sum -= A[s]
        s += 1
    elif e==N:
        break
    else:
        sum += A[e]
        e+= 1

if res == N+1:
    print(0)
else:
    print(res)
