#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

# Complete the bigSorting function below.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    li = [int(input()) for _ in range(n)]
    heapq.heapify(li)
    while li:
        fptr.write(str(heapq.heappop(li)))
        fptr.write('\n')
    
    fptr.close()
