#T1:15분 14초
#T2:28분 14초
#T3:75분 2초 -> 다른 사람 풀이 참고
'''
문제)
어떤 자연수 N은 그보다 작거나 같은 제곱수들의 합으로 나타낼 수 있다. 예를 들어 11=32+12+12(3개 항)이다. 이런 표현방법은 여러 가지가 될 수 있는데,
11의 경우 11=22+22+12+12+12(5개 항)도 가능하다. 이 경우, 수학자 숌크라테스는 “11은 3개 항의 제곱수 합으로 표현할 수 있다.”라고 말한다.
또한 11은 그보다 적은 항의 제곱수 합으로 표현할 수 없으므로, 11을 그 합으로써 표현할 수 있는 제곱수 항의 최소 개수는 3이다.

주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에 그 항의 최소개수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000)

출력)
주어진 자연수를 제곱수의 합으로 나타낼 때에 그 제곱수 항의 최소 개수를 출력한다.

'''
def solution(N): #무조건 맞지만 메모리초과나는 코드(정답 체크용)
    if N==1: print(1)
    elif N==2: print(2)
    else:
        from collections import deque
        res = N
        que = deque()
        que.append((0,0)) #cnt, current
        while que:
            cnt, current = que.popleft()
            if current == N:
                res = min(res, cnt)
                continue
            if cnt >= res: break
            target = 1
            while True:
                if target**2 + current >N: break
                que.append((cnt+1, current+target**2))
                target +=1
        print(res)

#sol1
#제출:132548kb	1400ms
N = int(input())
memo = {i:i for i in range(N+1)}
for i in range(1,N+1):
    j=1
    while i-j*j>=0:#표현가능한 제곱수들
        if memo[i] > memo[i-j*j]+1:#제곱수를 뺀 수의 항 개수 + 해당 제곱수(1번)
            memo[i] = memo[i-j*j]+1
        j+=1
print(memo[N])

#sol2: 필요없는 연산 빼기
#제출:132548kb	772ms -> 시간이 거의 절반으로 축소됨
N = int(input())
memo = {i:i for i in range(N+1)}
for i in range(4,N+1):#4부터 갱신하면 되니까
    j=2 #1은 굳이 X
    while i-j*j>=0:
        if memo[i] > memo[i-j*j]+1:
            memo[i] = memo[i-j*j]+1
        j+=1
print(memo[N])

#sol3: sol2에서 dictionary -> list 변경
#제출: 127688kb	196ms -> list가 값 변경이 더 빠른 것 같다.(둘 다 O(1)이긴함)
N = int(input())
memo = list(i for i in range(N+1))
for i in range(4,N+1):#4부터 갱신하면 되니까
    j=2 #1은 굳이 X
    while i-j*j>=0:
        if memo[i] > memo[i-j*j]+1:
            memo[i] = memo[i-j*j]+1
        j+=1
print(memo[N])

#틀린 코드 -> greedy하게 구현했는데, 무조건 큰 수의 제곱수로 구성되었다고 최소항을 가지는게 아니라서 틀렸다.
import math
N = int(input())
if N == 1: print(1)
elif N==2: print(2)
else:
    cnt = 0
    current = 0
    stat = False
    for i in range(int(math.sqrt(N)), 0, -1):
        while not stat:
            if current+i**2 <=N:
                cnt += 1
                current+= i**2
            else:
                break
            if current == N:
                stat=True
        if stat: break
    print(cnt)

'''
#초기화 과정이 list가 더 빠른가? -> No
import time
def test_list():
    start = time.time()
    l = list(i for i in range(10000000))
    end = time.time()
    return end-start

def test_dict():
    start = time.time()
    l = {i:i for i in range(10000000)}
    end = time.time()
    return end-start
print("list:",test_list())
print("dict:", test_dict())

#list: 0.923494815826416
#dict: 0.7739691734313965
'''

