#풀이 참고: https://programmers.co.kr/questions/17805
def solution(arr):
    i = len(arr) - 1
    sum = 0 # '-'부호가 나타나기 전까지의 연산값
    total_sum = [0, 0]  # index 0: min, 1:max

    #뒤에서부터 보기
    while i >= 0:
        if arr[i] >= '0':
            sum += int(arr[i])

        # 맨뒤에서 여기까지 최솟값,최댓값 갱신
        elif arr[i] == '-':

            #기존 값(tmp_sum)이랑 합치고 - 부호 붙일지, -sum + 기존 값 할지
            # arr[i+1]을 +arr[i+1]로 할지, -arr[i+1]로 할지
            candi = [-(total_sum[1] + sum), -(total_sum[0] + sum), total_sum[0] - sum, total_sum[1] + sum - (2 * int(arr[i + 1]))]
            total_sum[0] = min(candi)
            total_sum[1] = max(candi)

            sum = 0
        i -= 1
        # print(total_sum)
        # print("sum:",sum)
    return total_sum[1] + sum


'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.14ms, 10.3MB)
테스트 2 〉	통과 (0.13ms, 10.3MB)
테스트 3 〉	통과 (0.15ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.3MB)
테스트 5 〉	통과 (0.07ms, 10.2MB)
테스트 6 〉	통과 (0.69ms, 10.2MB)
테스트 7 〉	통과 (0.20ms, 10.3MB)
테스트 8 〉	통과 (0.22ms, 10.4MB)
'''


#======version2(조금 개선)
import sys
sys.setrecursionlimit(10 ** 8)

def cal(a, b, op):
    if op == '+':
        return a + b
    return a - b


def sol(nums, ops, flag, value):
    if len(ops) == 1:
        if flag:#왼쪽(최댓값)
            value = max(value, cal(nums[0], nums[1], ops[0]))
        else:#오른쪽(최솟값)
            value = min(value, cal(nums[0], nums[1], ops[0]))
        return value

    if len(nums) == 1:
        return nums[0]

    for i in range(len(ops)):
        tmp = cal(nums[i], nums[i + 1], ops[i])
        v = sol(nums[:i] + [tmp] + nums[i + 2:], ops[:i] + ops[i + 1:], flag, value)
        value = v

    return value


def solution(arr):
    INF = 987654321
    ans = -INF
    nums, ops = [int(arr[i]) for i in range(0, len(arr), 2)], [arr[i] for i in range(1, len(arr), 2)]

    # 1. -만 골라낸다.
    # 2. 그 - 기준으로 쪼갠다
    # 3. 왼쪽은 max값 / 오른쪽은 min값을 도출해서 빼준다. -> ans 갱신

    for i in range(len(ops)):
        if ops[i] == '-':
            left = sol(nums[:i + 1], ops[:i], 1, -INF)
            right = sol(nums[i + 1:], ops[i + 1:], 0, INF)
            ans = max(ans, left - right)

    return sum(nums) if ans == -INF else ans


'''
정확성  테스트
테스트 1 〉	통과 (551.20ms, 10.4MB)
테스트 2 〉	통과 (80.79ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (1304.31ms, 10.4MB)
테스트 6 〉	통과 (1302.82ms, 10.5MB)
테스트 7 〉	통과 (139.46ms, 10.5MB)
테스트 8 〉	통과 (645.93ms, 10.5MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	통과 (0.07ms, 10.5MB)
테스트 6 〉	통과 (0.06ms, 10.5MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''

# =====version 1
import sys

sys.setrecursionlimit(10 ** 8)
ans = -987654321


def cal(a, b, op):
    if op == '+':
        return a + b
    return a - b


def sol(nums, ops):
    global ans
    if len(ops) == 1:
        ans = max(ans, cal(nums[0], nums[1], ops[0]))
        return

    for i in range(len(ops)):
        tmp = cal(nums[i], nums[i + 1], ops[i])
        sol(nums[:i] + [tmp] + nums[i + 2:], ops[:i] + ops[i + 1:])


def solution(arr):
    # 숫자와 연산자 분리
    nums, ops = [int(arr[i]) for i in range(0, len(arr), 2)], [arr[i] for i in range(1, len(arr), 2)]
    sol(nums, ops)
    return ans


'''
정확성  테스트
테스트 1 〉	통과 (5641.36ms, 10.4MB)
테스트 2 〉	통과 (5656.25ms, 10.4MB)
테스트 3 〉	통과 (5514.34ms, 10.4MB)
테스트 4 〉	통과 (5534.46ms, 10.5MB)
테스트 5 〉	통과 (5668.97ms, 10.4MB)
테스트 6 〉	통과 (5643.12ms, 10.4MB)
테스트 7 〉	통과 (5611.70ms, 10.5MB)
테스트 8 〉	통과 (5755.72ms, 10.4MB)
테스트 9 〉	통과 (0.35ms, 10.5MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
'''