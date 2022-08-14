'''
문제
개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수)
첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.
아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)

이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.
위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)

하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.

동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)
다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

출력
첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.
'''
import sys
from collections import Counter
N,H= map(int, input().split())
info = {'bottom':[], 'top':[]}

#석순: bottom, 종유석: top
for n in range(1, N+1):
    if n%2:
        info['bottom'].append(int(sys.stdin.readline()))
    else:
        info['top'].append(int(sys.stdin.readline()))

bottom_counter = Counter(info['bottom'])
top_counter = Counter(info['top'])

ans = [N+2 for _ in range(H+1)]
for h in range(1,H+1): #종유석 >= h, 석순 >= H-h 개수 카운트
    b_count, t_count =0,0

    for value in range(h,H+1):
        try:
            t_count += top_counter[value]
        except:
            continue

    for value in range(H-h+1, H+1):
        try:
            b_count += bottom_counter[value]
        except:
            continue
    ans[h] = b_count + t_count

min_value = min(ans)
print(min_value, len(list(filter(lambda x: x==min_value, ans))))
