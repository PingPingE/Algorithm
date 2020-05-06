'''
두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열  A가 있다. 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다.
예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자.

A =>  < < < > < < > < >

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다.

3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다.
그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다.

5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다.
앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 선택된 숫자는 모두 달라야 한다.

'''
k = int(input())
char = list(input().split())
max_list = list(map(str, range(10)))
min_list = list(map(str, range(9,-1,-1)))
minn, maxx = min_list.pop(), max_list.pop()
memo=[0,0]
#121808kb	148ms
for i in range(len(char)):
    if char[i] == '<':
        memo[1] = 0
        memo[0] += 1
        tmp1 = maxx[len(maxx)-memo[0]:]
        maxx= maxx[:-memo[0]]
        maxx += max_list.pop()
        maxx+=tmp1

        minn += min_list.pop()
    else:
        memo[0] = 0
        memo[1] += 1
        tmp2 = minn[len(minn)-memo[1]:]
        minn = minn[:-memo[1]]
        minn += min_list.pop()
        minn += tmp2

        maxx += max_list.pop()
print(f"{maxx}\n{minn}")

