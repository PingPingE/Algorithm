import time #시간 측정
import random
a= []

for i in range(10000): #두 병합정렬의 속도 차이를 측정하기 위해 10000개의 원소를 갖는 리스트 생성
    a.append(random.random())

start = 0 #시작시간

def merge_sort1(li):#병합정렬1
    global start
    start = time.time()
    if len(li) <= 1: #종료조건(재귀함수 필수)
        return li
    mid = len(li)//2 #리스트의 중간지점
    result = [] #결과를 저장할 리스트

    #재귀호출로 리스트를 계속 반으로 쪼갬
    x= merge_sort1(li[:mid])
    y= merge_sort1(li[mid:])
    
    
    #다 쪼개고 나서 합치기
    while x and y:#x,y 둘 다 값이 있으면 
        if x[0] >= y[0]:# 둘 중 작은 값을 result에 넣어준다.
            result.append(y.pop(0))
        else:
            result.append(x.pop(0))
        
    #x리스트에 값이 남아있으면
    while x:
        result.append(x.pop(0))
    #y리스트에 값이 남아있으면
    while y:
        result.append(y.pop(0))

    return result
b=a #a와 같은 원소를 가지는 리스트 
print(merge_sort1(b),"%.5f"%(time.time()-start))


def merge_sort2(li): #병합정렬2 -> 새로운 리스트없이 진행
    global start
    start = time.time()
    if len(li) > 1:
        mid = len(li)//2
        x= li[:mid]
        y = li[mid:]
        merge_sort2(x)
        merge_sort2(y)
        
        xn=0 #x리스트 순서
        yn=0 #y리스트 순서
        n=0 #li리스트 순서

        while xn <len(x) and yn< len(y):
            if x[xn] <= y[yn]:
                li[n] = x[xn]
                n += 1
                xn += 1
            else:
                li[n] = y[yn]
                n += 1
                yn += 1

        while xn<len(x):
            li[n] = x[xn]
            n += 1
            xn += 1

        while yn<len(y):
            li[n] = y[yn]
            n += 1
            yn += 1

     
merge_sort2(a)
print(a,"%.5f"%(time.time()-start))
  
    
#결론: 예상대로 return값 없이 바로 진행하는 merge_sort2가 더 빠르게 나온다. 되도록이면 새로운 리스트를 만들지 말자.
            
    
