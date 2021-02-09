'''
문제)
하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

3 : 3 (한 가지)
41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
53 : 5+7+11+13+17 = 53 (두 가지)
하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다.
또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

출력)
첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.
'''
def get_primes(N):
    check = [0 for _ in range(N+1)]#0: 소수, 1: 소수X
    primes =[]
    for i in range(2,N+1):
        if check[i]: continue
        primes.append(i)
        for j in range(i,N+1,i): #소수가 아님을 표시
            check[j] =1
    return primes

from collections import deque
N = int(input())
primes = get_primes(N)

#sol1 bfs : 232744kb	752ms
que = deque()
for i in range(len(primes)):
    if primes[i]>N: break
    que.append([i,primes[i]]) #인덱스, cur_sum
cnt = 0
while que:
    idx, cur_sum = que.popleft()
    if cur_sum == N:
        cnt += 1
        continue
    if idx+1<len(primes) and cur_sum+primes[idx+1] <=N:
        que.append([idx+1, cur_sum+primes[idx+1]])
print(cnt)

#sol2 two pointer: 167500kb 760ms -> 메모리는 확실히 줄어들었다.
cnt =0
s,e=0,0
sum = 0
while s<=e and e<len(primes):
    if sum+primes[e] <N:
        sum += primes[e]
        e+=1
    elif sum+primes[e] == N:
        cnt +=1
        sum -= primes[s]
        s+=1
    else:
        sum-=primes[s]
        s+=1
print(cnt)
