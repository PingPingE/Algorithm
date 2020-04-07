#!/bin/python3

import math
import os
import random
import re
import sys
import operator

# Complete the bigSorting function below.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    dic = {}
    for _ in range(n):
        dic[_] = int(input())
    fptr.write('\n'.join(str(dic[x]) for x in sorted(dic.keys(), key= lambda x: dic[x])))
    fptr.close()


#TLE
#Tes Case 0: 0.00015354156494140625