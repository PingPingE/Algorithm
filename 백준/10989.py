'''
수 정렬하기 3
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

*메모리제한: 8MB
'''
#32288kb	9564ms
import sys
from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(sys.stdin.realdine())):
    dic[int(sys.stdin.readline())] += 1
k = sorted(dic)
for d_k in k:
    for _ in range(dic[d_k]):
        print(d_k)
