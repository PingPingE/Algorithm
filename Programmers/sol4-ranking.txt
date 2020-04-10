def solution(n, results):
    d = [[-1 for _ in range(n)] for __ in range(n)]
    for i,j in results:
        d[i-1][j-1] = 1
        d[j-1][i-1] = 0
    res= 0
    for i in range(n):#거쳐가는 노드
        for j in range(n):#시작노드
            d[j][j] = -2 #자기자신은 -2로 표시
            if d[j][i] == -1:
                continue
            if d[j][i] == 0:#j가 i한테 짐
                for k in range(n): #도착노드
                    if d[i][k] ==0:
                        d[j][k] = 0
            else: #j가 i 이김
                for k in range(n): #도착노드
                    if d[i][k] == 1:
                        d[j][k] = 1  
    for i in range(n):
        if -1 not in d[i]:
            res += 1
    return res

정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.8MB)
테스트 2 〉	통과 (0.07ms, 10.8MB)
테스트 3 〉	통과 (0.13ms, 10.8MB)
테스트 4 〉	통과 (0.26ms, 10.8MB)
테스트 5 〉	통과 (1.97ms, 10.8MB)
테스트 6 〉	통과 (4.17ms, 10.9MB)
테스트 7 〉	통과 (21.06ms, 11.1MB)
테스트 8 〉	통과 (45.37ms, 13.7MB)
테스트 9 〉	통과 (63.51ms, 16.3MB)
테스트 10 〉	통과 (64.84ms, 17.5MB)