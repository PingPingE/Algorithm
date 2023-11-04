'''
list A의 길이가 N이라면,
1~N까지의 순열이 존재하는지 return 0 or 1
'''

#O(N) ~ O(NlogN)
def solution(A):
    # Implement your solution here
    N = len(A)
    set_origin = set(range(1,N+1))
    set_A = set(A)
    diff = set_origin-set_A
    if diff:
        return 0
    else:
        return 1