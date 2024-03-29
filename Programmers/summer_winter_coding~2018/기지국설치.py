'''
문제 설명)
N개의 아파트가 일렬로 쭉 늘어서 있습니다. 이 중에서 일부 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
기술이 발전해 5g 수요가 높아져 4g 기지국을 5g 기지국으로 바꾸려 합니다. 그런데 5g 기지국은 4g 기지국보다 전달 범위가 좁아, 4g 기지국을 5g 기지국으로 바꾸면 어떤 아파트에는 전파가 도달하지 않습니다.

예를 들어 11개의 아파트가 쭉 늘어서 있고, [4, 11] 번째 아파트 옥상에는 4g 기지국이 설치되어 있습니다.
만약 이 4g 기지국이 전파 도달 거리가 1인 5g 기지국으로 바뀔 경우 모든 아파트에 전파를 전달할 수 없습니다.
(전파의 도달 거리가 W일 땐, 기지국이 설치된 아파트를 기준으로 전파를 양쪽으로 W만큼 전달할 수 있습니다.)

초기에, 1, 2, 6, 7, 8, 9번째 아파트에는 전파가 전달되지 않습니다.
기지국설치1_pvskxt.png

1, 7, 9번째 아파트 옥상에 기지국을 설치할 경우, 모든 아파트에 전파를 전달할 수 있습니다.
기지국설치2_kml0pb.png

3개의 아파트보다 더 많은 아파트 옥상에 기지국을 설치할 경우에도 모든 아파트에 전파를 전달할 수 있습니다.
기지국설치3_xhv7r3.png

이때, 우리는 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 합니다. 위의 예시에선 최소 3개의 아파트 옥상에 기지국을 설치해야 모든 아파트에 전파를 전달할 수 있습니다.

아파트의 개수 N, 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations, 전파의 도달 거리 W가 매개변수로 주어질 때,
모든 아파트에 전파를 전달하기 위해 증설해야 할 기지국 개수의 최솟값을 리턴하는 solution 함수를 완성해주세요

제한사항)
N: 200,000,000 이하의 자연수
stations의 크기: 10,000 이하의 자연수
stations는 오름차순으로 정렬되어 있고, 배열에 담긴 수는 N보다 같거나 작은 자연수입니다.
W: 10,000 이하의 자연수
'''
def solution(n, stations, w):
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
        # if s > i: continue
        #틀린 이유: s>i인 경우도 s를 갱신해줘야지..
        if s >= i:
            s = j + 1
            continue

        e = i - 1
        add_cnt += get_cnt(s, e)
        s = j + 1

    if s < n:
        add_cnt += get_cnt(s, n - 1)
    return add_cnt
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (8.69ms, 11.8MB)
테스트 2 〉	통과 (10.40ms, 11.9MB)
테스트 3 〉	통과 (8.28ms, 11.9MB)
테스트 4 〉	통과 (8.84ms, 11.8MB)
'''


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