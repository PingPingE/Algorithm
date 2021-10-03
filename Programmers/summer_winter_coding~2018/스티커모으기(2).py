#시도중 
import sys
sys.setrecursionlimit(10**8)
def solution(sticker):
    answer = 0
    copy = sticker[:]
    N = len(sticker)

    def dfs(ans, sum_):
        nonlocal answer, copy
        if sum_ == 0:
            answer = max(ans, answer)
            return

        for i in range(N):
            if copy[i] != -1:
                right = i + 1 if i + 1 < N else 0
                left = i - 1
                flag = [0,0]

                copy[i] = -1
                if copy[left] != -1:
                    copy[left] = -1
                    flag[0] =1
                    
                if copy[right] != -1:
                    copy[right] = -1
                    flag[1] = 1

                dfs(ans + sticker[i], sum_-(sticker[i]+flag[0]*sticker[left]+flag[1]*sticker[right]))

                copy[i] = sticker[i]
                if flag[0]:
                    copy[left] = sticker[left]
                if flag[1]:
                    copy[right] = sticker[right]

    dfs(0, sum(copy))
    return answer
