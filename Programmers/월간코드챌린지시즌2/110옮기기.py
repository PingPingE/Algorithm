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

        
        '''
        1. 0의 시작 위치를 찾는다. -> idx
        2. 0이 없거나(idx==-1) 있어도 110 이상인 경우(idx>=2)는 '110'*cnt를 가장 앞에
        3. 그 외 -> q_str[:idx+0개수] + '110'*cnt + q_str[idx+0개수:]
        '''
        #1
        q_str = ''.join(que)
        idx=q_str.find('0')
        print(q_str, idx)
        
        #2
        if idx==-1 or idx >=2:
            answer.append('110'*cnt + q_str)
        else:
            #3
            z_cnt = 0
            for i in range(idx, len(que)):
                if que[i] =='0':
                    z_cnt+=1
                else: break
            answer.append(q_str[:idx+z_cnt] + '110'*cnt + q_str[idx+z_cnt:] )

    return answer