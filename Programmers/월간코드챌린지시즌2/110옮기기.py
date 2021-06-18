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

        que = ''.join(que)
        if len(que)<3:
            idx=que.find('1')
            if idx==-1:
                answer.append(''.join(que)+'110'*cnt)
            else:
                answer.append(que[:idx] + '110'*cnt + que[idx:])
        else:
            idx=que.find('111')
            if idx==-1:
                answer.append(''.join(que)+'110'*cnt )
            else:
                answer.append(que[:idx] + '110'*cnt + que[idx:] )

    return answer