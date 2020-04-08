#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the hackerlandRadioTransmitters function below.
def check(num):#num수 만큼 설치 했을 때 모든 집을 커버할 수 있는지
    for cand in list(combinations(x,num)):
        #x에 있어야하고 범위는 k~max(x)
        s = set()
        for c in cand:
            s.update(cc for cc in range(c-k, c+k+1) if cc in x)
        if len(s) == n:
            return True
    return False

if __name__ == '__main__':
    n,k = map(int, input().split())
    x = list(map(int, input().rstrip().split()))
    x.sort()
    high = n//k
    low = 1
    while low < high:
        mid = (low+high)//2
        if check(mid) is True:
            high = mid-1
        else:
            low = mid+1
    print(low)

#24/31 test cases failed :(