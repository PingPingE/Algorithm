'''
길 찾기 게임
전무로 승진한 라이언은 기분이 너무 좋아 프렌즈를 이끌고 특별 휴가를 가기로 했다.
내친김에 여행 계획까지 구상하던 라이언은 재미있는 게임을 생각해냈고 역시 전무로 승진할만한 인재라고 스스로에게 감탄했다.

라이언이 구상한(그리고 아마도 라이언만 즐거울만한) 게임은, 카카오 프렌즈를 두 팀으로 나누고, 각 팀이 같은 곳을 다른 순서로 방문하도록 해서 먼저 순회를 마친 팀이 승리하는 것이다.

그냥 지도를 주고 게임을 시작하면 재미가 덜해지므로, 라이언은 방문할 곳의 2차원 좌표 값을 구하고 각 장소를 이진트리의 노드가 되도록 구성한 후, 순회 방법을 힌트로 주어 각 팀이 스스로 경로를 찾도록 할 계획이다.

라이언은 아래와 같은 특별한 규칙으로 트리 노드들을 구성한다.

트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
모든 노드는 서로 다른 x값을 가진다.
같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
자식 노드의 y 값은 항상 부모 노드보다 작다.
임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.

곤경에 빠진 카카오 프렌즈를 위해 이진트리를 구성하는 노드들의 좌표가 담긴 배열 nodeinfo가 매개변수로 주어질 때,
노드들로 구성된 이진트리를 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return 하도록 solution 함수를 완성하자.

제한사항)
nodeinfo는 이진트리를 구성하는 각 노드의 좌표가 1번 노드부터 순서대로 들어있는 2차원 배열이다.
nodeinfo의 길이는 1 이상 10,000 이하이다.
nodeinfo[i] 는 i + 1번 노드의 좌표이며, [x축 좌표, y축 좌표] 순으로 들어있다.
모든 노드의 좌표 값은 0 이상 100,000 이하인 정수이다.
트리의 깊이가 1,000 이하인 경우만 입력으로 주어진다.
모든 노드의 좌표는 문제에 주어진 규칙을 따르며, 잘못된 노드 위치가 주어지는 경우는 없다.
'''
import sys
sys.setrecursionlimit(10**8)
class Node:
    def __init__(self, num, y, x):
        self.num = num
        self.y = y
        self.x = x
        self.left = None
        self.right = None

def solution(nodeinfo):
    answer = [[]]
    for e in range(1, len(nodeinfo) + 1): #번호 달기
        nodeinfo[e - 1].append(e)
    nodeinfo.sort(key=lambda x: [-x[1], x[0]]) #상위레벨, 왼쪽순서대로 정렬
    tree = Node(0, 0, 0)
    for node in nodeinfo:
        x, y, num = node
        if tree.num == 0:  # root
            tree.num = num
            tree.y = y
            tree.x = x
        else:
            current = tree
            while current:
                if current.y > y:
                    if current.x > x:
                        if current.left:
                            current = current.left
                        else:
                            current.left = Node(num,y,x)
                            break
                    else:
                        if current.right:
                            current = current.right
                        else:
                            current.right = Node(num,y,x)
                            break

    def preorder(done, current):#부모>왼>오
        done.append(current.num)
        if current.left:
            preorder(done, current.left)
        if current.right:
            preorder(done, current.right)
        return done

    def postorder(done, current):#왼>오>부모
        if current.left:
            postorder(done,current.left)
        if current.right:
            postorder(done, current.right)
        done.append(current.num)
        return done
    answer = []
    answer.append(preorder([], tree))
    answer.append(postorder([], tree))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (63.05ms, 11.4MB)
테스트 7 〉	통과 (58.16ms, 11.5MB)
테스트 8 〉	통과 (44.41ms, 12.1MB)
테스트 9 〉	통과 (219.48ms, 15.2MB)
테스트 10 〉	통과 (14.65ms, 11MB)
테스트 11 〉	통과 (178.48ms, 15MB)
테스트 12 〉	통과 (212.63ms, 14.9MB)
테스트 13 〉	통과 (0.71ms, 10.3MB)
테스트 14 〉	통과 (3.81ms, 10.5MB)
테스트 15 〉	통과 (17.39ms, 12.6MB)
테스트 16 〉	통과 (37.78ms, 15.1MB)
테스트 17 〉	통과 (3.82ms, 10.6MB)
테스트 18 〉	통과 (44.25ms, 15MB)
테스트 19 〉	통과 (7.06ms, 11.1MB)
테스트 20 〉	통과 (16.76ms, 12.1MB)
테스트 21 〉	통과 (23.72ms, 13MB)
테스트 22 〉	통과 (40.78ms, 14.9MB)
테스트 23 〉	통과 (42.97ms, 15MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.2MB)
테스트 26 〉	통과 (94.04ms, 11.8MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.06ms, 10.3MB)
테스트 29 〉	통과 (0.01ms, 10.2MB)
'''