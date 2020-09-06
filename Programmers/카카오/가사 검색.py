'''
문제 설명)
[본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

친구들로부터 천재 프로그래머로 불리는 프로도는 음악을 하는 친구로부터
자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.
그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다.
와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다.
예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

가사 단어 제한사항)
words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

검색 키워드 제한사항)
queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
검색 키워드는 중복될 수도 있습니다.
각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.
'''
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data  # 한 단어의 마지막인경우 전체 삽입
        self.count = 0  # 현재 알파벳까지 해당 되는 단어 수
        self.child = {}

class Trie:
    def __init__(self):
        self.node = Node(None)

    def insert(self, x):  # 문자열 삽입
        cur_node = self.node
        for target in x:
            if target not in cur_node.child:
                cur_node.child[target] = Node(key=target)
            cur_node.count += 1
            cur_node = cur_node.child[target]
        cur_node.count += 1
        cur_node.data = x  # 하나의 단어의 끝이므로 전체 저장

    def search(self, x):
        cur_node = self.node
        cnt = 0
        for xx in x:
            if xx == '?': break
            if xx not in cur_node.child: return 0
            cur_node = cur_node.child[xx]

        for c in cur_node.child:
            cnt += cur_node.child[c].count

        return cnt

from collections import defaultdict
def solution(words, queries):
    answer = []
    trie = defaultdict(lambda: Trie())
    trie_r = defaultdict(lambda: Trie())
    for w in words:
        trie[len(w)].insert(w)
        trie_r[len(w)].insert(w[::-1])
    for q in queries:
        if q[0] == '?':
            answer.append(trie_r[len(q)].search(q[::-1]))
        else:
            answer.append(trie[len(q)].search(q))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (1.83ms, 9.97MB)
테스트 2 〉	통과 (0.52ms, 9.73MB)
테스트 3 〉	통과 (1.01ms, 9.79MB)
테스트 4 〉	통과 (0.78ms, 9.71MB)
테스트 5 〉	통과 (0.56ms, 9.63MB)
테스트 6 〉	통과 (1.03ms, 9.67MB)
테스트 7 〉	통과 (9.62ms, 12MB)
테스트 8 〉	통과 (4.36ms, 10.4MB)
테스트 9 〉	통과 (8.66ms, 11.6MB)
테스트 10 〉	통과 (9.47ms, 11.9MB)
테스트 11 〉	통과 (4.27ms, 10.5MB)
테스트 12 〉	통과 (9.48ms, 11.9MB)
테스트 13 〉	통과 (50.91ms, 21MB)
테스트 14 〉	통과 (19.26ms, 14.2MB)
테스트 15 〉	통과 (48.87ms, 20.8MB)
테스트 16 〉	통과 (57.07ms, 21.8MB)
테스트 17 〉	통과 (18.58ms, 13.9MB)
테스트 18 〉	통과 (50.31ms, 20.6MB)
효율성  테스트
테스트 1 〉	통과 (1615.32ms, 191MB)
테스트 2 〉	통과 (3561.50ms, 360MB)
테스트 3 〉	통과 (3198.91ms, 336MB)
테스트 4 〉	통과 (3028.45ms, 418MB)
테스트 5 〉	통과 (6283.93ms, 786MB)
'''