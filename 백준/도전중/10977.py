'''
문제)
데브시스터즈의 사내 레스토랑 스테이지 2에서는 총 M 가지의 음식을 만들 수 있으며 각 음식에는 1번부터 M 번까지 번호가 붙어 있다.
데브시스터즈 직원들은 매 끼니마다 스테이지 2에서 제공한 N 가지의 음식 중 하나를 골라서 먹을 수 있으며 스테이지 2에서 끼니마다 제공하는 음식은 다음과 같이 정해진다.
지난 끼니에 K 번 음식을 제공했다면, 이번 끼니에는 K+1번 음식을 제공한다. 단, 지난 끼니에 M 번 음식이 제공된 경우에는 이번 끼니에 1번 음식을 제공한다.
데브시스터즈에 처음 입사한 영희는 이 사실을 알고 스테이지 2에서 제공하는 음식의 조합이 몇 가지 인지 궁금해졌다.
그러나 영희는 일이 바쁘기 때문에 여러분에게 이번 끼니에 제공한 음식을 알려주면서 도움을 요청하였다. 여러분이 영희를 도와 음식 조합의 가짓수를 세어 주자.

입력)
첫 번째 줄에 테스트 케이스의 개수 T 가 주어진다.
각 케이스의 첫 줄에 스테이지2에서 만들 수 있는 음식의 가짓수 M, 끼니마다 제공되는 음식의 가짓수 N(1 ≤ N ≤ M ≤ 1,000,000)이 주어진다.
그 다음 N줄에 이번 끼니에 나온 음식들의 번호 xi (1 ≤ xi ≤ M)가 주어진다. 이 번호들은 모두 다르며 오름차순으로 정렬되어 있다.

출력)
각 테스트 케이스마다 한 줄씩 음식 조합의 가짓수를 출력한다.
'''
#시간초과
import sys
T = int(input())
while T:
    T-= 1
    candi = set()
    M,N = map(int, sys.stdin.readline().split())
    arr =[int(sys.stdin.readline())]
    arr_p = arr.append
    for e in range(N-1):
        arr_p(int(sys.stdin.readline()))
        target= M-arr[-1]+arr[0]
        candi.add(target)
    candi = sorted(candi)
    for c in candi:
        for a in arr:
            target =(a+c)
            if target>M:
                if target%M > 0:
                    target %= M
                else:
                    target= M
            if target not in arr:
                break
        else:
            print(c)
            break