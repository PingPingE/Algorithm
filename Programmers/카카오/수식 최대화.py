#sol1
import re
from itertools import permutations
def cal(n1,n2,op):
    return int(n1)+int(n2) if op=='+' else(int(n1)-int(n2) if op=='-' else int(n1)*int(n2)) 
def solution(expression):
    answer = 0
    op = []  # 연산자 순서대로
    number = list(map(int, re.findall('[0-9]+', expression)))  # 숫자 순서대로
    prev = 0
    for num in number[:-1]:#연산자 추출(정규식 활용하는 것보다 조금 더 빠름)
        target_op = expression[prev + len(str(num))]
        op.append(target_op)
        prev = prev+len(str(num))+1

    valid = set(op)
    for p in list(permutations(valid, len(valid))):
        tmp_num = number[:]
        tmp_op = op[:]
        for p1 in p:
            e = 0
            while p1 in tmp_op:
                if tmp_op[e] == p1:
                    tmp_num[e] = cal(tmp_num[e], tmp_num[e + 1], p1) #eval로하면 더 느림
                    del(tmp_op[e])
                    del(tmp_num[e+1])
                else:
                    e += 1
        answer = max(abs(tmp_num[0]), answer)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.14ms, 10.9MB)
테스트 2 〉	통과 (0.15ms, 10.9MB)
테스트 3 〉	통과 (0.16ms, 10.9MB)
테스트 4 〉	통과 (0.19ms, 10.9MB)
테스트 5 〉	통과 (0.20ms, 10.9MB)
테스트 6 〉	통과 (0.18ms, 10.9MB)
테스트 7 〉	통과 (0.19ms, 10.9MB)
테스트 8 〉	통과 (0.19ms, 10.9MB)
테스트 9 〉	통과 (0.22ms, 10.9MB)
테스트 10 〉	통과 (0.21ms, 10.9MB)
테스트 11 〉	통과 (0.21ms, 10.9MB)
테스트 12 〉	통과 (0.24ms, 11MB)
테스트 13 〉	통과 (0.23ms, 10.9MB)
테스트 14 〉	통과 (0.26ms, 11MB)
테스트 15 〉	통과 (0.28ms, 10.9MB)
테스트 16 〉	통과 (0.16ms, 11MB)
테스트 17 〉	통과 (0.17ms, 10.9MB)
테스트 18 〉	통과 (0.15ms, 10.9MB)
테스트 19 〉	통과 (0.14ms, 10.9MB)
테스트 20 〉	통과 (0.14ms, 10.9MB)
테스트 21 〉	통과 (0.17ms, 10.9MB)
테스트 22 〉	통과 (0.18ms, 11MB)
테스트 23 〉	통과 (0.14ms, 10.9MB)
테스트 24 〉	통과 (0.28ms, 10.9MB)
테스트 25 〉	통과 (0.25ms, 10.9MB)
테스트 26 〉	통과 (0.14ms, 10.9MB)
테스트 27 〉	통과 (0.27ms, 10.9MB)
테스트 28 〉	통과 (0.20ms, 10.9MB)
테스트 29 〉	통과 (0.20ms, 10.9MB)
테스트 30 〉	통과 (0.19ms, 10.9MB)
'''

#sol2
import re
from itertools import permutations
def get_res(op_order, num, op):
    for cur_op in op_order:
        while cur_op in op:
            for e,o in enumerate(op):
                if o == cur_op:
                    num[e] = eval(f"{num[e]}{cur_op}{num[e+1]}")
                    del(num[e+1])
                    del(op[e])
                    break
    return abs(int(num[0]))
                    
def solution(expression):
    ans = 0
    num = re.findall('[0-9]+',expression)
    op = re.findall('[-]|[*]|[+]',expression)
    for op_order in permutations(set(op), len(set(op))):
        ans=max(ans, get_res(op_order, num[:], op[:]))
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.24ms, 10.7MB)
테스트 2 〉	통과 (0.25ms, 10.7MB)
테스트 3 〉	통과 (0.41ms, 10.8MB)
테스트 4 〉	통과 (0.44ms, 10.8MB)
테스트 5 〉	통과 (0.53ms, 10.8MB)
테스트 6 〉	통과 (0.46ms, 10.7MB)
테스트 7 〉	통과 (0.62ms, 10.8MB)
테스트 8 〉	통과 (0.56ms, 10.8MB)
테스트 9 〉	통과 (0.62ms, 10.8MB)
테스트 10 〉	통과 (0.67ms, 10.7MB)
테스트 11 〉	통과 (0.61ms, 10.8MB)
테스트 12 〉	통과 (0.69ms, 10.8MB)
테스트 13 〉	통과 (0.73ms, 10.8MB)
테스트 14 〉	통과 (0.84ms, 10.7MB)
테스트 15 〉	통과 (0.89ms, 10.7MB)
테스트 16 〉	통과 (0.31ms, 10.8MB)
테스트 17 〉	통과 (0.35ms, 10.7MB)
테스트 18 〉	통과 (0.25ms, 10.7MB)
테스트 19 〉	통과 (0.23ms, 10.7MB)
테스트 20 〉	통과 (0.25ms, 10.8MB)
테스트 21 〉	통과 (0.30ms, 10.7MB)
테스트 22 〉	통과 (0.32ms, 10.8MB)
테스트 23 〉	통과 (0.20ms, 10.7MB)
테스트 24 〉	통과 (0.91ms, 10.9MB)
테스트 25 〉	통과 (0.89ms, 10.8MB)
테스트 26 〉	통과 (0.22ms, 10.7MB)
테스트 27 〉	통과 (0.90ms, 10.8MB)
테스트 28 〉	통과 (0.48ms, 10.8MB)
테스트 29 〉	통과 (0.39ms, 10.8MB)
테스트 30 〉	통과 (0.42ms, 10.7MB)
'''

