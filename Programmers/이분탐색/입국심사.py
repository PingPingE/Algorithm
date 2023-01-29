#이분 탐색: 걸리는 총 시간을 대상으로 이분탐색
def solution(n, times):
    answer = 0
    l= min(times)
    r= l*n
    while l<=r:
        m = (l+r)//2
        cnt = 0
        for t in times:
            cnt += m//t
        if cnt >= n:
            r=m-1
        else:
            l=m+1
    return l

#시간 초과
import heapq
def solution(n, times):
    answer = 0
    target = list((t, t) for t in times)
    heapq.heapify(target)
    while n:
        n-=1
        end_time, time = heapq.heappop(target)
        answer =max(answer, end_time)
        heapq.heappush(target, (end_time+time, time))
    return answer