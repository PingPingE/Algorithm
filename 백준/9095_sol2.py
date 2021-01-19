#T1: 18분 47초
#T2: 31분 47초(13분-> sol1,2)
#T3: -
#sol1: 일반 재귀
#122244kb	112ms
def get_result(cur,target):
    if cur >target: return 0
    if cur == target: return 1
    return get_result(cur+1, target) + get_result(cur+2,target) + get_result(cur+3,target)

T= int(input())
while T:
    T-=1
    print(get_result(0,int(input())))

#sol2: DP로 풀기
#121220kb	100ms
memo = [0 for _ in range(12)]
memo[1] = 1
memo[2] = 2
memo[3] = 4
for i in range(4,12):
    memo[i] = sum(memo[i-3:i])
T= int(input())
while T:
    T-=1
    print(memo[int(input())])
