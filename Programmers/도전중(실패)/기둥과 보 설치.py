def check(arr,n):
    for x in range(n+1):
        for y in range(n+1):
            if arr[x][y] == 1: #보
                if y == 0: return False
                if (x>0 and arr[x-1][y] == 1 and x<n and arr[x+1][y]==1) or arr[x][y-1] == 0 or (x<n and arr[x+1][y-1]== 0):
                    continue
                else:
                    return False
            elif arr[x][y] == 0: #기둥
                if y == 0 or ( x>0 and arr[x-1][y] == 1) or arr[x][y-1] == 0: continue
                else: return False
    return True

def solution(n, build_frame):
    answer = [[-1 for _ in range(n + 2)] for __ in range(n + 2)]
    for bf in build_frame:
        x, y, a, b = bf
        if b == 1:  # 설치
            answer[x][y]=a
            if check(answer, n)^1: answer[x][y]=-1
        else:  # 삭제
            tmp = answer[x][y]
            answer[x][y] = -1
            if check(answer, n)^1: answer[x][y] = tmp
    res = []
    for r in range(n + 1):
        for c in range(n + 1):
            if answer[r][c] == -1: continue
            res.append([r, c, answer[r][c]])
    res.sort()
    print(res)
    return res