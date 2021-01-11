'''
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과,
N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며,
그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

출력
듣보잡의 수와 그 명단을 사전순으로 출력한다.
'''
#131200kb	324ms
N, M = map(int, input().split())
s = set() #듣도 못한 사람의 명단
ans = []
for _ in range(N):
    s.add(input())

for _ in range(M): #보도 못한 사람 명단을 확인하며 set s에 있는지 확인->있으면 list ans에 담기
    tmp = input()
    if tmp in s:
        ans.append(tmp)
        
print(len(ans))
ans.sort()
for a in ans:
    print(a)

#sol2: list ans 안에 set 2개를 받아서 합집합 연산 후 sorting
#135504kb	316ms
N, M = map(int, input().split())
ans = sorted({input() for _ in range(N)} & {input() for _ in range(M)})
print(len(ans))
print('\n'.join(ans))
