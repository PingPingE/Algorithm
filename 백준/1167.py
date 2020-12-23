#참고: https://suri78.tistory.com/135 [공부노트]
#참고:https://blog.myungwoo.kr/112
#트리의 지름을 구하는 공식: 한 노드(x)에서 가장 먼 노드(y)를 찾고, 그 노드(y)에서 가장 먼 노드(z)를 찾는다.

#167868kb	644ms
import heapq
V = int(input())
links =[[] for _ in range(V+1)]#key: node, value: list((to_node, dist), ...)
for _ in range(V):
    li = list(map(int, input().split()))
    num = li[0]
    for i in range(1,len(li)-1,2):
        to_, dist = li[i], li[i+1]
        links[num].append((to_,dist))

def get_node(x):#한 정점(x) -> 모든 정점 최대거리
    que = [(0,x)]
    heapq.heapify(que)
    dists = [0 for _ in range(V+1)]
    dists[0]=-1
    done =set([x])
    while que:
        cur_dist,t = heapq.heappop(que) #min heap이므로 cur_dist는 음수값을 넣어줌
        cur_dist = -cur_dist #그래서 변환 작업이 필요
        for y, distance in links[t]:
            if y in done: continue
            if dists[y] <= cur_dist + distance:
                dists[y] = cur_dist+distance
                done.add(y)
                que.append((- dists[y],y))
    maxx = max(dists)
    ind = dists.index(maxx)
    return [maxx,ind]
tmp = get_node(1)[1] #한 노드에서 가장 먼 노드를 찾고
print(get_node(tmp)[0]) #그 노드에서 가장 먼 노드를 찾는다
