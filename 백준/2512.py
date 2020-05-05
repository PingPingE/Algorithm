import sys
#122476kb	184ms
N = int(input())
budgets = list(map(int ,sys.stdin.readline().split()))
M = int(input())
answer = 0
budgets.sort()
right = budgets[-1]
left = 0
while right>=left:
    mid =(right+left)//2
    target_num = len(list(filter(lambda x: x>mid, budgets)))
    total = sum(budgets[:len(budgets)-target_num])+mid*target_num
    if total <=M:
        answer = mid
        left = mid+1
    else:
        right = mid-1
print(answer)