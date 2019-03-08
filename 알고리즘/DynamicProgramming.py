#Dynamic programming
def fib(n):
    if n > 0 and arr[n] != 0: #arr에 있는 값이면
        return arr[n] #계산 하지 않고 바로 arr값 return
    elif n==0:
        return arr[n]
    else: #arr에 없는 값이면
        if n==1 or n==2:
            arr[n] = 1
        else:
            arr[n] = fib(n-1)+fib(n-2) #재귀호출로 계산

    return arr[n]

arr = []
n = int(input()) #구할 값(fib(n))

#arr 0으로 초기화
for i in range(n+1):
    arr.append(0)

print(fib(n))



