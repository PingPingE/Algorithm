#참고: https://justicehui.github.io/ps/2019/04/23/BOJ1517/
#참고: https://yangorithm.tistory.com/174
#풀이: 병합정렬로 왼쪽 배열의 원소 중 오른쪽 배열의 원소보다 큰 것이 몇 개 있는지 카운트
#222188kb	752ms
def merge(s,m,e):
    global ans,v
    tmp = []
    i,j = s,m+1
    while i<=m and j<=e:
        if v[i] > v[j]:
            tmp.append(v[j])
            j+= 1
            ans += m-i+1 #v[j]보다 더 큰 원소 개수
        else:
            tmp.append(v[i])
            i += 1
    while i<=m:
        tmp.append(v[i])
        i+= 1
    while j<=e:
        tmp.append(v[j])
        j+=1
    for b,a in enumerate(range(s,e+1)):
        v[a] = tmp[b]

def divide(s,e):
    if s<e:
        m = (s+e)//2
        divide(s,m)
        divide(m+1,e)
        merge(s,m,e)

ans = 0
N = int(input())
v = list(map(int, input().split()))
divide(0,N-1)
print(ans)