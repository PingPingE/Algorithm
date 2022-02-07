'''
문제)
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

입력)
첫째 줄에 정수 N, r, c가 주어진다.

출력)
r행 c열을 몇 번째로 방문했는지 출력한다.

제한)
1 ≤ N ≤ 15
0 ≤ r, c < 2N

'''
'''
문제)
한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.

다음 예는 22 × 22 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음은 N=3일 때의 예이다.

입력)
첫째 줄에 정수 N, r, c가 주어진다.

출력)
r행 c열을 몇 번째로 방문했는지 출력한다.

제한)
1 ≤ N ≤ 15
0 ≤ r, c < 2N

'''
#123316kb	112ms
N, r, c= map(int, input().split())
cnt= 0
status= False

def visit(row, col, size):
    global cnt,status
    # print(row,col)
    if status or (row==r and col ==c):
        print(cnt)
        status=True
        #return이 아니라 바로 나가줘야함
        exit(0)

    if size == 1:
        cnt += 1
        return
    else:
        #굳이 재귀 돌지 않아도 되는 경우
        if not (row<=r<row+size and col<=c<col+size):
            cnt += size*size
            return

        nsize = size // 2
        visit(row, col, nsize)
        visit(row, col + nsize, nsize)
        visit(row + nsize, col, nsize)
        visit(row + nsize, col + nsize, nsize)

#재귀가 깊어지지 않도록
half = 2**N//2
visit(0,0,half)
visit(0,half,half)
visit(half,0,half)
visit(half,half,half)
