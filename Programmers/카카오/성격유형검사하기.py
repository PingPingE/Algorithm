from collections import defaultdict
def solution(survey, choices):
    score = defaultdict(int)
    pairs = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    score_dict = {i: score for i, score in zip(range(1, 8), [3, 2, 1, 0, 1, 2, 3])}

    for target, choice in zip(survey, choices):
        if choice < 4:
            score[target[0]] += score_dict[choice]
        elif choice > 4:
            score[target[1]] += score_dict[choice]

    answer = ''
    for pair in pairs:
        p = sorted(pair,key=lambda x: (-score[x], x))[0]
        answer += p
    return answer

#test case: TCMA
#print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]	))