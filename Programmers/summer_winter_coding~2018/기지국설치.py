#몇 개 틀리는 코드
def solution2(n, stations, w):
    st_li = []

    for i in stations:
        # (전파 시작점, 전파 끝지점)
        st_li.append((max(0, i - 1 - w), min(n - 1, i - 1 + w)))

    def get_cnt(s, e):
        for t in range(n):
            if e - s + 1 <= t * (2 * w + 1):
                return t

    add_cnt = 0  # 추가 설치 개수
    s, e = 0, 0
    for i, j in sorted(st_li):
        if s > i: continue
        if s == i:
            s = j + 1
            continue

        e = i - 1
        add_cnt += get_cnt(s, e)
        s = j + 1

    if s < n:
        add_cnt += get_cnt(s, n - 1)

    return add_cnt


# 효율성에서 걸리는 코드
def solution1(n, stations, w):
    state = [0 for _ in range(n)]

    # index-1
    # 이렇게 표시하는 것 보다 차라리 (시작점, 끝점)을 저장하는 것이 더 나을듯
    for i in stations:
        for k in range(w + 1):
            state[max(0, i - 1 - k)] = 1
            state[min(n - 1, i - 1 + k)] = 1

    def find_0(start):
        for i in range(start, n):
            if state[i] == 0:
                return i
        return n

    def get_cnt(s, e):
        for t in range(1, n):
            if e - s <= t * (2 * w + 1):
                return t

    s = find_0(0)
    e = s
    add_cnt = 0  # 추가 설치 개수

    while e < n:
        if state[e] == 1:
            add_cnt += get_cnt(s, e)
            s = find_0(e)
            e = s

        else:
            e += 1
    if s < n:
        add_cnt += get_cnt(s, e)

    return add_cnt