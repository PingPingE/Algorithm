'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
#sol1) 비트마스킹 121808kb 148ms
def countBits(n):
    count =0
    while n:
        if n&1:
            count += 1
        n>>=1
    return count
N,M = map(int, input().split())
done = []
for i in range(1<<N):
    if countBits(i) == M:
        tmp = []
        for j in range(N):
            if i&1<<j:
                tmp.append(j+1)
        done.append(' '.join(map(str, tmp)))
done.sort()
for d in done:
    print(d)

#sol2) 내장함수 활용 121808kb 152ms
from itertools import combinations
N,M = map(int, input().split())
comb = list(combinations(range(1,N+1),M))
comb.sort()
for c in comb:
    print(' '.join(map(str,c)))