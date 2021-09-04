#시도 중
'''
1. 각 팀(팀장 기준)에서 팀원 중 가장 매출이 적은 팀원의 매출 저장(mini)
2. res[cur] = res[prev] + min(sales[prev-1], mini[cur]) #이전 레벨의 팀장인 팀원이 참가 or 가장 매출이 적은 팀원이 참가
'''
from collections import defaultdict
def solution(sales, links):
    answer = 0
    INF=987654321
    mini = defaultdict(lambda:INF) #key: 팀장, value: 해당 팀의 팀원 중 가장 최소 매출액
    link = defaultdict(int) #key:노드, value: 부모 노드
    link[1]=0
    for t1,t2 in links:
        mini[t1] = min(sales[t1-1], min(sales[t2-1], mini[t1]))
        link[t2] = t1
    print(mini)
    def get_degree(x, cnt):
        if x == 1:
            return cnt
        return get_degree(link[x], cnt + 1)

    degree = defaultdict(set) #key: degree, value: 해당하는 노드set

    for k in link:
        degree[get_degree(k, 0)].add(k)

    res=defaultdict(lambda:INF)
    # print(link)

    def dfs(prev, cur):#이전 팀장 번호, 현 팀장 번호
        nonlocal res
        if cur == 0:
            return
        res[cur] = res[prev] + min(sales[prev-1], mini[cur])
        dfs(cur, link[cur])


    for i in degree[max(degree)]:
        res[i]=0
        dfs(i, link[i])
    print(res)
    return res[1]