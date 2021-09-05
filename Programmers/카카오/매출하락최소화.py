'''
1. 각 팀(팀장 기준)에서 팀원 중 가장 매출이 적은 팀원의 매출 저장(mini)
2. res[cur] = min(res[prev-1]+sales[prev-1], res[prev] + mini[cur]) #이전 레벨의 팀장인 팀원이 참가 or 가장 매출이 적은 팀원이 참가

문제점: 같은 레벨 팀 전체를 보지 않음
-> leaf노드 모두 탐색해야함
-> 같은 레벨의 팀들의 res도 같이 고려해서 cur의 res를 갱신할 수 있도록 해야함 
'''
from collections import defaultdict
def solution(sales, links):
    answer = 0
    INF=987654321
    mini = defaultdict(lambda:INF) #key: 팀장, value: 해당 팀의 팀원 중 가장 최소 매출액
    link = defaultdict(int) #key:노드, value: 부모 노드
    link[1]=0
    for t1,t2 in links:
        mini[t1] = min(sales[t2-1], mini[t1])
        link[t2] = t1
    # print(mini)
    #leaf노드만
    # leaf = set(range(1,1+len(sales))) - set(mini)
    def get_level(x, cnt):
        if x == 1:
            return cnt
        return get_level(link[x], cnt + 1)

    level = defaultdict(set) #key: level, value: 해당하는 노드set

    for k in link:
        level[get_level(k, 0)].add(k)

    res=[INF for _ in range(len(sales)+1)]
    # print("mini:",mini)
    # print("link:",link)
    
    def dfs(prev, cur):#이전 팀장 번호, 현 팀장 번호
        nonlocal res
        # print("prev:",prev," cur:",cur,"res:",res)
        if cur == 0:
            return
        prev_res = res[prev-1]
        # print(prev_res)
        res[cur] = min(res[cur], min((0 if prev_res==INF else prev_res)+sales[prev-1], \
                                                             res[prev] + mini[cur]))
        dfs(cur, link[cur])
        
    for i in level[max(level)]:
        res[i]=0
        dfs(i, link[i])
    # print("res:",res)
    return res[1]