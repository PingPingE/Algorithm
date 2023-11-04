'''
Calculate the values of counters after applying all alternating operations:
- increase counter by 1;
- set value of all counters to current maximum.


0으로 초기화된 N 크기의 counter에 조건별 연산을 수행한 후의 상태 리턴
조건1) 리스트 A 원소 값(a) <= N인 경우
- counter[a]+=1
조건2) 리스트 A 원소 값 > N인 경우
- counter의 max 값으로 모두 채우기
'''

def solution(N, A):
    # Implement your solution here
    counter = [0] * N
    check_max = 0  # 저장한 max값
    cur_max = 0  # 현재 max 값
    for a in A:
        if a <= N:
            counter[a - 1] = max(counter[a - 1], check_max) + 1
            cur_max = max(cur_max, counter[a - 1])
        else:
            check_max = cur_max
    return [c if c >= check_max else check_max for c in counter]
