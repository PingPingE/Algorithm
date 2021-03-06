'''
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며,
그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다.
하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.
(0 ≤ x < y < 2^31)
'''
#121808kb	196ms
for _ in range(int(input())):
    x,y = map(int, input().split())
    cnt = 3 # y-x>=3을 만족한다면 3이 최소이동거리
    until = 4# 3<= y-x <= 4까지 본다는 뜻
    jump = 2 # until 얼마만큼 늘릴건지 -> 2,4,6,9,12,16,... 즉 +2,+2,+3,+3,+4,+4... 한 jump당 두 번 적용됨
    stat  =0 # stat이 1이면 jump +=1 
    if y-x <3:
        print(y-x)
        continue
    while 1:
        if y-x>until:
            if stat == 1:
                jump += 1
                stat = 0
            else:
                stat ^= 1
            until += jump
            cnt += 1
        else:
            break
    print(cnt)

