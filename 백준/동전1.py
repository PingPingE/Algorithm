'''
문제
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

입력
첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.
'''
#메모리 초과
import sys
n, k = map(int, input().split())
n_list = list([0]*(k+1) for _ in range(n+1))
origin_n = [0]

#n_list[i][j]: i까지 사용해서 j를 나타낼 수 있는 경우의 수
for e in range(1,n+1):
    tmp_n = int(sys.stdin.readline())
    n_list[e][tmp_n] = 1
    origin_n.append(tmp_n)

for n1 in range(n):
    for n2 in range(n1+1,k+1):
        n_list[n1][n2] += n_list[n1-1][n2] + n_list[n1][n2-origin_n[n1]]

print(sum(list(li[-1] for li in n_list)))