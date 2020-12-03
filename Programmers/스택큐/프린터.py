'''
문제 설명)
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 
중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.
현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

제한사항)
현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다
'''

from collections import deque
def solution(priorities, location):
    answer = 0
    loc = priorities[location]
    priorities[location] = -1 #타깃문서표시
    que =deque(priorities)
    while que:
        target = que.popleft()
        stat = False #타깃문서인지
        
        if target == -1:
            stat = True
            
        #현 que에서 loc까지 합쳐서 max구하기 -> max(max(que),loc) 이게 좀 더 효율이 좋을 것이다.
        if que and max(list(que)+[loc]) > (target if target > -1 else loc):
            que.append(target)
            continue
            
        else:
            answer += 1
            if stat:
                break
                
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.18ms, 10.2MB)
테스트 2 〉	통과 (1.40ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.19ms, 10.2MB)
테스트 7 〉	통과 (0.17ms, 10.2MB)
테스트 8 〉	통과 (1.06ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.22ms, 10.2MB)
테스트 11 〉	통과 (0.83ms, 10.2MB)
테스트 12 〉	통과 (0.05ms, 10.1MB)
테스트 13 〉	통과 (0.84ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.07ms, 10.3MB)
테스트 17 〉	통과 (1.28ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.93ms, 10.2MB)
테스트 20 〉	통과 (0.13ms, 10.2MB)
'''

#sol2: 다른 사람 코드 참고
from collections import deque
def solution(priorities, location):
    answer = 0
    #(우선순위, 인덱스)
    que = deque((pri, e) for e,pri in enumerate(priorities))
    while que:
        pri, e  = que.popleft()
        if any(pri < t[0] for t in que): #any는 하나라도 True면 return True -> all도 있음
            que.append((pri,e))
        else:
            answer +=1
            if e==location:
                break
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.41ms, 10.2MB)
테스트 2 〉	통과 (1.07ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.16ms, 10.1MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.82ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.17ms, 10.2MB)
테스트 11 〉	통과 (0.55ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.2MB)
테스트 13 〉	통과 (0.50ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
테스트 16 〉	통과 (0.06ms, 10.2MB)
테스트 17 〉	통과 (0.80ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.2MB)
테스트 19 〉	통과 (0.60ms, 10.2MB)
테스트 20 〉	통과 (0.10ms, 10.2MB)
'''