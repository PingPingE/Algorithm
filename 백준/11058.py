'''
크리보드는 kriii가 만든 신기한 키보드이다. 크리보드에는 버튼이 4개만 있으며, 하는 역할은 다음과 같다.

화면에 A를 출력한다.
Ctrl-A: 화면을 전체 선택한다
Ctrl-C: 전체 선택한 내용을 버퍼에 복사한다
Ctrl-V: 버퍼가 비어있지 않은 경우에는 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용을 붙여넣는다.
크리보드의 버튼을 총 N번 눌러서 화면에 출력된 A개수를 최대로하는 프로그램을 작성하시오.

1 ≤ N ≤ 100

'''
import sys
sys.setrecursionlimit(10**8)
N= int(input())
res = [0 for _ in range(N+1)]
def sol(n):
    if n<=0 : return 0
    if res[n] == 0:
        res[n] = max(sol(n-1)+1, sol(n-3)*2, sol(n-4)*3, sol(n-5)*4)
    return res[n]
print(sol(N))