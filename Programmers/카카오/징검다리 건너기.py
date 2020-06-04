def check(k, stones, num):
    count = 0 #건너뛴 횟수
    cur = 0 #아직 해당구간(i~i+k)을 건너야하는 남은아이들
    for i in range(len(stones)):
        if count >0:
            cur = stones[i]-(num+cur)+cur
        else:
            cur = stones[i] - num
        if cur <0:
            count +=1
            if count == k:
                return False
        else:
            count = 0
    return True
def solution(stones, k):
    answer = 0
    left = 0
    right= max(stones)
    while left <=right:
        mid = (left+right)//2
        if check(k,stones, mid):
            left = mid+1
            answer = mid
        else:
            right= mid-1
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.8MB)
테스트 2 〉	통과 (0.04ms, 10.8MB)
테스트 3 〉	통과 (0.05ms, 10.7MB)
테스트 4 〉	통과 (0.05ms, 10.7MB)
테스트 5 〉	통과 (0.07ms, 10.8MB)
테스트 6 〉	통과 (0.45ms, 10.8MB)
테스트 7 〉	통과 (1.27ms, 10.9MB)
테스트 8 〉	통과 (1.28ms, 10.9MB)
테스트 9 〉	통과 (1.36ms, 10.9MB)
테스트 10 〉	통과 (0.07ms, 10.9MB)
테스트 11 〉	통과 (0.06ms, 10.8MB)
테스트 12 〉	통과 (0.07ms, 10.8MB)
테스트 13 〉	통과 (0.09ms, 10.8MB)
테스트 14 〉	통과 (0.43ms, 10.8MB)
테스트 15 〉	통과 (1.31ms, 10.8MB)
테스트 16 〉	통과 (1.03ms, 11MB)
테스트 17 〉	통과 (1.31ms, 10.9MB)
테스트 18 〉	통과 (0.05ms, 10.8MB)
테스트 19 〉	통과 (0.07ms, 10.7MB)
테스트 20 〉	통과 (0.11ms, 10.7MB)
테스트 21 〉	통과 (0.53ms, 10.8MB)
테스트 22 〉	통과 (1.25ms, 10.8MB)
테스트 23 〉	통과 (1.97ms, 10.8MB)
테스트 24 〉	통과 (1.17ms, 10.8MB)
테스트 25 〉	통과 (0.05ms, 10.8MB)
효율성  테스트
테스트 1 〉	통과 (610.52ms, 161MB)
테스트 2 〉	통과 (716.34ms, 160MB)
테스트 3 〉	통과 (780.65ms, 162MB)
테스트 4 〉	통과 (340.38ms, 160MB)
테스트 5 〉	통과 (377.95ms, 161MB)
테스트 6 〉	통과 (399.12ms, 162MB)
테스트 7 〉	통과 (768.94ms, 161MB)
테스트 8 〉	통과 (862.12ms, 162MB)
테스트 9 〉	통과 (841.05ms, 161MB)
테스트 10 〉	통과 (849.96ms, 161MB)
테스트 11 〉	통과 (813.73ms, 161MB)
테스트 12 〉	통과 (898.74ms, 160MB)
테스트 13 〉	통과 (434.78ms, 160MB)
테스트 14 〉	통과 (345.82ms, 159MB)
'''