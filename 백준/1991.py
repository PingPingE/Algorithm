'''
문제)
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력)
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.

출력)
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''
#T1: 13분 20초
#T2: 45분 40초(32분 20초)
#T3: -
#sol1: 그냥 구현
#123560kb	144ms
from collections import deque
def get_preorder():
    stack = ['A']
    ans = []
    while stack:
        node = stack.pop()
        ans.append(node)
        left, right = nodes[node]
        if right == '.':
            if left != '.':
                stack.append(left)
        else:
            stack.append(right)
            if left != '.':
                stack.append(left)
    return ''.join(ans)

def get_inorder():
    que = deque(['A'])
    done =set()
    ans =[]
    while que:
        node = que.popleft()
        left, right= nodes[node]
        if left in done or left =='.':
            ans.append(node)
            done.add(node)
            if right != '.' and right not in done:
                que.appendleft(right)
        else:
            que.appendleft(node)
            if left != '.' and left not in done:
                que.appendleft(left)
    return ''.join(ans)

def get_postorder():
    que = deque(['A'])
    done = set()
    ans = []
    while que:
        node = que.popleft()
        left, right = nodes[node]
        if (left in done or left == '.') and (right in done or right=='.'):
            ans.append(node)
            done.add(node)
        else:
            que.appendleft(node)
            if right != '.' and right not in done:
                que.appendleft(right)
            if left != '.' and  left not in done:
                que.appendleft(left)
    return ''.join(ans)

N = int(input())
nodes = {}
for _ in range(N):
    a,b,c = input().split()
    nodes[a] = [b,c]
print(get_preorder())
print(get_inorder())
print(get_postorder())