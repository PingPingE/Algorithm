#!/bin/python3
import math
import os
import random
import re
import sys
from time import time
from functools import reduce
import operator

# Complete the countSort function below.

def countSort(arr):
    s = time()
    res = ['' for _ in range(n)]
    for e, a in enumerate(arr):
        if e < n // 2:
            res[int(a[0])] += ' -'
        else:
            res[int(a[0])] += f' {a[1]}'
    #print(time()-s)#0.003016233444213867
    return f"{' '.join(r.strip() for r in res).strip()} \n {time()-s}"

def countSort2(arr): #타임아웃
    s = time()
    res = [[] for _ in range(n)]
    for e,a in enumerate(arr):
        if e<n//2:
            res[int(a[0])].append('-')
        else:
            res[int(a[0])].append(a[1])
    #print(time()-s)#0.0025320053100585938 --> 여기까진 sol1보다 이게 더 빠름
    return f"{' '.join(sum(res,[])).strip()} \n {time()-s}"#이 부분이 문제다.

def countSort3(arr):#시간 효율 1등
    s = time()
    res = [[] for _ in range(n)]
    for e,a in enumerate(arr):
        if e<n//2:
            res[int(a[0])].append('-')
        else:
            res[int(a[0])].append(a[1])
    return f"{' '.join(' '.join(r).strip() for r in res).strip()} \n {time()-s}" #개선 후

if __name__ == '__main__':
    n = int(input().strip()) #10000일때
    arr = []
    for _ in range(n):
        arr.append(input().rstrip().split())

    print(countSort(arr))
    #sol1: 0278928279876709

    print(countSort2(arr))
    #sol2: 35312509536743164

    print(countSort3(arr))
    #sol3: 008902311325073242

'''
def sol1(N):
    st = ['' for _ in range(N)]
    s1 = time()
    for _ in range(N):
        st[_] += ' i'
    st = ' '.join(s.strip() for s in st).strip()
    print(time()-s1)
    return st

def sol2(N):
    arr = [[] for _ in range(N)]
    s2 = time()
    for _ in range(N):
        arr[_].append('i')
    arr =' '.join(' '.join(r) for r in arr).strip()
    print(time()-s2)
    return arr
N=1000000
print(sol1(N) == sol2(N))
#이 경우, 비슷하거나 sol2가 더 오래 걸린다(사실 대부분 더 오래 걸렸음);;;;;;;;;;;

'''