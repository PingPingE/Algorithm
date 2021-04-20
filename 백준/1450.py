'''
문제
세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.

N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 C가 주어진다. N은 30보다 작거나 같은 자연수이고, C는 10^9보다 작거나 같은 음이아닌 정수이고.
둘째 줄에 물건의 무게가 주어진다. 무게도 10^9보다 작거나 같은 자연수이다.

출력
첫째 줄에 가방에 넣는 방법의 수를 출력한다.
'''
#한 번에 다 보고 모든 경우의 수를 구하면 시간 초과나니까
# 1. 반으로 쪼개고([0,N//2), [N//2,N))
# 2. 해당하는 값들로 경우의 수를 구해서 A와 B에 저장했다가
# 3. A,B 원소를 하나씩 더했을 때 조건 만족하는거 카운트 -> 이분 탐색으로 시간 절약

#126644kb	192ms
N,C = map(int, input().split())
targets=sorted(map(int, input().split()))
A,B=[],[]
cnt=0
def binary_search(x):
    l,r=0,len(B)-1
    while l<=r:
        m=(l+r)//2
        if B[m]+x>C:
            r=m-1
        else:
            l=m+1
    return l

def sol(idx, w, end, stat):#인덱스, 현재 무게, 끝 인덱스, A에 넣을건지(1) B에 넣을건지(0)
    if w>C: return
    if idx>=end:
        if stat:#A에 넣어야하면
            A.append(w)
        else:
            B.append(w)
        return

    sol(idx+1, w+targets[idx], end, stat) #포함
    sol(idx+1, w, end, stat) #포함X

sol(0,0,N//2,1)#===A에 먼저 넣고
A.sort()
sol(N//2,0,N,0)#===B에 넣고
B.sort()
for a in A:#A,B 조합해서 조건 만족하는거 카운트
    cnt+=binary_search(a)
print(cnt)
