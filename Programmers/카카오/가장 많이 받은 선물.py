def solution(friends, gifts):
    answer = 0
    N = len(friends)
    index_mapping = {friend:e for e,friend in enumerate(friends)}
    count = [[0]*N for _ in range(N)]
    for gift in gifts:
        give, get = gift.split()
        give_id, get_id =index_mapping[give], index_mapping[get]
        count[give_id][get_id] += 1
        count[get_id][give_id] -= 1
    for i in range(N):
        tmp_ans = 0
        for j in range(N):
            if count[i][j] > count[j][i]:
                tmp_ans +=1
            elif count[i][j] == count[j][i]:
                i_sum = sum(count[i])
                j_sum = sum(count[j])
                if i_sum > j_sum:
                    tmp_ans += 1
        answer = max(answer, tmp_ans)
    return answer