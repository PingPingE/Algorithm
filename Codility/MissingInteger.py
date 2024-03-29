'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''
#O(N) or O(N * log(N))
def solution(A):
    #자료구조 선택이 관건인 문제인듯
    pos_A = set(filter(lambda x: x>0, A))
    for n in range(1,1000001):
        if n not in pos_A:
            return n