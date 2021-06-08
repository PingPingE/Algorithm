#틀린 로직
from collections import deque
def solution(a):
    def check(e):
        st1, st2 = [a[e]], deque(a[e+1:])
        flag = 1 #작은 값을 버릴 수 있는 횟수
        remain = 0
        while st1 or st2:
            if st1 and st2:
                if st1[-1] > st2[0]:  # st1의 top이 더 큰 경우
                    if remain == 0:  # st1의 top이 a[e]인 경우
                        st1.append(st2.popleft())  # 일단 flag안쓰고 st2 top가져오기(사실 deque지만 편의상)
                        remain += 1  # 가져온거 표시

                    else:  # st1의 top이 a[e]이 아닌 경우(더 추가된 경우)
                        st1.pop() #그럼 버려도 되지
                        remain -= 1
                else:
                    st2.popleft()
            elif st1:
                if st1[0] != min(st1):
                    flag=0
                break

        # 해당 a[e]가 못남는 경우(a[:e]의 최솟값을 못지우는 경우)
        if minn < st1[0] and flag == 0:
            return False
        return True

    cnt = 0
    maxx = -1000000001
    minn = 1000000001
    for e, i in enumerate(a):
        minn = min(minn, i)

        #이때까지 통과한 숫자 중 가장 큰 숫자 보다 작으면 프리패스
        if maxx > i:
            print("free pass==> ",i)
            cnt += 1
            continue
        if check(e):
            print("check===> ", i)
            cnt+=1
            maxx = max(maxx,i)
    return cnt

# print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))