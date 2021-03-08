'''
문제)
상근이는 1층 빌딩에 침입해 매우 중요한 문서를 훔쳐오려고 한다. 상근이가 가지고 있는 평면도에는 문서의 위치가 모두 나타나 있다. 빌딩의 문은 모두 잠겨있기 때문에, 문을 열려면 열쇠가 필요하다. 
상근이는 일부 열쇠를 이미 가지고 있고, 일부 열쇠는 빌딩의 바닥에 놓여져 있다.

상근이가 훔칠 수 있는 문서의 최대 개수를 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 수는 100개를 넘지 않는다.

각 테스트 케이스의 첫째 줄에는 지도의 높이와 너비 h와 w (2 ≤ h, w ≤ 100)가 주어진다. 다음 h개 줄에는 빌딩을 나타내는 w개의 문자가 주어지며, 각 문자는 다음 중 하나이다.

'.'는 빈 공간을 나타낸다.
'*'는 벽을 나타내며, 상근이는 벽을 통과할 수 없다.
'$'는 상근이가 훔쳐야하는 문서이다.
알파벳 대문자는 문을 나타낸다.
알파벳 소문자는 열쇠를 나타내며, 그 문자의 대문자인 모든 문을 열 수 있다.
마지막 줄에는 상근이가 이미 가지고 있는 열쇠가 공백없이 주어진다. 만약, 열쇠를 하나도 가지고 있지 않는 경우에는 "0"이 주어진다.

상근이는 처음에는 빌딩의 밖에 있으며, 빌딩 가장자리의 빈 공간이나 문을 통해 빌딩 안팎을 드나들 수 있다. 각각의 문에 대해서,
그 문을 열 수 있는 열쇠의 개수는 0개, 1개, 또는 그 이상이고, 각각의 열쇠에 대해서, 그 열쇠로 열 수 있는 문의 개수도 0개, 1개, 또는 그 이상이다. 열쇠는 여러 번 사용할 수 있다.

출력)
각 테스트 케이스 마다, 상근이가 훔칠 수 있는 문서의 최대 개수를 출력한다.
'''
#130848kb	300ms
from collections import deque,defaultdict
import sys
T=int(input())
def get_alphabet(ny,nx):
    tmp = ord(board[ny][nx])
    if 97 <= tmp:  # 소문자: 열쇠
        key_set.add(board[ny][nx]) #상근이가 가진 key 집합에 추가

        while failed[board[ny][nx].upper()]:#이 열쇠로 열 수 있는 문이 실패 기록에 있는 경우
            yx=failed[board[ny][nx].upper()].pop()
            board[yx[0]][yx[1]] = '.'  # 해당 자리 빈칸으로 만들고
            que.append(yx)  # 그 자리 큐에 넣기
            done.add(yx)

        board[ny][nx] = '.' #빈칸으로 만들기
        done.add((ny, nx))
        que.append((ny,nx))

    else: # 대문자: 문
        if board[ny][nx].lower() in key_set:  # 상근이의 key 집합에 있는 경우
            board[ny][nx] = '.' #빈칸으로 만들기
            que.append((ny, nx))
            done.add((ny, nx))

        else: # 없으면 일단 실패 기록
            failed[board[ny][nx]].append((ny, nx))

def get_doc(ny,nx): #문서 줍기
    global doc_cnt
    board[ny][nx] = '.' #문서 자리 빈칸으로 만들기
    doc_cnt += 1 #문서 count++
    done.add((ny, nx))
    que.append((ny, nx))

def get_start_point(y,x,axis): #0: 수평, 1: 수직
    global h,w
    if axis: #수직(x고정)
        for r in range(h):
            ny,nx=r,x
            if board[ny][nx]=='*': continue #벽
            elif board[ny][nx] == '.': #빈칸
                que.append((ny, nx))
                done.add((ny, nx))
            elif board[ny][nx] == '$': #문서
                get_doc(ny, nx)
            else: #열쇠 or 문
                get_alphabet(ny, nx)

    else:#수평(y고정)
        for c in range(w):
            ny,nx=y,c
            if board[ny][nx] == '*': continue
            elif board[ny][nx] == '.':
                que.append((ny, nx))
                done.add((ny, nx))
            elif board[ny][nx] == '$':
                get_doc(ny, nx)
            else:
                get_alphabet(ny, nx)


while T:
    T-=1
    doc_cnt = 0
    que=deque()
    h,w=map(int, input().split())
    board=[list(sys.stdin.readline().strip()) for _ in range(h)]
    key_set = set(s for s in input())
    done = set()
    failed = defaultdict(list)#======열쇠로 열 수 있는 문이 여러 개일 수 있으므로 list로 선언해야 한다(처음에 틀렸던 이유)

    #가장 자리에서 start point 찾기
    get_start_point(0,0,0) #맨 윗행
    get_start_point(h-1,0,0) #맨 아랫행
    get_start_point(0,0,1)#맨 왼쪽열
    get_start_point(0,w-1,1) #맨 오른쪽열

    dy,dx=[-1,1,0,0],[0,0,-1,1]
    while que:
        # print("doc_cnt:",doc_cnt, "key_set:",key_set,"failed: ",failed)
        y,x=que.popleft()
        for d in range(4):
            ny,nx=y+dy[d], x+dx[d]
            if ny<0 or nx<0 or ny>=h or nx>=w or board[ny][nx]=='*' or (ny,nx) in done:
                continue
            if board[ny][nx] == '$':#문서가 있는 경우
                get_doc(ny,nx)
            elif board[ny][nx]=='.':
                done.add((ny, nx))
                que.append((ny, nx))
            else:
                get_alphabet(ny,nx)
    print(doc_cnt)
    # print("Test Case:",T+1,"doc_cnt:",doc_cnt)