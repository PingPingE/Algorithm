def sift_down(arr, start, end):
    big = start #가장 큰 값 저장(초기값: 부모노드)
    while start*2+1 <= end: #자식이 있으면 진행
        left = start*2+1 #0부터 시작하므로 start*2+1
        right = left+1 
        if arr[left] > arr[big]: #왼쪽자식이 big보다 더 크면
            big = left
        if right<=end and arr[right]>arr[big]: #오른쪽 자식이 있고 big보다 더 크면
            big = right
        if big != start: #big값이 바뀌었으면
            arr[big],arr[start]= arr[start],a[big] #부모와 자리를 바꿔주고
            start = big #부모는 big값을 가짐
        else:
            return
        
def heapify(arr,start,end):
    last = end #bottom-up 형식
    parent = int(last/2) #가장 마지막 부모노드
    while parent >= 0:
        sift_down(arr, parent, last) #밑에서 부터 자식노드와 부모노드 비교
        parent -= 1

def heap(arr, start, end):
    heapify(arr, start, end) #힙을 만들고
    for i in range(end,0,-1): #힙이 빌 때 까지 반복
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr, 0, i-1)

#a = [35,467,52,78, 895,34,432,885,0,23,3]
a = [23,56,4,6,8,94,27,8,9,10]
heap(a, 0, len(a)-1)
print(a)
