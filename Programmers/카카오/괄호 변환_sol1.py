def sol(w):
    # 빈문자열
    if len(w) == 0:
        return w
    count = {'(':0, ')':0}
    u = ''
    v= ''
    #u,v로 나누기
    for ww in range(len(w)):
        count[w[ww]] += 1
        if count['('] == count[')']:
            try:
                u=w[:ww+1]
                v=w[ww+1:]
                break
            except:
                break

    count = {'(': 0, ')': 0}
    stat = True
    for uu in range(len(u)):
        if u[0]==')' or count[')'] > count['(']:
            stat = False
            break
    #u가 올바른 괄호 문자열임
    if stat is True:
        return u+sol(v)
    #u가 올바른 괄호 문자열이 아님
    else:
        tmp = "("
        tmp += sol(v[:])
        tmp += ')'
        u = u[1:len(u)-1]
        for t in range(len(u)):
            if u[t] == '(':
                u=u[:t]+')'+u[t+1:]
            else:
                u=u[:t]+'('+u[t+1:]
        return tmp+u

def solution(p):
    return sol(p)

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.8MB)
테스트 3 〉	통과 (0.04ms, 10.8MB)
테스트 4 〉	통과 (0.05ms, 10.7MB)
테스트 5 〉	통과 (0.04ms, 10.8MB)
테스트 6 〉	통과 (0.04ms, 10.8MB)
테스트 7 〉	통과 (0.05ms, 10.7MB)
테스트 8 〉	통과 (0.05ms, 10.8MB)
테스트 9 〉	통과 (0.05ms, 10.8MB)
테스트 10 〉	통과 (0.05ms, 10.8MB)
테스트 11 〉	통과 (0.06ms, 10.8MB)
테스트 12 〉	통과 (0.08ms, 10.7MB)
테스트 13 〉	통과 (0.10ms, 10.9MB)
테스트 14 〉	통과 (0.12ms, 10.9MB)
테스트 15 〉	통과 (0.15ms, 10.9MB)
테스트 16 〉	통과 (0.29ms, 10.8MB)
테스트 17 〉	통과 (0.24ms, 10.9MB)
테스트 18 〉	통과 (0.33ms, 10.8MB)
테스트 19 〉	통과 (0.56ms, 10.8MB)
테스트 20 〉	통과 (0.40ms, 10.7MB)
테스트 21 〉	통과 (0.68ms, 10.8MB)
테스트 22 〉	통과 (0.26ms, 10.7MB)
테스트 23 〉	통과 (0.36ms, 10.8MB)
테스트 24 〉	통과 (0.15ms, 10.8MB)
테스트 25 〉	통과 (0.23ms, 10.7MB)
'''