'''
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
'''


def solution(citations):
    def check(idx, h_idx): #citations의 [0,idx] 범위내에서 h_idx 초과의 값이 있는지 체크 
        l,r = 0, idx
        while l <=r:
            mid = (l+r)//2
            if citations[mid] > h_idx:
                return False
            l = mid+1
        return True
    
    def get_target(h_idx):#인용횟수가 h_idx미만이기 시작하는 index 반환 
        l,r = 0,total_cnt
        while l<=r:
            mid = (l+r)//2
            if citations[mid] >=h_idx:
                r = mid-1
            else:
                l = mid+1
        return r
        
    answer = 0
    total_cnt = len(citations)
    if total_cnt ==1: return answer
    citations.sort()
    s,e = 0, citations[-1]
    while s<=e:
        h = (s+e)//2
        m = get_target(h)
        if  total_cnt-(m+1)>=h and check(m,h):
            answer = h
            s = h+1
        else:
            e = h-1
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.2MB)
테스트 2 〉	통과 (0.13ms, 10.1MB)
테스트 3 〉	통과 (0.11ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.3MB)
테스트 5 〉	통과 (0.13ms, 10.2MB)
테스트 6 〉	통과 (0.14ms, 10.3MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (0.15ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.14ms, 10.3MB)
테스트 14 〉	통과 (0.13ms, 10.2MB)
테스트 15 〉	통과 (0.14ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
'''