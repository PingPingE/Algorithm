'''
문제 설명)
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 
그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.

잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

제한사항)
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.
'''

def rotation(key):#열쇠 회전
    M =len(key)
    new_k = list([0 for _ in range(M)] for __ in range(M))
    for i in range(M):
        for j in range(M):
            new_k[j][M-1-i] = key[i][j]
    return new_k

def check(key, lock): #자물쇠 열 수 있는지 체크
    N,M = len(lock), len(key)
    for _ in range(4):
        key = rotation(key)
        for i in range(-M, N+M):
            for j in range(-M,N+M):
                cnt = 0
                stat = False
                for m in range(M):
                    for n in range(M):
                        if i+m >= N or j+n >=N or i+m<0 or j+n<0:
                            continue
                        if lock[i+m][j+n] == 1 and key[m][n]== 1: 
                            stat = True
                            break
                        if lock[i+m][j+n] == 0 and key[m][n] == 1:
                            cnt += 1
                    if stat:
                        break
                if cnt ==total_0 and stat^1:
                    return True
    return False

from collections import Counter
def solution(key, lock):
    global total_0
    total_0 = 0
    M,N = len(key), len(lock)
    for l in lock: #자물쇠의 홈부분 카운트
        total_0 += Counter(l)[0]
    return check(key, lock)

'''
정확성  테스트
테스트 1 〉	통과 (1.42ms, 9.59MB)
테스트 2 〉	통과 (0.07ms, 9.69MB)
테스트 3 〉	통과 (4.12ms, 9.75MB)
테스트 4 〉	통과 (0.09ms, 9.52MB)
테스트 5 〉	통과 (13.80ms, 9.48MB)
테스트 6 〉	통과 (6.37ms, 9.62MB)
테스트 7 〉	통과 (34.60ms, 9.69MB)
테스트 8 〉	통과 (18.25ms, 9.57MB)
테스트 9 〉	통과 (38.85ms, 9.56MB)
테스트 10 〉	통과 (88.39ms, 9.6MB)
테스트 11 〉	통과 (131.04ms, 9.77MB)
테스트 12 〉	통과 (0.06ms, 9.51MB)
테스트 13 〉	통과 (2.44ms, 9.61MB)
테스트 14 〉	통과 (0.72ms, 9.65MB)
테스트 15 〉	통과 (2.04ms, 9.48MB)
테스트 16 〉	통과 (17.57ms, 9.58MB)
테스트 17 〉	통과 (38.71ms, 9.53MB)
테스트 18 〉	통과 (3.68ms, 9.68MB)
테스트 19 〉	통과 (0.52ms, 9.68MB)
테스트 20 〉	통과 (24.39ms, 9.59MB)
테스트 21 〉	통과 (63.95ms, 9.49MB)
테스트 22 〉	통과 (17.04ms, 9.65MB)
테스트 23 〉	통과 (3.62ms, 9.54MB)
테스트 24 〉	통과 (3.53ms, 9.57MB)
테스트 25 〉	통과 (36.28ms, 9.61MB)
테스트 26 〉	통과 (133.94ms, 9.54MB)
테스트 27 〉	통과 (204.86ms, 9.52MB)
테스트 28 〉	통과 (17.12ms, 9.58MB)
테스트 29 〉	통과 (6.02ms, 9.6MB)
테스트 30 〉	통과 (24.41ms, 9.61MB)
테스트 31 〉	통과 (19.22ms, 9.59MB)
테스트 32 〉	통과 (76.50ms, 9.46MB)
테스트 33 〉	통과 (25.55ms, 9.58MB)
테스트 34 〉	통과 (2.63ms, 9.59MB)
테스트 35 〉	통과 (2.07ms, 9.54MB)
테스트 36 〉	통과 (3.41ms, 9.69MB)
테스트 37 〉	통과 (2.20ms, 9.54MB)
테스트 38 〉	통과 (0.45ms, 9.52MB)
'''