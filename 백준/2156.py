import sys
sys.setrecursionlimit(10**6)
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
#i번째 원소를 넣었을때 3유형(i+1,i+2,i+3) 별로 그때그때 최댓값을 나타냄
tmp  = [[-1,-1,-1] for _ in range(n)]
def sol(i, c, stat):
    if i >= n or stat >= 3:
        return 0
    if tmp[i][c] == -1:
        tmp[i][c] = arr[i]+ max(sol(i+1, 0,stat+1), sol(i+2,1, 1),sol(i+3,2,1))
    return tmp[i][c]
t1 = sol(0,0,1)
tmp = [[-1,-1,-1] for _ in range(n)]
t2 = sol(1,0,1)
print(max(t1, t2))

# import sys
# sys.setrecursionlimit(10**6)
# n = int(input())
# #위치별 값
# arr =[]
# #위치별 최대값
# res = []
# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))
# if n== 1:
#     print(arr[0])
# elif n==2:
#     print(arr[0]+arr[1])
# else:
#     res.append(arr[0])
#     res.append(arr[1]+arr[0])
#     res.append(max(max(res[1], res[0]+arr[2]),arr[1]+arr[2]))
#     for i in range(3,n):
#         res.append(max(max(res[i-1],res[i-2]+arr[i]),res[i-3]+arr[i-1]+arr[i]))
#
#     print(res[-1])