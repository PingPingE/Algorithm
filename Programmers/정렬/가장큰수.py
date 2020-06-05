def solution(numbers):
    answer = ''
    m = {str(i):[] for i in range(0,10)}
    for n in numbers:
        m[str(n)[0]].append(str(n))
    for nn in range(9,-1,-1):
        #value정렬: #9 vs 998=> 999 vs 998
        m[str(nn)].sort(reverse= True, key = lambda x: ((x*3)[:4])) 
        for mm in m[str(nn)]:
            answer += mm
    if answer[0]=='0': answer = '0' #예외처리(젤 큰게 0이라면 그냥 0임)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (63.59ms, 61.6MB)
테스트 2 〉	통과 (32.78ms, 36.5MB)
테스트 3 〉	통과 (77.18ms, 78.6MB)
테스트 4 〉	통과 (1.59ms, 11MB)
테스트 5 〉	통과 (55.34ms, 55.2MB)
테스트 6 〉	통과 (48.88ms, 49.2MB)
테스트 7 〉	통과 (0.06ms, 10.6MB)
테스트 8 〉	통과 (0.07ms, 10.7MB)
테스트 9 〉	통과 (0.06ms, 10.6MB)
테스트 10 〉	통과 (0.06ms, 10.7MB)
테스트 11 〉	통과 (0.07ms, 10.6MB)
'''