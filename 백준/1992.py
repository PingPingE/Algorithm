#쿼드트리
#29076kb	84ms
#문제 조건 잘 보자 -> 전체가 0이나 1로 꽉채워져있으면 괄호가 필요없다.
def quad(b, M):
    global ans
    pre_check = sum(sum(a) for a in b)
    if pre_check == M*M:
        ans.append("1")
        return
    elif pre_check == 0:
        ans.append("0")
        return
    ans.append("(")
    n = M // 2 * M // 2

    # 왼위
    target1 = list(b[i][:M // 2] for i in range(M // 2))
    tmp1 = sum(sum(a) for a in target1)
    if tmp1 in [0, n]:
        ans.append('0' if tmp1 == 0 else '1')
    else:
        quad([t[:] for t in target1], M // 2)

    # 오위
    target2 = list(b[i][M // 2:] for i in range(M // 2))
    tmp2 = sum(sum(a) for a in target2)
    if tmp2 in [0, n]:
        ans.append('0' if tmp2 == 0 else '1')
    else:
        quad([t[:] for t in target2], M // 2)

    # 왼아
    target3 = list(b[i][:M // 2] for i in range(M // 2, M))
    tmp3 = sum(sum(a) for a in target3)
    if tmp3 in [0, n]:
        ans.append('0' if tmp3 == 0 else '1')
    else:
        quad([t[:] for t in target3], M // 2)

    # 오아
    target4 = list(b[i][M // 2:] for i in range(M // 2, M))
    tmp4 = sum(sum(a) for a in target4)
    if tmp4 in [0, n]:
        ans.append('0' if tmp4 == 0 else '1')
    else:
        quad([t[:] for t in target4], M // 2)

    ans.append(")")

import sys
N = int(input())
board = list(list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N))
ans = []
quad(list(board[i][:] for i in range(N)), N)
print(''.join(ans))