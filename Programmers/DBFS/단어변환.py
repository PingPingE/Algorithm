'''
문제 설명)
두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면 
hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제한사항)
각 단어는 알파벳 소문자로만 이루어져 있습니다.
각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
begin과 target은 같지 않습니다.
변환할 수 없는 경우에는 0를 return 합니다.
'''

# T1(문제 이해 ~ 코딩 시작): 7분 33초
# T2(코딩 시작 ~ 제출): 33분 18초(25분 45초)
# T3(디버깅): 54분 3초(20분 45초)
def solution(begin, target, words):
    INF = 987654321
    count = INF
    if target not in words:
        return 0

    def dfs(current, done):
        nonlocal count, target
        if len(done) > count: return

        for word in words:
            if word in done: continue
            cnt = 0 #디버깅에 오래걸린 이유: 다른 개수를 세지않고, 다른 부분의 index를 저장했다.
            for e, w in enumerate(word):
                if w != current[e]:
                    cnt += 1
                    if cnt > 1: break
                    
            else:#그리고나서 여기서 해당 index를 굳이 replace했다. 반례: current가 'hello', word가'helro'인 경우 current.replace(current[index], word[index]) -> 'herro'가 된다.
                if word == target:
                    count = min(count, len(done))
                    continue

                done.add(word)
                dfs(word, done)
                done.remove(word)

    dfs(begin, set([begin]))
    return 0 if count == INF else count

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.26ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
'''

#solution 염탐
def solution2(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1: #true, false값으로 이루어진 list의 sum으로도 할 수 있겠네
                    temp_Q.append(words.pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1


#solution 염탐
from collections import defaultdict

def nextWord(cur, words):
    ret = []
    for word in words:
        cnt = 0
        for idx in range(len(word)):
            if word[idx] == cur[idx]:
                cnt += 1
        if cnt == len(cur)-1:
            ret.append(word)
    return ret

def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    count = 0
    min = 1e9

    while(len(queue) > 0):
        size = len(queue)
        count += 1

        for _ in range(size):
            key = queue.pop(0)
            visited[key] = True
            if (key == target and count < min):
                min = count
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):
                    queue.append(candidate)

    if min == 1e9:
        return 0
    else:
        return min

def solution3(begin, target, words):
    answer = bfs(begin, target, words)
    return answer