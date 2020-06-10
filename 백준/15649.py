'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.


'''
#128312kb	228ms
from itertools import permutations
def countBits(target):
    count = 0
    while target:
        if target&1:
            count +=1
        target >>= 1
    return count
N, M = map(int, input().split())
ans = []
for i in range(1<<N):
    if countBits(i) == M:
        tmpSet = []
        for j in range(N):
            if i&1<<j:
                tmpSet.append(j+1)
        for p in permutations(tmpSet,M):
            ans.append(p)
ans.sort()
for a in ans:
    print(' '.join(map(str, a)))


