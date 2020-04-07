#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the bigSorting function below.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    fptr.write('\n'.join(map(str, sorted([int(input()) for _ in range(n)]))))
    fptr.close()
