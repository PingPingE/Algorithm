'''
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

[제한사항]
numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

'''
def solution(numbers, hand):
    hand = 'L' if hand == 'left' else 'R'
    answer= ''
    cur = {'L':'*', 'R':'#'}
    dic = {1: (0, 0), 2: (0, 1), 3: (0, 2), \
           4: (1, 0), 5: (1, 1), 6: (1, 2), \
           7: (2, 0), 8: (2, 1), 9: (2, 2), \
           '*':(3, 0), 0:(3, 1), '#':(3, 2)}

    def get_distance(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    def left(num):
        nonlocal answer,cur
        answer+='L'
        cur['L']=num

    def right(num):
        nonlocal answer,cur
        answer+='R'
        cur['R']=num
           
    for num in numbers:
        if num in (1,4,7):
            left(num)
        elif num in (3,6,9):
            right(num)
        else:
            dist_L = get_distance(dic[cur['L']],dic[num])
            dist_R = get_distance(dic[cur['R']],dic[num])
            if dist_L < dist_R:
                left(num)
            elif dist_L>dist_R:
                right(num)
            else:
                if hand=='L':left(num)
                else:right(num)
           
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.09ms, 10.3MB)
테스트 15 〉	통과 (0.23ms, 10.3MB)
테스트 16 〉	통과 (0.25ms, 10.3MB)
테스트 17 〉	통과 (0.49ms, 10.3MB)
테스트 18 〉	통과 (0.41ms, 10.3MB)
테스트 19 〉	통과 (0.72ms, 10.3MB)
테스트 20 〉	통과 (0.47ms, 10.3MB)
'''
