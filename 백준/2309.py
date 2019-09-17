#브루트포스
import itertools

n = []
total = 0
for _ in range(9):
    tmp = int(input())
    total += tmp
    n.append(tmp)

#sol1) 9개 다 더한 값(total)에서 임의의 두 값의 합을 빼서 100이 되는 값 구하기

def sol1(n):
    # combination 구하기
    t = list(itertools.combinations(n, 2))
    for i in t:
        tmp = total - (i[0]+i[1])
        if tmp == 100:
            n.remove(i[0])
            n.remove(i[1])
            break
    n.sort()

#sol2) 9개 중 7개 택해서 100되는 값 찾기
def sol2(n):
    t = list(itertools.combinations(n, 7))
    for i in t:
        tmp = 0
        for j in i:
            tmp += j
        if tmp == 100:
            tt = list(i)
            tt.sort()
            return tt


for i in sol2(n):
     print(i)