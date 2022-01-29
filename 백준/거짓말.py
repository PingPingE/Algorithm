'''
문제)
지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다.
지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다.
당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다. 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다.
문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다. 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다.
당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다. 지민이는 이런 일을 모두 피해야 한다.

사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다. 지민이는 모든 파티에 참가해야 한다.
이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 사람의 수 N과 파티의 수 M이 주어진다.
둘째 줄에는 이야기의 진실을 아는 사람의 수와 번호가 주어진다. 진실을 아는 사람의 수가 먼저 주어지고 그 개수만큼 사람들의 번호가 주어진다. 사람들의 번호는 1부터 N까지의 수로 주어진다.
셋째 줄부터 M개의 줄에는 각 파티마다 오는 사람의 수와 번호가 같은 방식으로 주어진다.

N, M은 50 이하의 자연수이고, 진실을 아는 사람의 수는 0 이상 50 이하의 정수, 각 파티마다 오는 사람의 수는 1 이상 50 이하의 정수이다.

출력)
첫째 줄에 문제의 정답을 출력한다.
'''
#유니온 파인드로 기존에 진실을 알고 있는 사람과 같은 파티 참석 여부 확인(같은 파티에 한번이라도 참석한다면 root가 같으니)
#123316kb	108ms
def find(x):
    if x == links[x]:
        return x
    links[x] = find(links[x])
    return links[x]

def union(a,b):
    a_ , b_ = find(a), find(b)
    if a_ > b_:
        links[a_] = b_
    else:
        links[b_] = a_

N, M = map(int, input().split())
t_list = list(map(int,input().split()[1:]))
p_list =[list(map(int,input().split()))[1:] for _ in range(M)]
links = [i for i in range(N+1)]

if not t_list:
    print(M)
else:
    ## 1. 먼저 기존에 진실을 알고 있는 사람들부터 잇기(같은 root)
    for t in t_list[1:]:
        union(t_list[0], t)

    target = t_list[0]#기준
    ans = 0
    ## 2. 각 파티 참석자들끼리 모두 잇기(같은 파티에 참석한다면 root가 같도록)
    for party in p_list:
        for participant in party[1:]:
            union(party[0], participant)

    ## 3. 이제 기존에 진실을 알고 있는 사람(1에서 이은)과 같은 root를 가졌는지 확인하여 같은 파티 참석 여부 알아내기
    for party in p_list:
        for participant in party:
            if find(participant) == find(target):
                break
        else:
            ans += 1
    # print(links)
    print(ans)

#삽질 기록
'''
from collections import deque
N, M = map(int, input().split())
t_set = set(input().split()[1:])
p_list = [set(input().split()[1:]) for _ in range(M)]
que = deque() #현재까지 진실을 아는 사람 set, 현재까지 과장한 파티 개수, 참여한 파티 index set
ans =0
for e,p in enumerate(p_list):
    if t_set & p:
        que.append([t_set|p, 0, set([e])])
    else:
        que.append([t_set|set(),1,set([e])])
print(que)

#truth_set 한명이라도 있으면 말 못하지
while que:
    truth_set,untruth_cnt,join_set= que.popleft()
    print("====", truth_set,untruth_cnt,join_set)
    if len(join_set) == M:
        ans = max(ans,untruth_cnt)
        continue

    for i in set(range(M))-join_set:
        print("-> ", i)
        if truth_set & p_list[i]:
            que.append([truth_set|p_list[i], untruth_cnt, join_set|set([i])])
        else:
            que.append([truth_set | set(), untruth_cnt+1, join_set | set([i])])

print(ans)



#t_set에 해당되는 사람과 파티를 함께 하는 사람 추가
for i in range(M):
    p = p_list[i]
    if t_set&p:
        t_set |= p
    else: pass

#t_set에 해당되는 사람이 한 명이라도 있으면 그 파티에선 진실만 말해야함
for i in range(M):
    p = p_list[i]
    if not t_set&p:
        ans += 1
print(ans)

'''