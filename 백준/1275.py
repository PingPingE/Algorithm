'''
문제)
모두 알다시피 동호는 커피숍의 마담이다. (마담이 무엇인지는 본인에게 물어보도록 하자.)

어느 날 커피숍의 손님 A씨가 동호에게 게임을 하자고 했다.

그 게임은 다음과 같은 규칙을 갖는다.

N개의 정수가 있으면, 동호는 다음과 같이 말한다. “3~7번째 수의 합은 무엇이죠?” 그러면 상대방은 “그 답은 000입니다. 
그리고 8번째 수를 2로 고치도록 하죠” 그러면 동호는 “네 알겠습니다.”라고 한 뒤에 다시 상대방이 동호가 했던 것처럼 “8~9번째 수의 합은 무엇이죠?”라고 묻게된다. 
이 것을 번갈아 가면서 반복하는 게임이다.

당신은 이 게임의 심판 역을 맡았다. 요컨대, 질문에 대한 답들을 미리 알아야 한다는 것이다.

당신의 머리가 출중하다면 10만개 가량 되는 정수와 10만턴 정도 되는 게임을 기억할 수 있을 것이다. 
몇판 이 게임을 즐기던 동호는 많은 사람들이 이 게임을 하기를 바라게 되었고, 당신에게 심판 프로그램을 구현해달라고 요청했다.

입력)
첫째 줄에 수의 개수 N과 턴의 개수 Q가 주어진다.(1 ≤ N, Q ≤ 100,000) 둘째 줄에는 처음 배열에 들어가 있는 정수 N개가 주어진다. 
세 번째 줄에서 Q+2번째 줄까지는 x y a b의 형식으로 x~y까지의 합을 구하여라, a번째 수를 b로 바꾸어라 라는 뜻의 데이터가 주어진다.

입력되는 모든 수는 -231보다 크거나 같고, 231-1보다 작거나 같은 정수이다.

출력)
한 턴마다 구한 합을 한 줄마다 한 개씩 출력한다.
'''
#세그먼트트리로 구현 (참고: https://jaimemin.tistory.com/815)
#45884kb	3480ms
import sys,math
sys.setrecursionlimit(10**9)
N,Q= map(int, input().split())
nodes= [0 for _ in range(N*4)] #==일단 넉넉하게
arr=list(map(int, sys.stdin.readline().split()))

def init(n,l,r):
    if l==r: #==리프노드
        nodes[n]=arr[l]
        return nodes[n]
    else:
        m=(l+r)//2
        left= init(n*2, l,m)
        right=init(n*2+1, m+1,r)
        nodes[n]=left+right
        return nodes[n]

def sum(l,r, n, cur_l, cur_r): #== [l,r]의 합을 구하기 위해 n번째 node를 보고 있고, 현재의 범위는 [cur_l,cur_r]
    if r<cur_l or l>cur_r: return 0
    if l<=cur_l and r>=cur_r: return nodes[n] #===구간에 들어옴
    m=(cur_l+cur_r)//2
    return sum(l,r,n*2,cur_l,m)+sum(l,r,n*2+1,m+1,cur_r) #===쪼개서 재귀

def update(idx, val, n, cur_l, cur_r):#arr의 idx번째 원소(리프노드)를 val로 바꾸기 위해 n번째 node를 보고 있고, 현재의 범위는 [cur_l,cur_r]
    if idx<cur_l or idx>cur_r: return nodes[n]
    if cur_r==cur_l:
        nodes[n] = val
        return nodes[n]
    m=(cur_l+cur_r)//2
    nodes[n]= update(idx, val, n*2, cur_l, m) + update(idx, val, n*2+1, m+1, cur_r)
    return nodes[n]

init(1,0,N-1)
for _ in range(Q):
    x,y,a,b= map(int, sys.stdin.readline().split())
    if x>y:
        x,y=y,x
    print(sum(x-1,y-1,1,0,N-1))
    update(a-1,b,1,0,N-1)


#===시간 초과 코드====
#===값을 바꾸는 연산이 많으므로 prefix-sum 알고리즘을 적용하는 것은 적절하지 않았음
import sys
N,Q= map(int, input().split())
num=[0 for _ in range(N+1)] #==원소 저장
p_sum = [0 for _ in range(N+1)] #===누적합
for e,i in enumerate(map(int, sys.stdin.readline().split())):
    p_sum[e+1] = p_sum[e]+i
    num[e+1]=i

for _ in range(Q):
    x,y,a,b= map(int, sys.stdin.readline().split())
    if x>y:
        x,y=y,x
    print(p_sum[y]-p_sum[x-1])
    diff=b-num[a]#==차이 구하고
    num[a]=b #바꿔주고
    for i in range(a,N+1): #===O(N)
        p_sum[i] += diff
