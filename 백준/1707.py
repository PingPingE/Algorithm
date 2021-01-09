import sys
K = int(input())
while K:
    K-=1
    V, E = map(int, input().split())
    color = {}
    ans = "YES"
    for _ in range(E):
        a,b = map(int, sys.stdin.readline().split())
        c = [0,0]
        stat= [False, False]
        if a in color:
            c[0] = color[a]
            stat[0] = True
        else:
            c[0] = 0
            color[a] = 0

        if b in color:
            c[1] = color[b]
            stat[1] = True
        else:
            c[1] = not c[0]
            color[b] = c[1]

        if c[0] == c[1]:
            if not stat[0] or not stat[1]: #둘 중 하나라도 방문된적 없으면
                if stat[0]:
                    color[b] = not c[1]
                else:
                    color[a] = not c[0]
                continue
            ans = "NO"
    print(ans)