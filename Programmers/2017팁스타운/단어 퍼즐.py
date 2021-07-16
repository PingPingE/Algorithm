#시도중
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
        self.t = t
        self.len = len(t)
        self.ans = [INF for _ in range(self.len)]

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

    def search(self, s_idx, idx, cnt):  # 시작 인덱스, 현재 인덱스, 현재까지의 단어조각 개수
        cur_node = self.node
        i = idx
        while cur_node.children and i < self.len:
            if self.t[i] in cur_node.children:
                cur_node = cur_node.children[self.t[i]]
                i += 1
                if cur_node.end:
                    if self.ans[i - 1] >= cnt + 1:
                        self.ans[i - 1] = cnt + 1
                        flag = True
                        d_cnt = 0
                        k = i
                        while flag:
                            for j in range(idx - s_idx + 1):
                                if k + j >= self.len or self.t[k + j] != self.t[s_idx + j]:
                                    flag = False
                                    break
                            else:  # 바로 뒤에 또 같은 단어가 있으면
                                d_cnt += 1
                                k += idx - s_idx + 1

                        if d_cnt > 0 and self.ans[k - 1] > cnt + d_cnt + 1:
                            self.search(k, k, cnt + d_cnt + 1)
                        self.search(i, i, cnt + 1)
                    else:
                        return
            else:
                return

        if i == self.len and cur_node.end:
            return


def solution(strs, t):
    trie = Trie(t)
    for s in strs:
        trie.insert(s)
    trie.search(0, 0, 0)
    return -1 if trie.ans[-1] == INF else trie.ans[-1]