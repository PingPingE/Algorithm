'''
문제
게임을 좋아하는 큐브러버는 체스에서 사용할 새로운 말 "데스 나이트"를 만들었다.
데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자.
체스판의 행과 열은 0번부터 시작한다.

데스 나이트는 체스판 밖으로 벗어날 수 없다.

입력
첫째 줄에 체스판의 크기 N(5 ≤ N ≤ 200)이 주어진다. 둘째 줄에 r1, c1, r2, c2가 주어진다.

출력
첫째 줄에 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.

'''

#125908kb	148ms
from collections import deque
N=int(input())
r1,c1,r2,c2=map(int, input().split())
que=deque([(r1,c1,0)])
dy,dx=[-2,-2,0,0,2,2],[1,-1,2,-2,1,-1]#이동 가능 방향
ans=-1
stat=((r1,c1)==(r2,c2))#도착 여부
done=set([(r1,c1)])
while que and not stat:
    r,c,cnt=que.popleft()
    for d in range(6):
        nr,nc=r+dy[d],c+dx[d]
        if nr<0 or nc<0 or nr>=N or nc>=N or (nr,nc) in done:
            continue

        if (nr,nc)==(r2,c2):
            stat=True
            ans=cnt+1
            break

        done.add((nr,nc))
        que.append((nr,nc,cnt+1))
print(ans)