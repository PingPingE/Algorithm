#10845번) 큐

N = int(input())
arr = []
for i in range(N):
    s= input().split()
    if 'push' in s:
        arr.append(int(s[1]))
    elif 'pop' in s:
        if len(arr)==0:
            print('-1')
        else:
            print(arr[0])
            del arr[0]
    elif 'size' in s:
        print(len(arr))
    elif 'empty' in s:
        if len(arr) != 0:
            print('0')
        else:
            print('1')
    elif 'front' in s:
        if len(arr) == 0:
            print('-1')
        else:
            print(arr[0])

    elif 'back' in s:
        if len(arr)==0:
            print('-1')
        else:
            print(arr[len(arr)-1])
'''
C++은 배열을 사용해서 값이 뒤로 들어오기만하고 앞으로 빠져나가지 않아 rear, front와 같은 변수가 필요했지만
파이썬은 리스트를 사용해서 앞뒤로 값이 들어오고 빠져나가기 때문에 a[0], a[len(a)-1]을 사용할 수 있다.
'''
        
