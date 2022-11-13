'''
문제)
벌목꾼 백은진은 나무를 종이 공장에 옮겨야 한다. 하지만, 통나무의 길이가 너무 길어서 트럭에 들어가지 않으므로, 여러개의 조각으로 나누려고 한다.
통나무의 길이는 L이고, K개의 위치에서만 자를 수 있다. 통나무를 자를 수 있는 위치가 주어진다. 이 위치는 통나무의 가장 왼쪽에서부터 떨어진 거리이다.
통나무를 자를 수 있는 횟수는 최대 C번이다.

통나무의 가장 긴 조각을 작게 만들고, 그 길이를 구해보자.

입력)
첫째 줄에 세 정수 L, K, C가 주어진다. 둘째 줄에는 통나무를 자를 수 있는 위치가 주어진다.

출력)
첫째 줄에 두 개의 수를 출력한다. 첫 번째 수는 가장 긴 조각의 길이이고, 두 번째 수는 그 때 처음 자르는 위치를 출력한다.
만약 가능한 것이 여러 가지라면, 처음 자르는 위치가 작은 것을 출력한다.

제한)
2 ≤ L ≤ 1,000,000,000
1 ≤ K, C ≤ 10,000
1 ≤ 자를 수 있는 위치 ≤ L
'''
L,K,C = map(int, input().split())
k_set = set(list(map(int, input().split())))
print(k_set)

#가장 긴 길이를 자를 수 없으면 굳이 볼 필요 없음
'''
while C>0
가장 긴 구간에서의 l,r
0. C-=1
1. (l+r)//2와 가장 가까운 k 선택
2. 자르기
3. ans 갱신
'''
l,r= 1, L
ans = [L+1,L+1]

while C:
    print(l,r)
    C-=1
    #중앙값
    m = (l+r)//2
    #중앙값이랑 최소로 떨어져있는 k 구하기
    diff_l, diff_r = 0, (r-m)
    sorted_k =  sorted(k_set & set(list(range(l,r+1))), key= lambda x: (abs(m-x),x))
    #없으면 이제 못자름
    if not sorted_k:
        break

    m = sorted_k[0]
    print(" m:", m)
    if m-l < r-m:
        l = m+1
    else:
        r = m

    max_len = r-l+1

    if ans[0] > max_len:
        ans[0] = max_len
        ans[1] = min(ans[1], m)

#재귀로 해야할듯?
def divide(l,r,c):
    if c ==0:
        return

    m = (l + r) // 2
    diff_l, diff_r = 0, (r - m)
    sorted_k = sorted(k_set & set(list(range(l, r + 1))), key=lambda x: (abs(m - x), x))

    if not sorted_k:
        return

    else:
        m = sorted_k[0]
        if m - l < r - m:
            l = m + 1
        else:
            r = m
        max_len = r - l + 1

print(ans[0], ans[1])





