def solution(numbers, hand):
    hand = 'L' if hand == 'left' else 'R'
    answer= hand
    cur = {'L':'*', 'R':'#'}
    cur[hand] = numbers[0]
    dic = {{1: (0, 1), 2: (0, 2), 3: (0, 3), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 0:(3,1), '*':(3,0), '#':(3,2)}

    for num in numbers[1:]:
        if num in (1,4,7):
           answer+='L'
           cur['L']=num
        elif num in (3,6,9):
           answer+='R'
           cur['R']=num
        else:
           dist_L = dic[cur['L']]
           dist_R = dic[cur['R']]
    return answer
