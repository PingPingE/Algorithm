'''
문제 설명)
단어 퍼즐은 주어진 단어 조각들을 이용해서 주어진 문장을 완성하는 퍼즐입니다.
이때, 주어진 각 단어 조각들은 각각 무한개씩 있다고 가정합니다.
예를 들어 주어진 단어 조각이 [“ba”, “na”, “n”, “a”]인 경우 "ba", "na", "n", "a" 단어 조각이 각각 무한개씩 있습니다.
이때, 만들어야 하는 문장이 “banana”라면 “ba”, “na”, “n”, “a”의 4개를 사용하여 문장을 완성할 수 있지만,
“ba”, “na”, “na”의 3개만을 사용해도 “banana”를 완성할 수 있습니다.
사용 가능한 단어 조각들을 담고 있는 배열 strs와 완성해야 하는 문자열 t가 매개변수로 주어질 때,
주어진 문장을 완성하기 위해 사용해야 하는 단어조각 개수의 최솟값을 return 하도록 solution 함수를 완성해 주세요.
만약 주어진 문장을 완성하는 것이 불가능하면 -1을 return 하세요.

제한사항)
strs는 사용 가능한 단어 조각들이 들어있는 배열로, 길이는 1 이상 100 이하입니다.
strs의 각 원소는 사용 가능한 단어조각들이 중복 없이 들어있습니다.
사용 가능한 단어 조각들은 문자열 형태이며, 모든 단어 조각의 길이는 1 이상 5 이하입니다.
t는 완성해야 하는 문자열이며 길이는 1 이상 20,000 이하입니다.
모든 문자열은 알파벳 소문자로만 이루어져 있습니다.
'''

#삽질 끝에 간단한(?) DP로 해결
def solution(strs, t):
    #가장 긴 단어 조각의 길이 추출(사실 짧아서 그냥 5로 해도 큰 차이 없을 듯)
    max_len=len(sorted(strs,key=lambda x: len(x), reverse=True)[0])

    #in 메서드의 시간 복잡도가 list는 O(N), set는 O(1)이라서 바꿔 줬는데 N이 최대 100이고, 원소도 길어봤자 5라서 차이가 없는 것 같다.
    strs= set(strs)
    INF=987654321
    ans = [INF for _ in range(len(t)+1)]
    for i in range(1,len(t)+1):
        if t[:i] in strs:
            ans[i]= 1
        else:
            for j in range(i-1,0,-1):
                #이 제한을 걸어주지 않으면 효율성에서 시간초과남
                if i-j > max_len:
                    break
                if t[j:i] in strs:
                    ans[i] = min(ans[j]+1, ans[i])

    return ans[-1] if ans[-1] != INF else -1
'''
#strs를 set로 변경했을 때
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.08ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.1MB)
테스트 5 〉	통과 (0.12ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.23ms, 10.3MB)
테스트 8 〉	통과 (2.67ms, 10MB)
테스트 9 〉	통과 (1.65ms, 10.1MB)
테스트 10 〉	통과 (1.55ms, 10.3MB)
테스트 11 〉	통과 (2.18ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (128.34ms, 10.8MB)
테스트 2 〉	통과 (130.01ms, 10.9MB)
테스트 3 〉	통과 (122.70ms, 10.9MB)
테스트 4 〉	통과 (130.30ms, 10.8MB)
테스트 5 〉	통과 (127.85ms, 10.7MB)
'''

'''
#strs를 list로 했을 때(그대로)
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (0.11ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.28ms, 10.2MB)
테스트 8 〉	통과 (2.31ms, 10.3MB)
테스트 9 〉	통과 (3.51ms, 10.1MB)
테스트 10 〉	통과 (5.01ms, 10.1MB)
테스트 11 〉	통과 (3.85ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.03ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 10.1MB)
테스트 19 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (127.60ms, 10.9MB)
테스트 2 〉	통과 (132.02ms, 10.8MB)
테스트 3 〉	통과 (123.98ms, 10.8MB)
테스트 4 〉	통과 (125.21ms, 10.8MB)
테스트 5 〉	통과 (120.39ms, 10.5MB)
'''


#=========삽질 기록
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