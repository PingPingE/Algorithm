from collections import deque
def solution(s):
    answer = []
    for i in s:
        st, que = list(i), deque()
        cnt = 0
        while st:
            que.appendleft(st.pop())
            if len(que) > 2 and que[0] == '1' and que[0] == que[1] != que[2]:
                cnt += 1
                for _ in range(3):
                    que.popleft()

        q_str = ''.join(que)

        '''
        이전 로직은 q_str이 '1010' 같은 반례가 있었음(오답:'10'+'110'*cnt+'10', 정답:'1010'+'110'*cnt)
        그래서 흔한 '1'보다는 '11'을 찾고, '11'이 없더라도 마지막으로 '0'이 나오는 인덱스를 찾음으로써 커버
        + 11을 찾는다면 그 앞에 바로 넣으면 되니까 이전 로직처럼 '1'다음에 '0'이 몇 개오는지 세는 연산 필요 X 
        '''

        # '11'이 시작하는 인덱스 찾기
        idx = q_str.find('11')
        # 마지막 '0' 인덱스 찾기
        z_idx = q_str.rfind('0')

        if idx == -1:
            answer.append(q_str[:z_idx + 1] + '110' * cnt + q_str[z_idx + 1:])
        else:
            answer.append(q_str[:idx] + '110' * cnt + q_str[idx:])

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (277.77ms, 15.8MB)
테스트 2 〉	통과 (254.25ms, 15.8MB)
테스트 3 〉	통과 (195.71ms, 16MB)
테스트 4 〉	통과 (291.50ms, 21.3MB)
테스트 5 〉	통과 (291.92ms, 16MB)
테스트 6 〉	통과 (322.52ms, 16MB)
테스트 7 〉	통과 (210.26ms, 15.8MB)
테스트 8 〉	통과 (147.85ms, 15.1MB)
테스트 9 〉	통과 (315.93ms, 30.4MB)
테스트 10 〉	통과 (295.38ms, 31.9MB)
테스트 11 〉	통과 (301.63ms, 30.6MB)
테스트 12 〉	통과 (297.30ms, 30.7MB)
테스트 13 〉	통과 (313.45ms, 30.4MB)
테스트 14 〉	통과 (300.97ms, 30.1MB)
테스트 15 〉	통과 (315.37ms, 30.1MB)
테스트 16 〉	통과 (316.50ms, 30.1MB)
테스트 17 〉	통과 (274.22ms, 29.1MB)
테스트 18 〉	통과 (313.42ms, 17MB)
테스트 19 〉	통과 (315.77ms, 20.6MB)
테스트 20 〉	통과 (263.07ms, 15.6MB)
테스트 21 〉	통과 (324.22ms, 23.6MB)
'''