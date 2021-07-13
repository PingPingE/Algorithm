#시도 중
import re, sys
sys.setrecursionlimit(10 ** 8)
def solution(strs, t):
    INF = 987654321
    ans = INF

    def sol(cur_str, cnt, idx):
        nonlocal ans
        # print(cur_str)
        if not cur_str:
            ans = min(ans, cnt)
            return

        o_len = len(cur_str)
        for i in range(idx, len(strs)):
            tmp = re.sub(strs[i], '', cur_str)
            sol(tmp, cnt + (o_len - len(tmp)) // len(strs[i]), i + 1)
        return

    sol(t, 0, 0)
    return -1 if ans == INF else ans