from collections import defaultdict
def solution(dirs):
    dir_dic = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}
    from_to_dic = defaultdict(set)
    cur = [0, 0]

    for d in dirs:
        prev = cur[:]
        cur[0] += dir_dic[d][0]
        cur[1] += dir_dic[d][1]

        if -5 <= cur[0] <= 5 and -5 <= cur[1] <= 5:
            from_to_dic[(prev[0], prev[1])].add((cur[0], cur[1]))
            from_to_dic[(cur[0], cur[1])].add((prev[0], prev[1]))
        else:
            cur = prev[:]
    return sum(len(v) for k, v in from_to_dic.items()) // 2

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.23ms, 10.3MB)
테스트 5 〉	통과 (0.16ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.3MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.3MB)
테스트 13 〉	통과 (0.10ms, 10.4MB)
테스트 14 〉	통과 (0.11ms, 10.3MB)
테스트 15 〉	통과 (0.11ms, 10.3MB)
테스트 16 〉	통과 (0.41ms, 10.3MB)
테스트 17 〉	통과 (0.46ms, 10.3MB)
테스트 18 〉	통과 (0.46ms, 10.3MB)
테스트 19 〉	통과 (0.41ms, 10.3MB)
테스트 20 〉	통과 (0.44ms, 10.3MB)
'''