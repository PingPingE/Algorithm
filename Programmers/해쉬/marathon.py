#해쉬
'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''
def solution(participant, completion):
    m = {}
    for i  in participant:
        if i not in m.keys(): #key값엔 참가자 이름, value는 해당이름을 가진 참가자의 수
            m[i] = 1
        else:
            m[i] += 1 #동명이인이 있을 수 있으므로 
    for j in completion:
        if j in m.keys(): #완주자 리스트에 있는 참가자면 -1
            m[j] -= 1
        
    tmp = max(m.keys(), key =(lambda k:m[k])) #가장 큰 값을 가지는 key 리턴
    return tmp

#정확성(50), 효율성(50) 테스트통과(100)