#sol3
import re
from itertools import permutations
def cal(n1,n2,op):
    return int(n1)+int(n2) if op=='+' else(int(n1)-int(n2) if op=='-' else int(n1)*int(n2)) 
def get_res(op_order, num, op):
    for cur_op in op_order:
        while cur_op in op:
            for e,o in enumerate(op):
                if o == cur_op:
                    #num[e] = eval(f"{num[e]}{cur_op}{num[e+1]}")
                    num[e] = cal(num[e],num[e+1],cur_op)
                    del(num[e+1])
                    del(op[e])
                    break
    return abs(int(num[0]))
                    
def solution(expression):
    ans = 0
    num = re.findall('[0-9]+',expression)
    op = re.findall('[-]|[*]|[+]',expression)
    for op_order in permutations(set(op), len(set(op))):
        ans=max(ans, get_res(op_order, num[:], op[:]))
    return ans

'''
정확성  테스트
테스트 1 〉	통과 (0.20ms, 10.8MB)
테스트 2 〉	통과 (0.20ms, 10.9MB)
테스트 3 〉	통과 (0.23ms, 10.9MB)
테스트 4 〉	통과 (0.24ms, 10.9MB)
테스트 5 〉	통과 (0.27ms, 10.8MB)
테스트 6 〉	통과 (0.25ms, 10.9MB)
테스트 7 〉	통과 (0.26ms, 11MB)
테스트 8 〉	통과 (0.27ms, 10.9MB)
테스트 9 〉	통과 (0.27ms, 10.9MB)
테스트 10 〉	통과 (0.32ms, 10.9MB)
테스트 11 〉	통과 (0.27ms, 10.9MB)
테스트 12 〉	통과 (0.30ms, 11MB)
테스트 13 〉	통과 (0.62ms, 11MB)
테스트 14 〉	통과 (0.34ms, 10.9MB)
테스트 15 〉	통과 (0.35ms, 10.9MB)
테스트 16 〉	통과 (0.21ms, 10.9MB)
테스트 17 〉	통과 (0.22ms, 10.9MB)
테스트 18 〉	통과 (0.25ms, 10.9MB)
테스트 19 〉	통과 (0.20ms, 10.9MB)
테스트 20 〉	통과 (0.24ms, 10.9MB)
테스트 21 〉	통과 (0.24ms, 10.9MB)
테스트 22 〉	통과 (0.23ms, 10.9MB)
테스트 23 〉	통과 (0.19ms, 10.9MB)
테스트 24 〉	통과 (0.36ms, 10.9MB)
테스트 25 〉	통과 (0.34ms, 11MB)
테스트 26 〉	통과 (0.19ms, 10.9MB)
테스트 27 〉	통과 (0.37ms, 10.9MB)
테스트 28 〉	통과 (0.26ms, 10.9MB)
테스트 29 〉	통과 (0.25ms, 10.9MB)
테스트 30 〉	통과 (0.24ms, 10.9MB)
'''