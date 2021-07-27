#시도 중
import sys
sys.setrecursionlimit(10**8)
def solution(arr):
    N=len(arr)
    memo= [0 for _ in range(N)]
    def sol(idx):
        sum=0
        for i in range(idx,N):
            #'-' 나오면 쪼개기
            if arr[i] =='-':
                tmp = int(arr[i+1])
                ret = sol(i+2)
                return max(sum-tmp+ret, sum-(tmp+ret))
            else:
                if arr[i]=='+': continue
                sum+=int(arr[i])
        return sum
    return sol(0)