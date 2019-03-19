
cnt =0

def hanoi(n, start, end, temp):#옮길 원판 개수, 시작기둥, 도착기둥, 보조기둥
    global cnt #전역 변수 cnt 사용
    cnt += 1
    if n==1:
        print("{} -> {}".format(start,end))
        return
    hanoi(n-1, start, temp, end)#n-1개의 원판을 보조기둥으로 모두 이동
    print("{} -> {}".format(start, end))#시작기둥에 남은 가장 큰 원판을 도착기둥으로 이동
    hanoi(n-1, temp,end,start) #n-1개의 원판을 보조기둥에서 도착기둥으로 이동
    
    
hanoi(3,1,3,2)
print(cnt)
cnt = 0
hanoi(6,1,3,2)
print(cnt)
cnt = 0
hanoi(5,1,3,2)
print(cnt)
