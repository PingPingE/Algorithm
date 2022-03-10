'''
문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항
차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

입출력 예
routes	return
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2

입출력 예 설명
-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.
-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.
'''

from collections import defaultdict


def solution(routes):
    N = len(routes)
    r_dict = defaultdict(set)
    num = 0

    for s, e in routes:
        for n in range(s, e + 1):
            r_dict[n].add(num)
        num += 1

    sorted_dict = sorted(r_dict, key=lambda x: len(r_dict[x]), reverse=True)

    def check(c_count):
        remain = c_count
        current = set()
        for spot in sorted_dict:
            if len(current | r_dict[spot]) > len(current):
                remain -= 1
                break
        return False

    l, r = 0, N
    while l <= r:
        m = (l + r) // 2
        if check(m):
            r = m - 1
        else:
            l = m + 1
    return r