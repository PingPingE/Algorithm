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
'''
필요 자료구조)
1. 현재 보고 있는 히스토그램의 높이
    => list에 높이 넣고 for문으로 하나씩 보기
    
2. (높이,인덱스) 오름차순 정렬 + 해당 높이에 해당되는 히스토그램 몇 개 
    => stack에 해당 높이의 인덱스(위 list 기준)를 원소로 넣기 / 해당 높이에 해당되는 히스토그램 개수는 로직 3-3에서 설명
    => (높이, 인덱스)를 인덱스 하나로 대체
    
3. 현재까지의 가장 넓은 넓이
    => 그냥 스칼라타입 변수

로직)
1. for문에서 list의 원소를 하나씩 꺼낸다.(enumerate) => cur_index,cur_height 
2. stack에서 하나씩 pop (while not empty)
3. cur_height와 list[top_index] 비교
    3-1 cur_height = list[top_index] 경우
        => break
            => 높이 안낮추고 같은 영역에 포함 가능하므로
            
    3-2 cur_height > list[top_index] 경우
        => append
            => 새로운 시작
            
    3-3 cur_height < list[top_index] 경우
        => prev_index= 현재 top_index pop 하고 그다음 pop할 index (즉 순서를 보면, ... ~ prev_index ~ top_index ~ cur_index 이렇게 되어 있는거)
        => max값 갱신: max(maxx, (cur_index-prev_index-1)*list[top_index])
            => list[top_index]의 높이로 더 이상 영역 확장 불가
        
        => append
            => 새로운 시작
    => append가 겹치므로 그냥 공통으로 빼두는게 나을 듯(3-1의 경우도 append해도 노상관)
'''
#160248kb	216ms
import sys
while True:
    tmp=list(map(int, sys.stdin.readline().strip().split()))
    if tmp[0] ==0: break
    n,heights=tmp[0], [0]+tmp[1:]+[0]
    '''
    1 2 1 같은 경우 1*3이 가장 크다. 근데 인덱스 1의 2를 만나는 경우, 인덱스 0에서의 1인 경우가 stack에서 사라짐 따라서 앞에 [0] 추가
    1000 1000 1000 1000, 1 2 2 2 등의 케이스와 같이 끝까지 가고 나서 계산해야하는 경우를 위해 뒤에 [0]추가
    '''
    maxx= 0
    st=[]

    for cur_index, cur_height in enumerate(heights):
        # print("before:",st)
        while st and cur_height < heights[st[-1]]:
            top_index=st.pop()
            top_height=heights[top_index]
            # print("===top:", top_index, top_height,"===cur:", cur_index, cur_height)
            # print(cur_index-top_index, cur_index-st[-1]-1)
            maxx=max(maxx, (cur_index-st[-1]-1)*top_height) #=== 우리가 봐야하는 것은 prev_index(st[-1]) ~ cur_index이므로
        st.append(cur_index)
        # print("after",st,"maxx:",maxx)
    # print("remain:",st)
    print(maxx)


#https://hwiyong.tistory.com/379 코드
while True:
    n, *heights = list(map(int, input().split()))
    if (n == 0):
        break

    # 첫 시점의 계산을 위해 0을 맨 앞에 추가하고,
    heights.insert(0, 0)
    # 마지막 사각형 계산을 위해 0을 끝에 추가합니다.
    heights += [0]
    checked = [0]
    area = 0

    # 현재 높이보다 이전 높이가 높으면, while에 진입합니다.
    # 현재 높이가 더 낮은 경우, 넓이를 이어서 계산할 수 없으므로
    # 이전 시점까지 저장됬던 사각형의 높이를 계산합니다.
    # 끝 사각형도 고려해야 하므로, n+1까지 반복합니다.
    for i in range(1, n + 2):
        # heights[checked[-1]]은 이전 시점의 사각형 높이
        # heights[i]는 현재 시점의 사각형 높이
        # heights[checked[-1]] > heights[i]는 현재 높이보다 이전 높이가 높은지 확인
        while (checked and (heights[checked[-1]] > heights[i])):
            # 비교할 사각형 index
            cur_height = checked.pop()
            # (i - 1 - checked[-1])은 cur_height와 현재 시점 사이에 몇 개의 사각형이 존재하는지를 판단
            print(i-1-checked[-1])
            area = max(area, (i - 1 - checked[-1]) * heights[cur_height])
        checked.append(i)
    print(area)



#==========시간 초과===========
'''
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
'''