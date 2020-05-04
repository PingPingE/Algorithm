'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

'''
#29380kb 64ms
import sys
sys.setrecursionlimit(10**6)
def cal(m,x):
    if x not in m:
        if x%3==0:
            tmp1 = cal(m,x/3)+1
        elif (x-1)%3 == 0:
            tmp1 = cal(m,(x-1)/3)+2
        elif (x-2)%3 ==0:
            tmp1 = cal(m,(x-2)/3)+3
        if x%2 == 0:
            tmp2 = cal(m,x/2)+1
        elif (x-1)%2 == 0:
            tmp2 = cal(m,(x-1)/2)+2
        m[x] = min(tmp1, tmp2)
    return m[x]
print(cal({1:0, 2:1, 3:1, 4:2},int(input())))