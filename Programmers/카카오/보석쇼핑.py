def solution(gems):
    N = len(gems)
    cnt = {}
    e = 0
    for i, gem in enumerate(gems):
        if gem not in cnt:
            # 가장 마지막에 들어온 gem 위치
            e = i
            cnt[gem] = [0 for _ in range(N)]
        
        for k in cnt:
            if k == gem:
                cnt[k][i] = cnt[k][i - 1] + 1
            else:
                cnt[k][i] = cnt[k][i - 1]

    if e == 0:
        return [1, 1]

    r, l = 0, e + 1

    if l == N:
        return [1, N]

    while r <= l:
        m = (r + l) // 2

        for k in cnt:
            # 해당구간에 없는 보석 체크
            if cnt[k][m] - cnt[k][m - 1] == 0 and cnt[k][e] == cnt[k][m]:
                l = m - 1
                break
        else:
            r = m + 1

    return [r, e + 1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))