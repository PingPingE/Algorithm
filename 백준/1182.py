'''
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
'''
#28776kb	396ms
import sys
sys.setrecursionlimit(10**8)
N, S = map(int, input().split())
li = list(map(int, sys.stdin.readline().split()))
def sol(num, idx, stat):
    global ans
    if idx>=N: #num==S로 조건을 두고 return으로 하면 뒷 숫자들이 0이거나 -1,1일 때 세지 못한다.
        if stat and num ==S: return  1
        else: return 0
    return sol(num+li[idx], idx+1, True)+sol(num, idx+1, stat)
print(sol(0,0,False))