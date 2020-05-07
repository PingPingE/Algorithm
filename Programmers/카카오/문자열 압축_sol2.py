import re
def solution(s):
    ans = len(s)
    cut_length = len(s)//2+1
    while cut_length>0:
        tmp_s = ""
        i = 0
        while i<len(s):
            com = re.search(f"({s[i:i+cut_length]})+", s[i:])
            leng = len(com.group())//len(s[i:i+cut_length])
            if leng>1:
                tmp_s += f"{leng}"
            tmp_s += f"{com.group()[:cut_length]}"
            i += cut_length*leng
        ans = min(ans, len(tmp_s))
        cut_length -=1
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (1.63ms, 10.8MB)
테스트 2 〉	통과 (44.50ms, 11MB)
테스트 3 〉	통과 (17.62ms, 10.9MB)
테스트 4 〉	통과 (1.44ms, 10.8MB)
테스트 5 〉	통과 (0.11ms, 10.7MB)
테스트 6 〉	통과 (2.17ms, 10.7MB)
테스트 7 〉	통과 (74.37ms, 11.1MB)
테스트 8 〉	통과 (58.96ms, 11.1MB)
테스트 9 〉	통과 (94.18ms, 11.1MB)
테스트 10 〉	통과 (697.99ms, 12MB)
테스트 11 〉	통과 (6.80ms, 10.7MB)
테스트 12 〉	통과 (13.63ms, 10.8MB)
테스트 13 〉	통과 (9.20ms, 10.8MB)
테스트 14 〉	통과 (88.25ms, 11MB)
테스트 15 〉	통과 (9.52ms, 10.8MB)
테스트 16 〉	통과 (0.72ms, 10.7MB)
테스트 17 〉	통과 (261.20ms, 11.2MB)
테스트 18 〉	통과 (221.66ms, 11.5MB)
테스트 19 〉	통과 (238.93ms, 11.2MB)
테스트 20 〉	통과 (1037.87ms, 12.2MB)
테스트 21 〉	통과 (849.34ms, 12.3MB)
테스트 22 〉	통과 (885.85ms, 12.3MB)
테스트 23 〉	통과 (768.40ms, 12.2MB)
테스트 24 〉	통과 (712.39ms, 12MB)
테스트 25 〉	통과 (889.83ms, 12.3MB)
테스트 26 〉	통과 (826.72ms, 12.3MB)
테스트 27 〉	통과 (801.94ms, 12.3MB)
테스트 28 〉	통과 (0.81ms, 10.8MB)
'''
'''
sol1과 다르게 정규식을 활용해서 풀어봤다.
코드양은 줄었으나, 효율성이 좋지 않은 것 같다.
'''