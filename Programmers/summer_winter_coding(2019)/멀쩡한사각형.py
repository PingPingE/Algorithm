#브레젠험 알고리즘: https://playground10.tistory.com/62
import math
def solution(w,h):
    if w==h: return w*h-w
    maxx, minn = max(w,h),min(w,h)
    if minn == 1: return 0
    n=0
    for x in range(1,minn+1):
        n+= math.ceil(maxx*x/minn) - math.floor(maxx*(x-1)/minn)
    return w*h -n


'''
정확성  테스트
테스트 1 〉	통과 (0.51ms, 10.2MB)
테스트 2 〉	통과 (4.62ms, 10.2MB)
테스트 3 〉	통과 (1.49ms, 10.2MB)
테스트 4 〉	통과 (0.52ms, 10.2MB)
테스트 5 〉	통과 (1.27ms, 10.2MB)
테스트 6 〉	통과 (8.25ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (3843.43ms, 10.2MB)
테스트 14 〉	통과 (0.00ms, 10.2MB)
테스트 15 〉	통과 (4860.85ms, 10.2MB)
테스트 16 〉	통과 (32.45ms, 10.2MB)
테스트 17 〉	통과 (2217.07ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.3MB)

'''