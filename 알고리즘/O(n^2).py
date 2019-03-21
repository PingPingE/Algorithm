def mini(li):
    mini = li[0]
    for i in range(1,len(li)):
        if li[i] < mini:
            mini = li[i]
    return mini

def Selective(li): #선택정렬 1
    size = len(li)
    result = []
    while True:
        temp = mini(li)
        result.append(temp)
        li.remove(temp)
        if len(li) == 1:
            result.append(li[0])
            break
    print(result)

Selective([4,32,56,2,33,21,6])

def Selective2(li): #선택정렬 2 -> 새로운 리스트 생성 하지 않고 swap을 이용

    for i in range(len(li)-1):
        mini = i
        for j in range(i+1, len(li)):
            if li[j] < li[mini]:
                mini = j

        li[i], li[mini] = li[mini], li[i]

    print(li)
Selective2([33,5,3.2,67,75,4,79,29])

def Insertion(li):#삽입정렬(내림차순)
    for i in range(len(li)-1):
        L = i
        R = i+1
        while L>=0 and li[L] < li[R]:
            li[L], li[R] = li[R],li[L]
            L -= 1
            R -= 1
    return li
print(Insertion([34,2,45,7,35,4,7]))        
            
            

