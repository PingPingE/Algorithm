'''
손익분기점
A: 고정비용, B: 가변비용, C:제품가격
'''
#29380kb 60ms
A,B,C = map(int, input().split())
print(-1 if C-B<=0 else A//(C-B)+1)
