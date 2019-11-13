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