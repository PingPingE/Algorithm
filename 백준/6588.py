'''
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.

각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)

입력의 마지막 줄에는 0이 하나 주어진다.
'''
import sys
prime ={}
check = [0 for _ in range(1000005)]
#에라토스테네스의 체
for i in range(2,1000001):
    if check[i]:
        continue
    prime[i] = prime.get(i, 0) +1
    for j in range(i*i,1000001,i):
        check[j] = 1
#211516kb	316ms
num = int(sys.stdin.readline())
p_key = sorted(prime)
while num!=0:
    i=1
    stat =False
    while p_key[i] < num:
        if num-p_key[i] in prime:
            print(f"{num} = {p_key[i]} + {num-p_key[i]}")
            stat =True
            break
        i+=1
    if stat is False:
        print("Goldbach's conjecture is wrong.")
    num = int(sys.stdin.readline())