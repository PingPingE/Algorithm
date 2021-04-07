'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''
#sol1: set의 in 연산으로 O(1)에 확인
#152200kb	260ms
import sys
N=int(input())
A=set(map(int, sys.stdin.readline().split()))
M=int(input())
for i in list(map(int, sys.stdin.readline().split())):
    if i in A:
        print(1)
    else:
        print(0)

#sol2: list의 in 연산으로 O(N)에 확인
#147140kb  3676ms => 올바른 자료구조 선택의 중요성...
import sys
N=int(input())
A=list(map(int, sys.stdin.readline().split()))
M=int(input())
for i in list(map(int, sys.stdin.readline().split())):
    if i in A:
        print(1)
    else:
        print(0)

#sol3: list + binary search
#144872kb	284ms => set보다 memory 줄고, 시간은 비슷
import sys
def binary_search(x):
    l,r=0,len(A)-1
    while l<=r:
        m=(l+r)//2
        if A[m] == x:
            return True
        elif A[m]<x:
            l=m+1
        else:
            r=m-1
    return False

N=int(input())
A=sorted(map(int, sys.stdin.readline().split()))
M=int(input())
for i in list(map(int, sys.stdin.readline().split())):
    if binary_search(i):
        print(1)
    else:
        print(0)