'''
John Watson knows of an operation called a right circular rotation on an array of integers. 
One rotation operation moves the last array element to the first position and shifts all remaining elements right one. 
To test Sherlock's abilities, Watson provides Sherlock with an array of integers. 
Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

Function Description)
Complete the circularArrayRotation function in the editor below. It should return an array of integers representing the values at the specified indices.

circularArrayRotation has the following parameter(s):

a: an array of integers to rotate
k: an integer, the rotation count
queries: an array of integers, the indices to report

Input Format)

The first line contains 3 space-separated integers, n, k, and q, the number of elements in the integer array, the rotation count and the number of queries.
The second line contains n space-separated integers, where each integer  describes array element a[i] (where 0<=i<n).
Each of the q subsequent lines contains a single integer denoting m, the index of the element to return from a .

Output Format)
For each query, print the value of the element at index m of the rotated array on a new line.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    a = deque(a)
    a.rotate(k%len(a)) #k를 len(a)로 나눈 나머지만큼만 회전
    return [a[n]for n in queries]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
