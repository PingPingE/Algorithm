#하노이의 탑
'''
하노이의 탑(Tower of Hanoi)은 퍼즐의 일종이다. 세 개의 기둥과 이 기둥에 꽂을 수 있는 크기가 다양한 원판들이 있고,
퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있다.

게임의 목적은 다음 두 가지 조건을 만족시키면서, 한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것이다.

1. 한번에 하나의 원판만 옮길 수 있다
2. 큰 원판이 작은 원판 위에 있어서는 안된다.
'''

def hanoi(n, start, end, temp):#옮길 원반 개수, 시작, 목표, 중간
    if n==1:
        print(start, "->", end)
        return
    else:
        hanoi(n-1, start, temp, end)#마지막 가장 큰 원반 빼고 temp로 이동
        print(start, "->", end)
        hanoi(n-1, temp, end, start)
    
cnt = 0
n = int(input()) #원반 갯수
print(hanoi(n,1,3,2))
    
    
