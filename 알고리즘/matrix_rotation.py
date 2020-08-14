#N*N 배열 회전하기
#input: N (N*N배열)

def rotation(target, N):
    new_arr = [[0 for _ in range(N)] for __ in range(N)]
    
    #default: 반시계(3번돌리면 시계)
    for i in range(N):
        for j in range(N):
            new_arr[N-1-j][i] = target[i][j]
    return new_arr

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))

print("before")
for n in range(N):
    print(arr[n])

print()

#시계
# for _ in range(3):
#     arr = rotation(arr,N)

#반시계
arr = rotation(arr,N)

print("after")
for n in range(N):
    print(arr[n])

'''
입력)
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

출력)
before
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 16]

after
[4, 8, 12, 16]
[3, 7, 11, 15]
[2, 6, 10, 14]
[1, 5, 9, 13]
'''