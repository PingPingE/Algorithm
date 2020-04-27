def solution(board, moves):
    answer = 0
    bucket = list()
    for m in moves:
        m-=1
        for i in range(len(board)):
            if board[i][m] != 0:
                if len(bucket) > 0 and bucket[-1] == board[i][m]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[i][m])
                board[i][m] = 0
                break
    return answer