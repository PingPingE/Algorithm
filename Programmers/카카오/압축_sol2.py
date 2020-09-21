import string
def solution(msg):
    alph = {i:e for e,i in enumerate(string.ascii_uppercase,1)}
    ind = 27
    s = 0
    res = []
    while s<len(msg):
        e=2
        target_ind = alph[msg[s]]
        while s+e<=len(msg):
            target=msg[s:s+e]
            if target in alph:
                target_ind = alph[target]
                e+=1
            else:
                alph[target] = ind
                ind +=1
                break
        res.append(target_ind)
        s += e-1
    return res

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.21ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.32ms, 10.3MB)
테스트 7 〉	통과 (0.33ms, 10.4MB)
테스트 8 〉	통과 (0.34ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.31ms, 10.4MB)
테스트 11 〉	통과 (0.19ms, 10.3MB)
테스트 12 〉	통과 (0.35ms, 10.3MB)
테스트 13 〉	통과 (0.45ms, 10.4MB)
테스트 14 〉	통과 (0.41ms, 10.4MB)
테스트 15 〉	통과 (0.43ms, 10.3MB)
테스트 16 〉	통과 (0.33ms, 10.4MB)
테스트 17 〉	통과 (0.33ms, 10.3MB)
테스트 18 〉	통과 (0.12ms, 10.3MB)
테스트 19 〉	통과 (0.14ms, 10.3MB)
테스트 20 〉	통과 (0.30ms, 10.3MB)
'''