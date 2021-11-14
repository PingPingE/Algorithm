'''

[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
개발자 출신으로 세계 최고의 갑부가 된 어피치는 스트레스를 받을 때면 이를 풀기 위해 오프라인 매장에 쇼핑을 하러 가곤 합니다.
어피치는 쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있습니다.
어느 날 스트레스를 풀기 위해 보석 매장에 쇼핑을 하러 간 어피치는 이전처럼 진열대의 특정 범위의 보석을 모두 구매하되 특별히 아래 목적을 달성하고 싶었습니다.
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
예를 들어 아래 진열대는 4종류의 보석(RUBY, DIA, EMERALD, SAPPHIRE) 8개가 진열된 예시입니다.
진열대 번호	1	2	3	4	5	6	7	8
보석 이름	DIA	RUBY	RUBY	DIA	DIA	EMERALD	SAPPHIRE	DIA
진열대의 3번부터 7번까지 5개의 보석을 구매하면 모든 종류의 보석을 적어도 하나 이상씩 포함하게 됩니다.
진열대의 3, 4, 6, 7번의 보석만 구매하는 것은 중간에 특정 구간(5번)이 빠지게 되므로 어피치의 쇼핑 습관에 맞지 않습니다.
진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems가 매개변수로 주어집니다. 이때 모든 보석을 하나 이상 포함하는 가장 짧은 구간을 찾아서 return 하도록 solution 함수를 완성해주세요.
가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.

[제한사항]
gems 배열의 크기는 1 이상 100,000 이하입니다.
gems 배열의 각 원소는 진열대에 나열된 보석을 나타냅니다.
gems 배열에는 1번 진열대부터 진열대 번호 순서대로 보석이름이 차례대로 저장되어 있습니다.
gems 배열의 각 원소는 길이가 1 이상 10 이하인 알파벳 대문자로만 구성된 문자열입니다.

'''

#파라메트릭 서치로 조건을 만족하는 가장 작은 윈도우 사이즈를 구하는 방식으로 구현함
from collections import defaultdict
def solution(gems):
    N = len(gems)
    set_gems = set(gems)
    kind_N = len(set_gems)

    if N == kind_N:
        return [1, N]

    def sliding_window(size):
        s, e = 0, size
        cnt = defaultdict(int)
        for i in range(e):
            cnt[gems[i]] += 1

        while s <= e and e < N:
            if len(cnt) == kind_N and all(cnt.values()):
                return [s + 1, e]

            cnt[gems[s]] -= 1
            cnt[gems[e]] += 1
            s += 1
            e += 1

        if len(cnt) == kind_N and all(cnt.values()):
            return [s + 1, e]

        return (-1, -1)

    l, r = 0, N
    ans = [1, N]
    while l <= r:
        m = (l + r) // 2
        start, end = sliding_window(m)
        if start == -1:
            l = m + 1
        else:
            ans = [start, end]
            r = m - 1
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.25ms, 10.3MB)
테스트 3 〉	통과 (0.46ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.32ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (2.13ms, 10.3MB)
테스트 9 〉	통과 (2.63ms, 10.4MB)
테스트 10 〉	통과 (1.85ms, 10.4MB)
테스트 11 〉	통과 (2.73ms, 10.5MB)
테스트 12 〉	통과 (5.48ms, 10.3MB)
테스트 13 〉	통과 (7.98ms, 10.4MB)
테스트 14 〉	통과 (13.38ms, 10.5MB)
테스트 15 〉	통과 (13.99ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (16.77ms, 10.6MB)
테스트 2 〉	통과 (55.04ms, 10.7MB)
테스트 3 〉	통과 (43.90ms, 11.1MB)
테스트 4 〉	통과 (52.04ms, 12.1MB)
테스트 5 〉	통과 (179.97ms, 11.9MB)
테스트 6 〉	통과 (106.48ms, 12.2MB)
테스트 7 〉	통과 (347.28ms, 12.7MB)
테스트 8 〉	통과 (347.00ms, 13MB)
테스트 9 〉	통과 (157.61ms, 13.5MB)
테스트 10 〉	통과 (289.17ms, 13.6MB)
테스트 11 〉	통과 (883.21ms, 14.5MB)
테스트 12 〉	통과 (298.39ms, 16MB)
테스트 13 〉	통과 (1946.99ms, 16.7MB)
테스트 14 〉	통과 (1355.72ms, 16.9MB)
테스트 15 〉	통과 (2188.64ms, 17.9MB)
'''


#삽질 기록
def try1(gems):
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



from collections import defaultdict
from functools import reduce
def try2(gems):
    N = len(gems)
    set_gems = set(gems)
    kind_N = len(set_gems)
    cnt_arr = [0 for _ in range(kind_N)]
    #보석이름 인덱싱 => 근데 이름 최대 길이가 10이라(별로 길지 않은편) 굳이 안해도..? (오히려 이것때문에 시간초과가 나는것 같기도)
    name = {}

    if N == kind_N:
        return [1, N]

    for e, gem in enumerate(set_gems):
        name[gem] = e

    def multiply(arr):
        return reduce(lambda x, y: x * y, arr)

    def sliding_window(size, arr):
        s, e = 0, size

        for i in range(e):
            arr[name[gems[i]]] += 1

        while s <= e and e < N:
            print(s,e,size,"arr:", arr)
            if multiply(arr)>0:
                return [s + 1, e]

            arr[name[gems[s]]] -= 1
            arr[name[gems[e]]] += 1
            s += 1
            e += 1

        if multiply(arr) > 0:
            return [s + 1, e]

        return (-1, -1)

    l, r = 0, N
    ans = [1, N]
    while l <= r:
        m = (l + r) // 2
        start, end = sliding_window(m,cnt_arr[:])
        if start == -1:
            l = m + 1
        else:
            ans = [start, end]
            r = m - 1
    return ans



