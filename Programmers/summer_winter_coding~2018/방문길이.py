'''
게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

U: 위쪽으로 한 칸 가기

D: 아래쪽으로 한 칸 가기

R: 오른쪽으로 한 칸 가기

L: 왼쪽으로 한 칸 가기

캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 
좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.

명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

제한사항)
dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
dirs의 길이는 500 이하의 자연수입니다.
'''

from collections import defaultdict
done = defaultdict(set) #key: 출발점, set: 도착점 집합
def find(dep, dest): #출발점, 도착점
    global done
    if dest in done and dep in done[dest]: #이미 지나온 길인지 확인
        return False
    return True
def solution(dirs):
    global done
    #상하좌우
    dy = [1,-1,0,0]
    dx = [0,0,-1,1]
    dir_d = {'U':0,'D':1,'L':2,'R':3}
    current = (0,0)
    for e,d in enumerate(dirs):
        x,y = current
        y += dy[dir_d[d]]
        x += dx[dir_d[d]]
        if y>5 or y<-5 or x>5 or x<-5:
            continue
        if find(current, (x,y)) is True: #지나오지 않은 길이면
            done[current].add((x,y))#set에 추가
        current = (x,y)
    ans = 0
    for k,v in done.items():
        ans += len(v)
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.8MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.13ms, 10.8MB)
테스트 5 〉	통과 (0.14ms, 10.8MB)
테스트 6 〉	통과 (0.09ms, 10.8MB)
테스트 7 〉	통과 (0.06ms, 10.8MB)
테스트 8 〉	통과 (0.08ms, 10.9MB)
테스트 9 〉	통과 (0.07ms, 10.8MB)
테스트 10 〉	통과 (0.07ms, 10.9MB)
테스트 11 〉	통과 (0.07ms, 10.8MB)
테스트 12 〉	통과 (0.12ms, 10.8MB)
테스트 13 〉	통과 (0.11ms, 10.7MB)
테스트 14 〉	통과 (0.11ms, 10.7MB)
테스트 15 〉	통과 (0.10ms, 10.8MB)
테스트 16 〉	통과 (0.34ms, 10.7MB)
테스트 17 〉	통과 (0.36ms, 10.7MB)
테스트 18 〉	통과 (0.37ms, 10.7MB)
테스트 19 〉	통과 (0.37ms, 10.8MB)
테스트 20 〉	통과 (0.37ms, 10.7MB)
'''