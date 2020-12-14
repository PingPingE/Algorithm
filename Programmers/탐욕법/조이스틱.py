'''
문제 설명)
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항)
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
'''

#풀이 참고: https://jayrightthere.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
def solution(name):
    answer = 0
    leng=len(name)
    move = leng
    for e,n in enumerate(name):
        cnt = min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
        next_idx = e+1
        while next_idx<leng and name[next_idx] == 'A': #다음 A가 아닌 알파벳을 만날때까지(오른쪽)
            next_idx +=1
        move =min(move, e+leng-next_idx+min(e, leng-next_idx)) #+min: 첫시작 오른쪽이 빠르냐(e) 왼쪽이 빠르냐(leng-next_idx)
        answer += cnt
    return answer + move

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
'''


#=====실패======================
#T1: 8분 4초
#T2: 25분 33초(17분 29초)
#T3: 75분 3초(50분 30초) -> 중단

from collections import deque
def solution(name):
    answer = 987654321
    que = deque() #현재 인덱스, 조작 횟수, done
    que.append([0,0,set([0])])
    print(que)
    while que:
        idx, cnt, done = que.popleft()
        print(idx, cnt, done, answer)
        n = name[idx]
        left = ord(n)-65
        right=  90-ord(n)+1
        if left> right:
            cnt += right
        else: cnt +=left

        if len(done) == len(name):
            answer =min(answer, cnt)
        else:
            tmp = idx - 1 if idx - 1 >= 0 else len(name) - 1
            tmp2 = idx + 1 if idx + 1 < len(name) else 0
            print("cur:", idx, "tmp:", tmp, "tmp2:", tmp2)
            if tmp not in done:
                if name[tmp] == 'A':
                    for i in range(len(name)):
                        if i in done: continue
                        if name[i] != 'A':
                            break
                    else:
                        answer = min(answer, cnt)
                        continue
                que.append([tmp, cnt+1, done|{tmp}])
            if tmp2 not in done:
                if name[tmp2] == 'A':
                    for i in range(len(name)):
                        if i in done: continue
                        if name[i] != 'A':
                            break
                    else:
                        answer = min(answer, cnt)
                        continue
                que.append([tmp2, cnt+1, done|{tmp2}])
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.3MB)
테스트 10 〉	통과 (0.05ms, 10.3MB)
테스트 11 〉	실패 (0.06ms, 10.2MB)
'''
