'''
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

#T1:13분 51초
#T2:1시간 30분 32초 (1시간 16분 41초)
#T3:1시간 32분 43초 (2분 11초) : int() -> math.ceil()

#139344kb	124ms
import math
N = int(input())
memo = ["***","* *","***"] #상, 중, 하
for i in range(1,math.ceil(math.log(N,3))):
    tmp = [memo[i][:] for i in range(len(memo))] #사본
    space = " " * (3**i) #가운데 공백
    high = []
    mid = []
    for j in range(3):#기존꺼 상중하 모두 돌면서
        for n in tmp[j].split('\n'):
            if n == "": continue
            high.append(n*3) #세 개 추가
            mid.append(n + space + n) #가운데 공백 추가
            high.append("\n")
            mid.append("\n")
    memo[0] = "".join(high)
    memo[1] = "".join(mid)
    memo[2] = "".join(high[:-1]) #마지막은 개행 없애기
if N == 3:
    print("\n".join(memo))
else:
    print("".join(memo))
    # print(len(memo[0]), len(memo[1]), len(memo[-1]),sum(len(a) for a in memo)-(N-1), N*N)