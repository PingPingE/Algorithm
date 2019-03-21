def binary_search(li, x): #리스트 li 에서 x찾기 (이분검색)
    low = 0
    high = len(li)-1
    while True:
        mid = (high+low)//2
        if li[mid] == x:
            break
        elif li[mid] < x:#x가 mid 위치의 원소보다 크면
            low = mid+1
        else:#x가 mid위치의 원소보다 작으면
            high = mid-1
            
    return mid+1 #1부터 시작

a = [4,356,3,46,7,86,84,35,6,7,8,3,44,64,77]
a.sort()#이분탐색의 조건: 리스트가 정렬되어 있어야 한다.
print(a, binary_search(a, 46))
            
