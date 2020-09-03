def solution(s):
    answer = 1001
    if len(s) <=2:
        return len(s)
    for n in range(1,len(s)//2+1): #몇개씩 볼건지
        target= s[:n]#비교대상선정
        cnt = 1
        new_s =[]
        for i in range(n,len(s),n):
            if target == s[i:i+n]:
                cnt += 1
            else:
                if cnt >1:#target과 같은 문자열이 2번이상 나왔다면 숫자 붙여서 저장
                    new_s.append(f"{cnt}{target}")
                else:
                    new_s.append(target)
                target = s[i:i+n]
                cnt =1
                
        if cnt >1:
            new_s.append(f"{cnt}{target}")
        else:
            new_s.append(target)
            
        answer = min(answer, len(''.join(new_s))) 
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 9.59MB)
테스트 2 〉	통과 (0.56ms, 9.46MB)
테스트 3 〉	통과 (0.30ms, 9.51MB)
테스트 4 〉	통과 (0.04ms, 9.7MB)
테스트 5 〉	통과 (0.00ms, 9.53MB)
테스트 6 〉	통과 (0.06ms, 9.63MB)
테스트 7 〉	통과 (0.69ms, 9.52MB)
테스트 8 〉	통과 (0.81ms, 9.39MB)
테스트 9 〉	통과 (1.09ms, 9.63MB)
테스트 10 〉	통과 (2.65ms, 9.47MB)
테스트 11 〉	통과 (0.13ms, 9.7MB)
테스트 12 〉	통과 (0.14ms, 9.46MB)
테스트 13 〉	통과 (0.18ms, 9.45MB)
테스트 14 〉	통과 (1.00ms, 9.5MB)
테스트 15 〉	통과 (0.17ms, 9.5MB)
테스트 16 〉	통과 (0.02ms, 9.5MB)
테스트 17 〉	통과 (1.51ms, 9.52MB)
테스트 18 〉	통과 (1.44ms, 9.53MB)
테스트 19 〉	통과 (1.83ms, 9.54MB)
테스트 20 〉	통과 (3.26ms, 9.58MB)
테스트 21 〉	통과 (3.19ms, 9.67MB)
테스트 22 〉	통과 (3.15ms, 9.43MB)
테스트 23 〉	통과 (3.07ms, 9.53MB)
테스트 24 〉	통과 (2.96ms, 9.69MB)
테스트 25 〉	통과 (3.06ms, 9.57MB)
테스트 26 〉	통과 (3.15ms, 9.56MB)
테스트 27 〉	통과 (4.97ms, 9.49MB)
테스트 28 〉	통과 (0.02ms, 9.57MB)
'''