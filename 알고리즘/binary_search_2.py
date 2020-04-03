def binary_search(A, cur, target,first):#타겟 리스트, 현재 인덱스, 타겟, 처음 시작 구했는지 여부
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low+high)//2
        if A[mid] == target:
            if first is True:#first구했다
                low = mid+1
            else:
                high = mid-1
        elif A[mid] > target:
            high= mid-1
        else:
            low = mid+1
    return low

A = [3,3,4,5,6,6,73,15,24,5,6,6,1,2,43,55,5,5,55,55,55,55]
A.sort()
print(A)
target = 1
first = binary_search(A, 0,target, False) #배열에 target이 없는 경우는 없다는 가정하에
last = binary_search(A, first, target, True)
print(f'배열 A에 {target}이(가) {last-first}개가 있다.')

