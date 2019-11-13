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
