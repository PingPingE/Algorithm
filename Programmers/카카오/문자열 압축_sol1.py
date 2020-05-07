def solution(s):
    answer = 1001
    for i in range(1, (len(s)//2)+1):
        m = {}
        res = 0
        prev =''
        for j in range(0, len(s), i):
            if prev == s[j:j + i]:
                if m[s[j:j + i]][-1] == 1:
                    res += 1
                tmp = len(str(m[s[j:j + i]][-1]))
                m[s[j:j + i]][-1] += 1
                #자리수가 커지면
                if tmp < len(str(m[s[j:j + i]][-1])):
                    res += 1
            else:
                res += len(s[j:j + i])
                if s[j:j + i] in m:
                    m[s[j:j + i]].append(1)
                else:
                    m[s[j:j + i]] = [1]
            prev = s[j:j + i]
        answer = min(answer, res)
    if len(s) <=2:
        answer = len(s)
    return answer

print(solution("abcabcabcabcdededededede"))
'''
정확성  테스트
테스트 1 〉	통과 (0.09ms, 10.6MB)
테스트 2 〉	통과 (1.06ms, 10.8MB)
테스트 3 〉	통과 (0.53ms, 10.8MB)
테스트 4 〉	통과 (0.10ms, 10.8MB)
테스트 5 〉	통과 (0.04ms, 10.6MB)
테스트 6 〉	통과 (0.14ms, 10.7MB)
테스트 7 〉	통과 (1.05ms, 10.7MB)
테스트 8 〉	통과 (1.11ms, 10.6MB)
테스트 9 〉	통과 (1.45ms, 10.7MB)
테스트 10 〉	통과 (5.46ms, 10.7MB)
테스트 11 〉	통과 (0.24ms, 10.8MB)
테스트 12 〉	통과 (0.23ms, 10.8MB)
테스트 13 〉	통과 (0.28ms, 10.5MB)
테스트 14 〉	통과 (1.44ms, 10.8MB)
테스트 15 〉	통과 (0.28ms, 10.7MB)
테스트 16 〉	통과 (0.06ms, 10.7MB)
테스트 17 〉	통과 (2.50ms, 10.8MB)
테스트 18 〉	통과 (2.41ms, 10.7MB)
테스트 19 〉	통과 (2.44ms, 10.8MB)
테스트 20 〉	통과 (5.78ms, 10.8MB)
테스트 21 〉	통과 (5.78ms, 10.7MB)
테스트 22 〉	통과 (5.73ms, 10.7MB)
테스트 23 〉	통과 (5.45ms, 10.8MB)
테스트 24 〉	통과 (6.56ms, 10.7MB)
테스트 25 〉	통과 (5.65ms, 10.8MB)
테스트 26 〉	통과 (5.71ms, 10.6MB)
테스트 27 〉	통과 (5.90ms, 10.7MB)
테스트 28 〉	통과 (0.06ms, 10.8MB)

'''
