'''
문제
언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다.
최고만을 지향한다는 기업의 이념에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다.
즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다. 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다. 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

출력
각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.
'''
#220712kb	3968ms
# import sys
# T= int(input())
# while T:
#     T-=1
#     N = int(input())
#     #1차 순위 기준으로 정렬(stack)
#     arr = sorted(list(tuple(map(int, sys.stdin.readline().split())) for _ in range(N)), key=lambda x: -x[0])
#
#     #1차 순위가 높은 지원자(앞에서 먼저 pop된 애들)들의 2차 순위 중 가장 높은 순위
#     min_rank = N
#     cnt = 0
#
#     while arr:
#         rank1, rank2 =  arr.pop()
#         if rank2 <= min_rank:
#             cnt+=1
#             min_rank = rank2
#             continue
#         else: #1차도 낮은데 2차도 min_rank보다 낮은 경우
#             continue
#     print(cnt)

'''
solution2
자료 구조 변경
기존: list(tuple(int)) -> 변경 후: list(int)

즉 리스트의 index가 1차 rank, 각 원소가 2차 rank
'''
#131316kb	1132ms
import sys
T= int(input())
while T:
    T-=1
    N = int(input())
    arr = [0 for _ in range(N+1)]
    for _ in range(N):
        a,b = map(int,sys.stdin.readline().split())
        arr[a] = b
    min_rank = N
    cnt = 0
    for i in range(1,N+1):
        if arr[i] <= min_rank:
            min_rank=arr[i]
            cnt+=1
    print(cnt)
