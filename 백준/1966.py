from collections import deque
def sol(arr):
    que = deque(arr)
    cnt = 0
    while que:
        q= que.popleft()
        stat = True
        #pop 할 수 있는지 check
        for i in range(len(que)):
            if q[0] < que[i][0]:
                que.append(q)
                stat = False
                break
        if stat == True:
            cnt += 1
            if q[1] == 1:
                return cnt


#입력(M)은 0부터, 출력은 1부터
T = int(input())
while T > 0:
    T -= 1
    N, M= list(map(int, input().split()))
    #숫자, 타켓 여부(0: X , 1: 타겟)
    arr = [[0,0] for _ in range(N)]
    j = 0
    for i in list(map(int, input().split())):
        arr[j][0] = i
        if j == M:
            arr[j][1] = 1
        j += 1
    if N ==1 :
        print(1)
    else:
        print(sol(arr))