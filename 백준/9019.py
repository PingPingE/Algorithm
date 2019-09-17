from collections import deque

def D(n):
    global done
    k = (n*2)%10000
    #중복 체크
    if k not in done:
        done[k] = (n,'D')
        return k
    return -1

def S(n):
    global done
    if n == 0:
        t = 9999
    else: t = n-1
    if t not in done:
        done[t] = (n,'S')
        return t
    return -1
def L(n):
    global done
    lt = str(n).zfill(4)
    lt =int(lt[1:]+lt[0])
    if lt not in done:
        done[lt] = (n,'L')
        return lt
    return -1
def R(n):
    global done
    rt= str(n).zfill(4)
    rt =int( rt[-1]+rt[:3])
    if rt not in done:
        done[rt] =(n,'R')
        return rt
    return -1

T = int(input())
while T>0:
    T -= 1
    A,B = map(int, input().split())
    que = deque()
    que.append(A)
    done = {}
    #어디서 왔는지(연산하기 전 값), 연산자
    done[A] = (None,None)
    stat = False
    res = ''
    while que:
        a = que.popleft()
        for tmp in [D(a),S(a),L(a),R(a)]:
            #큐에 넣기 전 매칭 체크
            if tmp == B:
                stat = True
                break
            elif tmp == -1:
                continue
            que.append(tmp)

        if stat is True:
            temp = done[B]
            #연산자를 쭉 이어 붙이고(string)
            while temp != (None,None):
                res += temp[1]
                temp = done[temp[0]]
            #거꾸로 출력
            print(res[::-1])
            break


# 숏코딩
# import collections
#
# for __ in range(int(input())):
#     f, t = map(int, input().split())
#     v = {f: (None, None)}
#     q = collections.deque(v)
#     while q and t not in v:
#         x = q.popleft()
#         for n, c in zip((x * 2 % 10000, (x - 1) % 10000, x * 10 % 10000 + x // 1000, x // 10 + x % 10 * 1000), 'DSLR'):
#             if n not in v:
#                 v[n] = (x, c)
#                 q.append(n)
#     r = ''
#     x, c = v[t]
#     while c is not None:
#         r = c + r
#         x, c = v[x]
#     print(r)