#시간 초과 코드
#다음 시도: 같은 단어 조각이 연속으로 나온다면 굳이 재귀 돌지 않고 한 번에 처리하도록
import sys

sys.setrecursionlimit(10 ** 8)
INF = 987654321

# data: 현재 알파벳, children: 그 다음에 오는 알파벳(key=알파벳, value=노드)
# end: 현재까지가 하나의 단어 조각인지 (True or False)
class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.end = False


#t: 만들어야 하는 문장
class Trie:
    def __init__(self, t):
        self.node = Node(None)
        self.ans = INF
        self.t = t
        self.len = len(t)

    def insert(self, target):
        cur_node = self.node
        i = 0
        while cur_node.children and i < len(target):
            if target[i] in cur_node.children:
                cur_node = cur_node.children[target[i]]
                i += 1
            else:
                break

        # cur_node에 추가할게 남았으면
        for j in range(i, len(target)):
            cur_node.children[target[j]] = Node(target[j])
            cur_node = cur_node.children[target[j]]

        cur_node.end = True

    def search(self, idx, cnt):
        if cnt >= self.ans:
            return
        cur_node = self.node
        i = idx
        while cur_node.children and i < self.len:
            if self.t[i] in cur_node.children:
                cur_node = cur_node.children[self.t[i]]
                i += 1
                if cur_node.end:
                    self.search(i, cnt + 1)
            else:
                break

        if i == self.len and cur_node.end:
            self.ans = min(self.ans, cnt)


def solution(strs, t):
    trie = Trie(t)
    for s in strs:
        trie.insert(s)

    trie.search(0, 1)
    return -1 if trie.ans == INF else trie.ans