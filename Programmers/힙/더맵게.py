'''
문제 설명)
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항)
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
'''

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) > 1:
        t1,t2 = heapq.heappop(scoville) , heapq.heappop(scoville)
        if t1>=K:
            heapq.heappush(scoville,t1)
            heapq.heappush(scoville,t2)
            break
        cnt += 1
        new_t = t1+(t2*2)
        heapq.heappush(scoville, new_t)
    tmp = heapq.heappop(scoville)
    if tmp<K:
        return -1
    return cnt

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.70ms, 10.2MB)
테스트 7 〉	통과 (0.66ms, 10.1MB)
테스트 8 〉	통과 (0.08ms, 10.3MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.50ms, 10.2MB)
테스트 11 〉	통과 (0.33ms, 10.2MB)
테스트 12 〉	통과 (1.11ms, 10.2MB)
테스트 13 〉	통과 (0.61ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.82ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (181.92ms, 16.2MB)
테스트 2 〉	통과 (388.85ms, 21.9MB)
테스트 3 〉	통과 (1887.25ms, 49.8MB)
테스트 4 〉	통과 (134.68ms, 15MB)
테스트 5 〉	통과 (1643.85ms, 51.9MB)
'''