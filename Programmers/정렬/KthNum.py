def solution(array, commands):
    '''answer = []
    for i in range(len(commands)):
        tmp = commands[i]
        s = sorted(array[tmp[0]-1:tmp[1]])
        answer.append(s[tmp[2]-1])
    return answer
        '''
    #가장 짧은 풀이
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
