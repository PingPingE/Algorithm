'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

#max heap: 221928kb	2596ms ( -붙여서 push + pop함수에 print(-heap[1]) + heapify 부호 반대)
#min_heap: 222068kb	3212ms

def heapify(heap, cur_ind):
    if len(heap)-1 < cur_ind*2:
        return
    if len(heap)-1 == cur_ind*2:
        min_ind = cur_ind*2
    else:
        min_ind = min([cur_ind*2, cur_ind*2+1], key=heap.__getitem__)
    if heap[cur_ind]<= heap[min_ind]:
        return
    heap[min_ind], heap[cur_ind] = heap[cur_ind] , heap[min_ind]
    heapify(heap, min_ind)

def push(heap, x):
    cur_ind = len(heap)
    heap.append(x)
    while cur_ind//2 > 0:
        if heap[cur_ind//2] <= heap[cur_ind]:
            break
        heap[cur_ind//2], heap[cur_ind] = heap[cur_ind], heap[cur_ind//2]
        cur_ind//=2

def pop(heap):
    print(heap[1])
    heap[1] = heap[-1]
    del(heap[-1])
    heapify(heap, 1)

import sys
N= int(input())
arr = [0]
for _ in range(N):
    push(arr, int(sys.stdin.readline()))

for _ in range(N):
    pop(arr)
