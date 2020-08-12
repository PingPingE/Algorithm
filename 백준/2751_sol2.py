'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
def merge(s,m,e):
    global arr
    tmp =[]
    i,j = s,m+1
    while i<=m and j<=e:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1
    while i<=m:
        tmp.append(arr[i])
        i+=1
    while j<=e:
        tmp.append(arr[j])
        j+=1
    arr[s:e+1] = tmp[:]
def partition(begin, end):
    if begin < end:
        mid = (begin+end)//2
        partition(begin, mid)
        partition(mid+1, end)
        merge(begin, mid, end)

#merge sort적용: 232620kb	1484ms
import sys,heapq
N = int(input())
arr = list(int(sys.stdin.readline()) for _ in range(N))
partition(0,N-1)
for a in arr:
    print(a)

#heap sort적용: 217996kb	1252ms
# arr = []
# heapq.heapify(arr)
# for _ in range(N):
#     heapq.heappush(arr,int(sys.stdin.readline()))
# while arr:
#     print(heapq.heappop(arr))