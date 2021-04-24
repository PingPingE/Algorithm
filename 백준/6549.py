'''
문제
히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다.
예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.

히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

입력
입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다.
(1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다.
이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다.
모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

출력
각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
'''
#==========시간 초과===========
import sys
from collections import deque
while True:
    tmp=list(map(int, sys.stdin.readline().strip().split()))
    # print(tmp)
    if tmp[0] ==0: break
    n,h=tmp[0], tmp[1:]
    # print("n:",n ,"len_h:",len(h))
    maxx=0
    #====복사 과정을 생략하기 위해 두 개의 덱큐를 선언
    que=[deque(),deque()]
    flag=0 #=== 하나의 큐는 현재 대상(que[flag]) / 나머지 하나는 갱신 값을 넣을 큐 (que[not flag])
    
    for cur_i,cur_h in enumerate(h):
        if not que[flag]:
            que[flag].append((cur_i, cur_h))
            continue

        while que[flag]:
            top_i, top_h= que[flag].pop()
            if cur_h >= top_h: #===top의 height가 더 작거나 같으면 그대로
                que[not flag].appendleft((top_i,top_h)) #===top_h 그대로

                while que[flag]:
                    top_i, top_h = que[flag].pop()
                    que[not flag].appendleft((top_i, top_h))
                break

            else: #===top의 height가 더 높으면 height를 갱신해야할 때
                # print("top_i, cur_i:",top_i, cur_i, "top_h, cur_h:",top_h, cur_h)
                maxx = max(maxx, (cur_i-top_i)*top_h)#===maxx값 갱신하고
                que[not flag].appendleft((top_i, cur_h))#===cur_h로 갱신

        que[not flag].append((cur_i,cur_h))
        flag=not flag#===flag 갱신
        
    # print(que[flag])
    while que[flag]:
        top_i,top_h=que[flag].pop()
        maxx = max(maxx, (n-top_i)*top_h)
    print(maxx)