'''
문제
가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다.
i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

출력
총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.
'''
#index로 보는거임 value가 아님
import sys
def dfs(from_):
    global ans_arr
    st = []
    for e,data in enumerate(arr[from_]):
        if data == 1:
            st.append((from_,e))

    while st:
        y,x = st.pop()
        if ans_arr[y][x] >0:
            continue
        ans_arr[y][x] = 1
        for i in range(N):
            if arr[x][i] == 1 and ans_arr[x][i] == 0:
                st.append((x,i))

N = int(input())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
ans_arr = [[0]*N for _ in range(N)]

for i in range(N):
    dfs(i)
            
for a in ans_arr:
    print(' '.join(map(str, a)))