#quick sort : pivot, L, R
def partition(arr, start, end):
    L = start+1
    pivot = arr[start] #첫번째 원소를 pivot으로
    R = end
    while L<=R:
        while L<=end and arr[L]<= pivot:#왼쪽은 pivot 보다 작은값
            L += 1
        while R>start and arr[R]>pivot:#오른쪽은 pivot 보다 큰 값
            R -= 1
       
        if L<R:#아직 검사할 원소가 있으면
            arr[L], arr[R] = arr[R],arr[L]#L과 R자리의 원소 swap
        
    #모든 원소를 다 돌았으면
    arr[R], arr[start] = arr[start], arr[R]#pivot과 R자리의 원소 swap
    return R #현재 R위치에 pivot이 있으므로(중간값)
    
def Quicksort(arr, start, end):
    if start<end:
        p = partition(arr,start,end)#partition을 통해 받은 R값을 p에 저장
        #p값을 중심으로 다시 나눔
        Quicksort(arr,start, p-1)
        Quicksort(arr,p+1, end)

#Test
arr1 = [3,5,1,2,23,12,7,3,8,12,4,2,10]
arr2 = [100,27,35,87,34,123,456,52,8,0]
arr3 = [67,3.6,278,12,1200,0.4,235,3.9,0,1]
Quicksort(arr1, 0,len(arr1)-1)
Quicksort(arr2, 0,len(arr2)-1)
Quicksort(arr3, 0,len(arr3)-1)
print(arr1)
print(arr2)
print(arr3)
