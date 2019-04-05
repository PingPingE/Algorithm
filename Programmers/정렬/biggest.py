'''
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''
def swap(arr,i,j): #원소 바꾸기
    arr[i], arr[j] = arr[j],arr[i]
def solution(numbers):
    answer = ''
    while len(numbers)>=2:
        for i in range(len(numbers)-1):
            s1 = str(numbers[i])
            s2 = str(numbers[i+1])

            if s1[0] > s2[0]:
                swap(numbers,i,i+1)
            elif s1[0] == s2[0]:
                n = min(len(s1),len(s2))
                if n <= 1:
                    if len(s2) == 1:
                        if s1[1] > s1[0]:
                            swap(numbers,i,i+1)
                            continue
                    elif len(s1) ==1 :
                        if s2[1] < s2[0]:
                            swap(numbers,i,i+1)
                            continue
                    continue
                else:
                    j= 1
                    k = 1
                    while j<len(s1) or k<len(s2):
                        if s1[j] > s2[k]:
                            swap(numbers,i,i+1)
                            break
                        elif s1[j] < s2[k]:
                            break
                        if j<len(s1)-1:
                            j += 1
                        if k < len(s2)-1:
                            k += 1

        answer += str(numbers[-1])
        del(numbers[-1])
    answer += str(numbers[0]) #마지막 남은 원소 붙이
    return answer

#시간초과로 실패... 
