'''
문제
생태학에서 나무의 분포도를 측정하는 것은 중요하다. 그러므로 당신은 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 %를 차지하는지 구하는 프로그램을 만들어야 한다.

입력
프로그램은 여러 줄로 이루어져 있으며, 한 줄에 하나의 나무 종 이름이 주어진다. 어떤 종 이름도 30글자를 넘지 않으며, 입력에는 최대 10,000개의 종이 주어지고 최대 1,000,000그루의 나무가 주어진다.

출력
주어진 각 종의 이름을 사전순으로 출력하고, 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력한다.
'''
#125200kb	508ms
import sys
name_dic={} #key: 나무 종 이름, value: index
tree_cnt={} #key: 나무 종 index, value: 카운트
index=0
total=0 #전체 그루
for name in sys.stdin:
    if name=='\n': break
    name=name.strip()
    if name in name_dic:#이미 index가 있는 경우
        tree_cnt[name_dic[name]] += 1
    else:
        name_dic[name] = index #없으면 부여
        tree_cnt[index] = 1
        index += 1
    total+=1
for k, v in sorted(name_dic.items(), key=lambda x: x[0]):
    print(f"{k} {tree_cnt[v]/total*100:.4f}")#백분율로 소수점 4째자리까지

#sol2: 해싱없이 그냥 해보기
#127836kb	444ms ===> 더 빠르다... 
import sys
from collections import defaultdict
tree_cnt=defaultdict(int)
index=0
total=0
for name in sys.stdin:
    if name=='\n': break
    name=name.strip()
    tree_cnt[name] +=1
    total+=1
for k, v in sorted(tree_cnt.items(), key=lambda x: x[0]):
    print(f"{k} {v/total*100:.4f}")