#T1: 5분 53초
#T2: 16분 37초(10분 44초)
#T3: -

#120784kb	104ms
import sys
N = int(input())
plus = list() #양수만
minus = list() #음수만(0포함)
for _ in range(N):
    tmp =int(sys.stdin.readline())
    if tmp <=0:
        minus.append(tmp)
    else:
        plus.append(tmp)
        
plus.sort(reverse=True) #양수 리스트는 내림차순
minus.sort() #음수 리스트는 오름차순
sum =0
p_index=0
m_index=0
while True:
    if p_index>=len(plus) and m_index>=len(minus):
        break
    if p_index<len(plus):
        if p_index+1 < len(plus) and plus[p_index]*plus[p_index+1] > plus[p_index]+plus[p_index+1]: #다음 인덱스 유무 체크 + 곱한게 더한거보다 더 큰지 체크
            sum += plus[p_index]*plus[p_index+1]
            p_index += 2
        else:
            sum += plus[p_index]
            p_index += 1

    if m_index<len(minus):
        if m_index+1 < len(minus):
            sum += minus[m_index]*minus[m_index+1]
            m_index += 2
        else:
            sum += minus[m_index]
            m_index += 1
print(sum)