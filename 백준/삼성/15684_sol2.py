from itertools import product
#메모리 초과 문제 원인: sys.setrecursionlimit
#125120kb	1680ms
def check():
    for col in range(N):
        row = 0
        cur = col
        while row<H:
            if ladder[row][cur] == 1:
                cur += 1
            elif cur-1>=0 and ladder[row][cur-1] == 1:
                cur -= 1
            row += 1
        if cur != col: return False
    return True

def solution(cnt, ind):
    global ret
    if cnt >= ret: return
    if check():
        ret = cnt
        return
    if cnt == 3: return
    for i in range(ind, len(candi)):
        r,c = candi[i]
        if ladder[r][c] == 1 or ladder[r][c+1] == 1 or (c-1>=0 and ladder[r][c-1]==1):
            continue
        ladder[r][c] = 1
        solution(cnt+1, i+1)
        ladder[r][c] = 0
    return

N, M, H = map(int, input().split())
ret = 4
ladder = list([0]*N for _ in range(H))
for _ in range(M):
  a,b = map(int,input().split())
  ladder[a-1][b-1] = 1
if check():
    ret = 0
else:
    candi = list()
    for comb in product(list(range(H)), list(range(N - 1))):
        r, c = comb
        if ladder[r][c] == 1 or ladder[r][c + 1] == 1 or (c - 1 >= 0 and ladder[r][c - 1] == 1):
            continue
        candi.append(comb)
    solution(0,0)
print(ret if ret<4 else -1)
