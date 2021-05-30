'''
문제 설명
정수 n이 매개변수로 주어집니다.
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후,
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 1,000 이하입니다.

입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

'''

def solution(n):
    def down(r, c):
        nonlocal li, num
        for i in range(r, N):
            if li[i][c] > 0: break
            li[i][c] = num
            num += 1

        return N - 1, c

    def right(r, c):
        nonlocal li, num
        for j in range(c + 1, N - C):
            if li[r][j] > 0: break
            li[r][j] = num
            num += 1
        return r, N - 1

    def up(r, c):
        nonlocal li, num
        for i in range(r - 1, R, -1):
            if li[i][c] > 0: break
            li[i][c] = num
            num += 1

    li = [[0] * n for _ in range(n)]

    #R,C는 시작 위치, N은 범위, num은 채워넣을 숫자
    R, C, N, num = 0, 0, n, 1
    while (R < n and C < n) and not li[R][C]: #시작 위치 및 범위를 갱신하면서 아래->오른쪽->위 순서대로 채워넣기 
        r_, c_ = down(R, C)
        r_, c_ = right(r_, c_)
        up(r_, c_)
        
        #시작 위치 갱신
        R += 2
        C += 1

        #범위 좁히기
        N -= 1

    answer = []
    for i in li:
        for j in i:
            if j > 0:
                answer.append(j)
    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (1.60ms, 10.9MB)
테스트 5 〉	통과 (1.60ms, 10.8MB)
테스트 6 〉	통과 (1.56ms, 11MB)
테스트 7 〉	통과 (128.70ms, 63.2MB)
테스트 8 〉	통과 (155.26ms, 63.3MB)
테스트 9 〉	통과 (131.57ms, 63.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''