'''
문제)
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 우표를 모으는 취미가 있듯이,
민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력)
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며,
이 값은 100,000을 넘지 않는다. 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.
친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력)
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
'''
#72612kb	372ms
import sys
sys.setrecursionlimit(10**8)
T=int(input())
def find(x):
    if x==links[x]:
        return x
    links[x]=find(links[x])
    return links[x]

def union(a,b):
    a,b=find(a), find(b)
    print(a,b)
    if a!=b:
        links[b]=a
        f_dict[a]+=f_dict[b]
    return f_dict[a]

while T:
    T-=1
    F=int(input())
    if F==0:
        print(0)
        continue
    cnt=0
    idx={}#해싱
    links={}#네트워크
    f_dict=[1 for _ in range(F*2)]#연결 개수
    while F:
        F-=1
        f1,f2=sys.stdin.readline().strip().split()
        if f1 not in idx:
            idx[f1]=cnt
            links[cnt]=cnt
            cnt+=1
        if f2 not in idx:
            idx[f2]=cnt
            links[cnt]=cnt
            cnt+=1
        print(union(idx[f1],idx[f2]))

