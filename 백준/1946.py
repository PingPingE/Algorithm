#서류, 면접성적을 모두 비교했을 때 둘 다 밀리는 경쟁자가 있으면 탈락
import sys
sys.setrecursionlimit(10**6)
T= int(input())
while T != 0 :
    N = int(input())
    arr = []
    cnt = 1
    T -= 1
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))
    #서류기준 sorting
    arr.sort()
    #서류 1등의 면접 점수
    tmp = arr[0][1]
    if tmp == 1:
        cnt = 1
    else:
        for k in arr:
            b= k[1]
            if b<tmp:
                #tmp값은 서류 1등의 면접등수보다 높은 사람들 중 가장 높은 등수로 갱신
                tmp = b
                cnt+=1
    print(cnt)

#숏코딩
# import sys
# input=sys.stdin.readline
# for tc in range(int(input())):
# 	n=int(input())
# 	a=[0]*n
# 	for i in range(n):
# 		x,y=map(int,input().split())
# 		a[x-1]=y-1
# 	j=n
# 	r=0
# 	for i in range(n):
# 		if a[i]<j:
# 			r+=1
# 			j=a[i]
# 	print(r)
