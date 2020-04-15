def solution(n, arr1, arr2):
    answer = []
    d = {'1':'#', '0':' '}
    for a1 in arr1:
        answer.append(format(a1, 'b').zfill(n))
    for e, a2 in enumerate(arr2):
        tmp = format(a2,'b').zfill(n)
        for i,t in enumerate(tmp):
            if t == '1':
                answer[e] = answer[e][:i] + '1'+answer[e][i+1:]
        tmp = ''
        for a in answer[e]:
            tmp += d[a]
        answer[e] = tmp

    return answer