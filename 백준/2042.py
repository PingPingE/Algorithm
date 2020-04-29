import sys
import math
#111684kb	1376ms
sys.setrecursionlimit(10**8)
def update(t_index, to_num):
    t_index  += size//2
    tree[t_index] = to_num
    while t_index>1:
        t_index//=2
        tree[t_index] = tree[t_index*2]+tree[t_index*2+1]

def get_sum(L,R,n_index, nodeL, nodeR):
    if L>nodeR or R<nodeL: return 0
    if L<=nodeL and R>=nodeR : return tree[n_index]
    mid = (nodeL+nodeR)//2
    return get_sum(L,R,n_index*2, nodeL, mid)+get_sum(L,R,n_index*2+1,mid+1, nodeR)

N,M,K = map(int, sys.stdin.readline().split())
size = 1<<math.ceil(math.log2(N))+1#포화 이진트리를 만들기 위함
tree = [0 for _ in range(size)]#루트노드 인덱스: 1
for _ in range(N):
    tree[size//2+_] = int(sys.stdin.readline())
#세그먼트 트리 만들기
for i in range(size//2-1, 0,-1):
    tree[i] = tree[i*2] + tree[i*2+1]

for _ in range(M+K):
    a,b,c = map(int, input().split())
    if a == 1:
        update(b-1,c)
    else:
        print(get_sum(b-1,c-1,1,0,size-size//2-1))