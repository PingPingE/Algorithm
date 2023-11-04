'''
1~X까지 모든 원소가 나오는 index 리턴

조심해야할 조건)
N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].

O(N**2)이상인 경우, 시간초과
'''
#O(N)
def solution(X, A):
    done_set = set()
    done_N = len(done_set)

    for e, a in enumerate(A):
        if a not in done_set:
            done_set.add(a)
            done_N += 1
            if done_N == X:
                return e
    return -1

#시간초과: O(N**2)
def solution(X, A):
    check_list = [0]*(X+1)
    check_list[0] = 1
    for e,a in enumerate(A):
        if check_list[a] == 0:
            check_list[a] = 1
            if sum(check_list) == X+1:
                return e
        else: continue
    return -1


