#1107: 리모컨
#스터디 후 2차시도
#T1: 8분 42초
#T2: 14분 37초(5분 55초)
#T3: 20분 48초(6분 11초) --> 런타임에러의 원인: M이 0일때도 input을 받도록 되어있었음
#123604kb 316ms

def check(x):#해당 숫자를 만들 수 있는지
    st= str(x)
    for s in st:
        if s in broken:
            return False
    return True

N = int(input())
M = int(input())
if M>0:
    broken = list(map(str, input().split()))
else:
    broken=[]
mini = abs(100-N)
if mini<=1 or M == 10: print(mini)
else:
    for i in range(0,1000000):#N이 최대 50만인데 100에서 + 버튼으로 49만9900번만에 갈 수 있으므로 약 100만 이상은 볼 필요가 없다.
        if check(i):
            mini = min(mini, len(str(i))+abs(i-N))
    print(mini)

