from collections import deque
def cal(c,curA, prev):
    global A
    if c == 0:
        #뒤에꺼랑
        if curA == 0:
            return A[curA]+A[curA+1]
        #앞에꺼랑
        return prev+A[curA]
    elif c== 1:
        if curA == 0:
            return A[curA] - A[curA + 1]
        return prev - A[curA]
    elif c==2:
        if curA == 0:
            return A[curA] * A[curA + 1]
        return prev * A[curA]
    else:
        if curA == 0:
            #원래 코드는 각 분자, 분모 모두 음수인지 확인해서 계산했음
            #코드는 더 간결해졌지만 원래대로하는게 더 빠르고 메모리 덜 차지함
            return int(A[curA]/A[curA+1])
        return int(prev/A[curA])

N = int(input())
A = list(map(int,input().split()))
#+,-,*,//의 개수
op = list(map(int, input().split()))
#최대, 최소
res = [0,0]
stat = 0
que = deque()
tmp = op[:]
#현재op, 현재까지의 값, A 인덱스
que.append([tmp, 0, 0])
while que:
    cop, cres, a = que.popleft()
    if a>N-1:
        if stat == 0:
            res[0] = cres
            res[1] = cres
            stat += 1
        else:
            res[0] = max(res[0],cres)
            res[1] = min(res[1],cres)
        continue

    for c in range(len(cop)):
        if cop[c]>0:
            tmp = cop[:]
            tmp[c] -= 1
            if a== 0:
                que.append([tmp, cal(c, a, cres), a + 2])
            else:
                que.append([tmp, cal(c,a, cres),a+1])

print(res[0])
print(res[1])

#숏코딩
# import sys
#
# n = int(sys.stdin.readline())
# num_list = list(map(int, sys.stdin.readline().split()))
# a, b, c, d = map(int, sys.stdin.readline().split())
# max_num, min_num = -sys.maxsize + 1, sys.maxsize
#
#
# def solution(num, i, add, minus, multiply, divide):
# 	global n, max_num, min_num
# 	if i == n:
# 		max_num = max(max_num, num)
# 		min_num = min(min_num, num)
# 		return
# 	else:
# 		if add:
# 			solution(num + num_list[i], i + 1, add - 1, minus, multiply, divide)
# 		if minus:
# 			solution(num - num_list[i], i + 1, add, minus - 1, multiply, divide)
# 		if multiply:
# 			solution(num * num_list[i], i + 1, add, minus, multiply - 1, divide)
# 		if divide:
# 			solution(int(num / num_list[i]), i + 1, add, minus, multiply, divide - 1)
#
#
# solution(num_list[0], 1, a, b, c, d)
# print(max_num)
# print(min_num)
