#solution2 -> 다른사람의 코드를 참고해서 que의 sum을 매번 계산하지 않고 저장하는 sum_que 변수 추가
#속도가 어마어마하게 빨라졌다.

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque()
    sum_que = 0
    
    for idx in range(len(truck_weights)):#O(N) N:len(truck_weights)
        while True: #O(M) M: bridge_length
            if len(que) == bridge_length:
                tmp = que.popleft()
                sum_que -=  tmp #빼주기

            if sum_que+truck_weights[idx] >weight:
                answer += 1
                que.append(0)
            else:
                que.append(truck_weights[idx])
                sum_que += truck_weights[idx] #더해주기
                answer+=1
                break

    return answer+bridge_length

'''
정확성  테스트
테스트 1 〉	통과 (0.93ms, 10.2MB)
테스트 2 〉	통과 (7.65ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (7.49ms, 10.2MB)
테스트 5 〉	통과 (66.95ms, 10.2MB)
테스트 6 〉	통과 (29.70ms, 10.2MB)
테스트 7 〉	통과 (0.54ms, 10.2MB)
테스트 8 〉	통과 (0.10ms, 9.97MB)
테스트 9 〉	통과 (2.87ms, 10.1MB)
테스트 10 〉	통과 (0.15ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.27ms, 10.2MB)
테스트 13 〉	통과 (0.92ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''


#solution1
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    que = deque()
    
    for idx in range(len(truck_weights)):#O(N) N:len(truck_weights)
        while True: #O(M) M: bridge_length
            if len(que) == bridge_length:
                que.popleft()

            if sum(que)+truck_weights[idx] >weight:
                answer += 1
                que.append(0)
            else:
                que.append(truck_weights[idx])
                answer+=1
                break

    return answer+bridge_length


'''
정확성  테스트
테스트 1 〉	통과 (7.48ms, 10.1MB)
테스트 2 〉	통과 (1447.47ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (360.85ms, 10.1MB)
테스트 5 〉	통과 (9791.08ms, 10MB)
테스트 6 〉	통과 (1684.56ms, 10.1MB)
테스트 7 〉	통과 (5.81ms, 10.1MB)
테스트 8 〉	통과 (0.38ms, 10.2MB)
테스트 9 〉	통과 (6.41ms, 10.2MB)
테스트 10 〉	통과 (0.48ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.48ms, 10.2MB)
테스트 13 〉	통과 (2.59ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''

#다른 사람 코드
def solution(bridge_length, weight, truck_weights):
    time = 1 
    passing_truck= []
    passed_truck= []
    current_mass = 0
    time_dic = {}

    while True:
        while truck_weights:
            if weight >= current_mass + truck_weights[0]:
                passing_truck.append(truck_weights.pop(0))
                time_dic[time] = bridge_length + time 
                current_mass = sum(passing_truck)#current_mass에 sum값을 저장해놓는다
                break  
            else :
                break

        time += 1

        for out_time in time_dic:
            if time_dic[out_time] == time:
                passed_truck.append(passing_truck.pop(0))

        current_mass = sum(passing_truck)#갱신

        if passing_truck == [] and truck_weights== []:
            break
    return time

'''
정확성  테스트
테스트 1 〉	통과 (1.33ms, 10.1MB)
테스트 2 〉	통과 (15.53ms, 10.1MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (205.46ms, 10.2MB)
테스트 5 〉	통과 (4764.77ms, 10.2MB)
테스트 6 〉	통과 (857.37ms, 9.99MB)
테스트 7 〉	통과 (1.22ms, 10.1MB)
테스트 8 〉	통과 (0.40ms, 10.2MB)
테스트 9 〉	통과 (86.64ms, 10.1MB)
테스트 10 〉	통과 (0.38ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.3MB)
테스트 12 〉	통과 (1.87ms, 10.1MB)
테스트 13 〉	통과 (6.16ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
'''
