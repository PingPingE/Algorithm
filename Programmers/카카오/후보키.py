from itertools import combinations
def Uniq(tmp, relation):
    global done
    d = set()
    #이미 있는지
    if tmp in done:
        if done[tmp] is False:
            return False
        return True
    # 유일성 체크
    for r in relation:
        s = ''
        for t in tmp:
            s += str(r[t])
        if s in d:
            done[tmp] = False
            return False
        d.add(s)
    done[tmp] = True
    return True


def check(tmp, relation):
    # 최소성 체크
    for i in range(1, len(tmp)):
        for c in list(combinations(list(tmp), i)):
            if Uniq(c, relation) is True:
                return False
    return True


def solution(relation):
    answer = 0
    #유일성check
    global done
    done =  {}
    if len(relation[0]) == 1:
        s = set()
        for r in relation:
            if ''.join(r) in s:
                return 0
            s.add(''.join(r))
        return 1

    for i in range(1, len(relation[0]) + 1):
        for c in list(combinations(list(range(len(relation[0]))), i)):
            if Uniq(c, relation) is True:
                done[c] = True
                if check(c, relation) is True:
                    answer += 1
            else:
                done[c] = False

    return answer
