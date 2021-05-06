'''
문제)
상근이는 문자열에 폭발 문자열을 심어 놓았다. 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

폭발은 다음과 같은 과정으로 진행된다.

문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
상근이는 모든 폭발이 끝난 후에 어떤 문자열이 남는지 구해보려고 한다. 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력한다.

폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다.

입력)
첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.

둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.

두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.

출력)
첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력한다.
'''
#===시도2: 구간 [s,e) 만큼 조금씩만 보면 어떨까 -> 13%에서 시간초과
cur_str=input()
bomb_str=input()
s,e=0,len(bomb_str)
while s<e and e<=len(cur_str):
    if cur_str[s:e] == bomb_str: #===bomb_str은 길어봤자 36이라 문제될 것이 없는데..
        cur_str=cur_str[:s]+cur_str[e:] #===이 부분이 문제인듯
        diff= s-len(bomb_str)
        remain= 0 if diff>=0 else -diff
        s,e= diff+remain, e+remain-len(bomb_str)

    else:
        s+=1
        e+=1

print(cur_str if cur_str else 'FRULA')

#===시도1: replace 메서드 적용 -> 49%에서 시간초과
cur_str=input()
bomb_str=input()
while True:
    before=len(cur_str)
    cur_str=cur_str.replace(bomb_str,'')
    if len(cur_str) == before:
        break
print(cur_str if cur_str else 'FRULA')