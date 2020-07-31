def solution(s):
    answer = len(s)
    for n in range(1, len(s)):
        cnt = 1
        cur= len(s)
        prev=''
        for cut in range(n,len(s)+1,n):
            if s[cut-n:cut] == prev:
                cnt += 1
            else:
                if cnt >1:
                    cur -= len(prev)*(cnt-1)-len(str(cnt)) 
                prev = s[cut-n:cut]
                cnt =1#초기화
        if cnt > 1:
            cur -= len(prev)*(cnt-1)-len(str(cnt)) 
        #print("n: ",n, " cnt: ",cnt, " prev: ",prev," answer: ",answer)
        answer = min(answer, cur)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.8MB)
테스트 2 〉	통과 (0.37ms, 10.9MB)
테스트 3 〉	통과 (0.21ms, 10.7MB)
테스트 4 〉	통과 (0.06ms, 10.8MB)
테스트 5 〉	통과 (0.04ms, 10.9MB)
테스트 6 〉	통과 (0.08ms, 10.8MB)
테스트 7 〉	통과 (0.40ms, 10.8MB)
테스트 8 〉	통과 (0.40ms, 10.9MB)
테스트 9 〉	통과 (0.58ms, 10.7MB)
테스트 10 〉	통과 (2.12ms, 10.8MB)
테스트 11 〉	통과 (0.12ms, 10.7MB)
테스트 12 〉	통과 (0.12ms, 10.8MB)
테스트 13 〉	통과 (0.14ms, 10.6MB)
테스트 14 〉	통과 (0.59ms, 10.7MB)
테스트 15 〉	통과 (0.13ms, 10.7MB)
테스트 16 〉	통과 (0.05ms, 10.6MB)
테스트 17 〉	통과 (0.99ms, 10.7MB)
테스트 18 〉	통과 (0.92ms, 10.8MB)
테스트 19 〉	통과 (1.01ms, 10.6MB)
테스트 20 〉	통과 (2.11ms, 10.9MB)
테스트 21 〉	통과 (2.11ms, 10.8MB)
테스트 22 〉	통과 (2.24ms, 10.8MB)
테스트 23 〉	통과 (2.22ms, 10.8MB)
테스트 24 〉	통과 (1.93ms, 10.9MB)
테스트 25 〉	통과 (2.11ms, 10.7MB)
테스트 26 〉	통과 (2.27ms, 10.7MB)
테스트 27 〉	통과 (2.12ms, 10.8MB)
테스트 28 〉	통과 (0.05ms, 10.7MB)
'''